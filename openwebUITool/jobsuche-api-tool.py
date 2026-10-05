"""
title: Arbeitsagentur Jobsuche
author: you
version: 1.1.0
license: MIT
description: Search job postings in Germany's largest job database (Bundesagentur für Arbeit) and fetch full job details. Based on https://github.com/bundesAPI/jobsuche-api
requirements: httpx
"""

import base64
import html
import re
from typing import Any, Awaitable, Callable, Dict, List, Optional

import httpx
from pydantic import BaseModel, Field

EventEmitter = Optional[Callable[[Dict[str, Any]], Awaitable[None]]]

# Friendly aliases so the model can pass natural words instead of API codes.
ARBEITSZEIT_ALIASES = {
    "vollzeit": "vz",
    "full-time": "vz",
    "fulltime": "vz",
    "teilzeit": "tz",
    "part-time": "tz",
    "parttime": "tz",
    "schicht": "snw",
    "nachtarbeit": "snw",
    "wochenende": "snw",
    "homeoffice": "ho",
    "home-office": "ho",
    "remote": "ho",
    "telearbeit": "ho",
    "minijob": "mj",
    "mini-job": "mj",
}
ARBEITSZEIT_VALID = {"vz", "tz", "snw", "ho", "mj"}

ANGEBOTSART_ALIASES = {
    "arbeit": "1",
    "job": "1",
    "stelle": "1",
    "work": "1",
    "selbstaendigkeit": "2",
    "selbständigkeit": "2",
    "selbstständig": "2",
    "freelance": "2",
    "ausbildung": "4",
    "duales studium": "4",
    "studium": "4",
    "apprenticeship": "4",
    "praktikum": "34",
    "trainee": "34",
    "internship": "34",
}
ANGEBOTSART_VALID = {"1", "2", "4", "34"}

BEFRISTUNG_ALIASES = {
    "befristet": "1",
    "temporary": "1",
    "fixed-term": "1",
    "unbefristet": "2",
    "permanent": "2",
}
BEFRISTUNG_VALID = {"1", "2"}

JOB_PAGE_URL = "https://www.arbeitsagentur.de/jobsuche/jobdetail/{refnr}"


def _normalize(
    value: Optional[str], aliases: Dict[str, str], valid: set
) -> Optional[str]:
    """Turn 'Vollzeit, Homeoffice' into 'vz;ho'. Unknown values are dropped."""
    if not value:
        return None
    out: List[str] = []
    for part in re.split(r"[;,|]", str(value)):
        p = part.strip().lower()
        if not p:
            continue
        p = aliases.get(p, p)
        if p in valid and p not in out:
            out.append(p)
    return ";".join(out) or None


def _clean_text(text: Optional[str]) -> str:
    """Strip HTML tags/entities and collapse whitespace."""
    if not text:
        return ""
    text = re.sub(r"<\s*br\s*/?\s*>|</\s*(p|li|div|h\d)\s*>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return text.strip()


def _extract_jobs(data: Any) -> List[Dict[str, Any]]:
    """Find the list of job entries regardless of the exact response key."""
    if not isinstance(data, dict):
        return []
    # The live /pc/v6/jobs endpoint returns the list under `ergebnisliste`.
    jobs = data.get("ergebnisliste")
    if isinstance(jobs, list) and jobs:
        return jobs
    if isinstance(jobs, dict):  # `ergebnisliste` may be nested under another key
        for v in jobs.values():
            if isinstance(v, list) and v and isinstance(v[0], dict):
                return v
    jobs = data.get("stellenangebote")
    if isinstance(jobs, list) and jobs:
        return jobs
    markers = (
        "referenznummer",
        "refnr",
        "hauptberuf",
        "stellenangebotsTitel",
        "beruf",
        "titel",
        "firma",
        "arbeitgeber",
        "hashId",
    )
    for key, val in data.items():
        if (
            isinstance(val, list)
            and val
            and isinstance(val[0], dict)
            and any(m in val[0] for m in markers)
        ):
            return val
        if isinstance(val, dict):  # one level of nesting, e.g. {"_embedded": {...}}
            inner = _extract_jobs(val)
            if inner:
                return inner
    return []


def _job_worktime(job: Dict[str, Any]) -> str:
    """Build a human-readable working-time label from boolean v6 flags."""
    flags = [
        (job.get("arbeitszeitVollzeit"), "full-time"),
        (job.get("arbeitszeitTeilzeitAbend"), "part-time (PM)"),
        (job.get("arbeitszeitTeilzeitVormittag"), "part-time (AM)"),
        (job.get("arbeitszeitTeilzeitFlexibel"), "part-time (flex)"),
        (job.get("arbeitszeitSchichtNachtWochenende"), "shift/weekend"),
        (job.get("istGeringfuegigeBeschaeftigung"), "mini-job"),
    ]
    parts = [label for flag, label in flags if flag]
    if job.get("homeofficemoeglich"):
        parts.append("home office")
    return ", ".join(parts) or "n/a"


def _first_date(obj: Any, key: str) -> str:
    """Return the 'von' date from a `{von: ..., bis: ...}` period object."""
    if isinstance(obj, dict):
        return str(obj.get(key) or "").strip()
    return str(obj or "").strip()


def _place(ort: Any) -> str:
    """Format a single location. Accepts a plain address dict (plz/ort/region/land)
    or a list of `stellenlokationen` entries (each `{adresse: {...}}`)."""
    if not ort:
        return "n/a"
    # List of location entries (both search and detail responses use this shape).
    if isinstance(ort, list):
        places = [
            _place(item.get("adresse") if isinstance(item, dict) else item)
            for item in ort
        ]
        places = [p for p in places if p and p != "n/a"]
        return "; ".join(places) if places else "n/a"
    if isinstance(ort, str):
        return ort.strip() or "n/a"
    if not isinstance(ort, dict):
        return str(ort)
    plz = str(ort.get("plz") or "").strip()
    ort_name = str(ort.get("ort") or "").strip()
    region = str(ort.get("region") or "").strip()
    land = str(ort.get("land") or "").strip()
    place = ", ".join(x for x in [plz, ort_name] if x)
    if (
        region
        and region.upper() not in (ort_name.upper(),)
        and region.upper() != land.upper()
    ):
        place = f"{place}, {region}" if place else region
    if land and land.upper() not in (region.upper(),):
        place = f"{place}, {land}" if place else land
    return place or "n/a"


class Tools:
    class Valves(BaseModel):
        BASE_URL: str = Field(
            default="https://rest.arbeitsagentur.de/jobboerse/jobsuche-service",
            description="Base URL of the Jobsuche service",
        )
        API_KEY: str = Field(
            default="jobboerse-jobsuche",
            description="Value for the X-API-Key header (public clientId)",
        )
        USER_AGENT: str = Field(
            default="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
            description="User-Agent header sent to the API",
        )
        TIMEOUT_SECONDS: int = Field(default=30, description="HTTP timeout")
        DEFAULT_RESULTS: int = Field(
            default=10, description="Default number of results per search"
        )
        MAX_RESULTS: int = Field(
            default=50, description="Upper limit for results per search"
        )
        MAX_DESCRIPTION_CHARS: int = Field(
            default=6000,
            description="Truncate long job descriptions to this many characters",
        )

    def __init__(self):
        self.valves = self.Valves()

    # ------------------------------------------------------------------ helpers

    def _headers(self) -> Dict[str, str]:
        return {
            "X-API-Key": self.valves.API_KEY,
            "Accept": "application/json",
            "User-Agent": self.valves.USER_AGENT,
        }

    async def _status(
        self, emitter: EventEmitter, description: str, done: bool = False
    ):
        if emitter:
            await emitter(
                {"type": "status", "data": {"description": description, "done": done}}
            )

    # ------------------------------------------------------------------ tools

    async def search_jobs(
        self,
        was: Optional[str] = None,
        wo: Optional[str] = None,
        umkreis: Optional[int] = None,
        arbeitszeit: Optional[str] = None,
        angebotsart: Optional[str] = None,
        befristung: Optional[str] = None,
        veroeffentlichtseit: Optional[int] = None,
        berufsfeld: Optional[str] = None,
        arbeitgeber: Optional[str] = None,
        zeitarbeit: Optional[bool] = None,
        page: int = 1,
        size: Optional[int] = None,
        __event_emitter__: EventEmitter = None,
    ) -> str:
        """
        Search current job postings in Germany (Bundesagentur für Arbeit).
        Returns a list of jobs, each with a reference number (refnr) that can be
        passed to get_job_details for the full description.

        :param was: Free-text search for job title / keywords, e.g. "Softwareentwickler" or "Pflegefachkraft".
        :param wo: Free-text location, e.g. "München" or "Berlin" or a postal code.
        :param umkreis: Search radius in kilometres around `wo`, e.g. 25 or 100.
        :param arbeitszeit: Working-time model. One or more of: vollzeit, teilzeit, homeoffice, minijob, schicht (or the raw codes vz, tz, ho, mj, snw). Separate multiple values with a comma or semicolon.
        :param angebotsart: Type of offer: arbeit (regular job, default), selbstaendigkeit, ausbildung (apprenticeship / dual study), praktikum (internship / trainee). Raw codes 1, 2, 4, 34 also work.
        :param befristung: Contract type: befristet (fixed-term) and/or unbefristet (permanent). Raw codes 1, 2 also work.
        :param veroeffentlichtseit: Only jobs published within the last N days (0-100).
        :param berufsfeld: Optional occupational field filter. Usually leave EMPTY and put keywords in `was` instead; this filter can be very restrictive.
        :param arbeitgeber: Employer name, e.g. "Deutsche Bahn AG".
        :param zeitarbeit: Set to false to exclude temp-agency postings. Defaults to including them.
        :param page: Result page, starting at 1.
        :param size: Number of results per page (default from settings, max 50).
        :return: Markdown list of matching job postings.
        """
        limit = max(
            1, min(size or self.valves.DEFAULT_RESULTS, self.valves.MAX_RESULTS)
        )

        params: Dict[str, Any] = {
            "was": was,
            "wo": wo,
            "umkreis": umkreis,
            "arbeitszeit": _normalize(
                arbeitszeit, ARBEITSZEIT_ALIASES, ARBEITSZEIT_VALID
            ),
            "angebotsart": _normalize(
                angebotsart, ANGEBOTSART_ALIASES, ANGEBOTSART_VALID
            ),
            "befristung": _normalize(befristung, BEFRISTUNG_ALIASES, BEFRISTUNG_VALID),
            "veroeffentlichtseit": veroeffentlichtseit,
            "berufsfeld": berufsfeld,
            "arbeitgeber": arbeitgeber,
            "zeitarbeit": None if zeitarbeit is None else str(zeitarbeit).lower(),
            "page": max(1, page),
            "size": limit,
        }
        params = {k: v for k, v in params.items() if v not in (None, "")}
        if umkreis and not wo:
            params.pop("umkreis", None)  # radius is meaningless without a location

        await self._status(__event_emitter__, "Searching Arbeitsagentur job database…")

        base = self.valves.BASE_URL.rstrip("/")
        endpoints = [
            f"{base}/pc/v6/jobs",
            f"{base}/pc/v4/jobs",
            f"{base}/pc/v4/app/jobs",
        ]
        # Second variant drops the (often too strict) berufsfeld filter.
        variants = [params]
        if "berufsfeld" in params:
            variants.append({k: v for k, v in params.items() if k != "berufsfeld"})

        data: Dict[str, Any] = {}
        jobs: List[Dict[str, Any]] = []
        used_params = params
        diagnostics: List[str] = []

        try:
            async with httpx.AsyncClient(
                timeout=self.valves.TIMEOUT_SECONDS,
                headers=self._headers(),
                follow_redirects=True,
            ) as client:
                for variant in variants:
                    for url in endpoints:
                        try:
                            resp = await client.get(url, params=variant)
                        except httpx.HTTPError as e:
                            diagnostics.append(f"{url}: {type(e).__name__}: {e}")
                            continue
                        if resp.status_code != 200:
                            diagnostics.append(
                                f"{url}: HTTP {resp.status_code} {resp.text[:150]!r}"
                            )
                            continue
                        try:
                            payload = resp.json()
                        except ValueError:
                            diagnostics.append(
                                f"{url}: HTTP 200 but not JSON: {resp.text[:150]!r}"
                            )
                            continue
                        found = _extract_jobs(payload)
                        if found:
                            data, jobs, used_params = payload, found, variant
                            break
                        keys = (
                            list(payload.keys())
                            if isinstance(payload, dict)
                            else type(payload).__name__
                        )
                        diagnostics.append(
                            f"{resp.url}: HTTP 200, no jobs found; top-level keys: {keys}; "
                            f"maxErgebnisse={payload.get('maxErgebnisse') if isinstance(payload, dict) else None}"
                        )
                    if jobs:
                        break
        except Exception as e:  # pragma: no cover
            diagnostics.append(f"Unexpected error: {type(e).__name__}: {e}")

        total = data.get("maxErgebnisse")
        await self._status(
            __event_emitter__, f"Found {len(jobs)} job(s) on this page", done=True
        )

        if not jobs:
            return "No job postings were returned. This does NOT necessarily mean the API is down; " "do not claim that to the user. Debug info:\n- Params: " + str(
                params
            ) + "\n- " + "\n- ".join(
                diagnostics or ["(no details)"]
            )

        note = ""
        if used_params is not params:
            note = "_(The berufsfeld filter returned nothing, so it was ignored.)_\n\n"

        header = f"**{total} total matches**, " if total else ""
        lines = [
            note + f"{header}showing {len(jobs)} (page {params.get('page', 1)}):",
            "",
        ]

        for i, job in enumerate(jobs, 1):
            refnr = job.get("referenznummer") or job.get("refnr") or ""
            title = (
                job.get("stellenangebotsTitel")
                or job.get("hauptberuf")
                or job.get("titel")
                or "Untitled"
            )
            employer = job.get("firma") or job.get("arbeitgeber") or "n/a"
            # v6: dates are period objects {"von": "..."}; fall back to flat keys.
            published = (
                _first_date(job.get("veroeffentlichungszeitraum"), "von")
                or job.get("aktuelleVeroeffentlichungsdatum")
                or "n/a"
            )
            start = (
                _first_date(job.get("eintrittszeitraum"), "von")
                or job.get("eintrittsdatum")
                or ""
            )
            locations = (
                job.get("stellenlokationen")
                or job.get("arbeitsorte")
                or job.get("arbeitsort")
            )
            worktime = _job_worktime(job)
            offer_type = job.get("stellenangebotsart") or ""
            link = (
                job.get("externeURL")
                or job.get("externeUrl")
                or (JOB_PAGE_URL.format(refnr=refnr) if refnr else "")
            )

            lines.append(f"### {i}. {title} — {employer}")
            lines.append(f"- **Location:** {_place(locations)}")
            lines.append(
                f"- **Working time:** {worktime}"
                + (f" | **Type:** {offer_type}" if offer_type else "")
            )
            lines.append(
                f"- **Published:** {published}"
                + (f" | **Start:** {start}" if start else "")
            )
            if refnr:
                lines.append(f"- **refnr:** `{refnr}`")
            if link:
                lines.append(f"- **Link:** {link}")
            lines.append("")

        lines.append("Use get_job_details with a refnr for the full description.")
        return "\n".join(lines)

    async def get_job_details(
        self,
        refnr: str,
        __event_emitter__: EventEmitter = None,
    ) -> str:
        """
        Get the full details of one job posting (description, salary info,
        working time, contract type, employer, locations, skills).

        :param refnr: The reference number of the job from search_jobs, e.g. "10001-1002716922-S". A full arbeitsagentur.de job URL is also accepted.
        :return: Markdown with the complete job details.
        """
        refnr = (refnr or "").strip().rstrip("/").split("/")[-1]
        if not refnr:
            return "Error: a refnr is required."

        encoded = base64.b64encode(refnr.encode()).decode()
        base = self.valves.BASE_URL.rstrip("/")
        await self._status(__event_emitter__, f"Loading details for {refnr}…")

        data: Optional[Dict[str, Any]] = None
        last_error = ""
        try:
            async with httpx.AsyncClient(
                timeout=self.valves.TIMEOUT_SECONDS, headers=self._headers()
            ) as client:
                # v4 is the recommended and working endpoint (v3 currently 403s).
                for version in ("v4",):
                    try:
                        resp = await client.get(
                            f"{base}/pc/{version}/jobdetails/{encoded}"
                        )
                        if resp.status_code == 404:
                            last_error = "job not found (it may have expired)"
                            continue
                        resp.raise_for_status()
                        data = resp.json()
                        break
                    except (httpx.HTTPError, ValueError) as e:
                        last_error = f"{type(e).__name__}: {e}"
        except Exception as e:  # pragma: no cover
            last_error = str(e)

        if data is None:
            await self._status(
                __event_emitter__, "Could not load job details", done=True
            )
            return f"Error: could not load job `{refnr}` ({last_error})."

        await self._status(__event_emitter__, "Job details loaded", done=True)

        title = (
            data.get("stellenangebotsTitel")
            or data.get("titel")
            or data.get("hauptberuf")
            or data.get("beruf")
            or "Untitled"
        )
        employer = data.get("firma") or data.get("arbeitgeber") or "n/a"
        if data.get("anzeigeAnonym"):
            employer = "Anonymous"

        out = [f"# {title}", f"**Employer:** {employer}", ""]

        orte = data.get("stellenlokationen") or data.get("arbeitsorte") or []
        if orte:
            out.append(f"**Location(s):** {_place(orte)}")

        # Build a readable salary string from the v4 pay fields.
        salary = ""
        span_lo, span_hi = data.get("gehaltsspanneVon"), data.get("gehaltsspanneBis")
        if data.get("verguetungsangabe") and data["verguetungsangabe"] not in (
            "KEINE_ANGABEN",
        ):
            salary = str(data["verguetungsangabe"])
            kind = data.get("artDerVerguetung")
            if kind and kind != salary:
                salary += f" ({kind})"
            if span_lo is not None or span_hi is not None:
                salary += f": {span_lo or '—'} – {span_hi or '—'} €"

        facts = [
            ("Offer type", data.get("stellenangebotsart")),
            ("Working time", _job_worktime(data)),
            ("Contract", data.get("vertragsdauer")),
            (
                "Take-over possible",
                {True: "yes", False: None}.get(data.get("uebernahme")),
            ),
            ("Salary / pay", salary or None),
            ("Open positions", data.get("anzahlOffeneStellen")),
            ("Industry", data.get("branche") or data.get("branchengruppe")),
            ("Occupation", data.get("hauptberuf") or data.get("beruf")),
            (
                "Start date",
                _first_date(data.get("eintrittszeitraum"), "von")
                or data.get("eintrittsdatum"),
            ),
            (
                "Published",
                _first_date(data.get("veroeffentlichungszeitraum"), "von")
                or data.get("aktuelleVeroeffentlichungsdatum"),
            ),
            (
                "First published",
                data.get("datumErsteVeroeffentlichung")
                or data.get("ersteVeroeffentlichungsdatum"),
            ),
            (
                "Crossing into the field (Quereinstieg) possible",
                {True: "yes", False: None}.get(data.get("quereinstiegGeeignet")),
            ),
        ]
        for label, value in facts:
            if value not in (None, "", []):
                out.append(f"- **{label}:** {value}")

        skills: List[str] = []
        for f in data.get("fertigkeiten") or []:
            name = f.get("hierarchieName")
            ausp = f.get("auspraegungen")
            items: List[str] = []
            if isinstance(ausp, dict):
                for v in ausp.values():
                    items.extend(v if isinstance(v, list) else [v])
            skills.append(
                name + (": " + ", ".join(map(str, items)) if items else "")
                if name
                else ""
            )
        skills = [s for s in skills if s]
        if skills:
            out += ["", "**Skills:** " + " | ".join(skills)]

        description = _clean_text(
            data.get("stellenangebotsBeschreibung") or data.get("stellenbeschreibung")
        )
        if description:
            limit = self.valves.MAX_DESCRIPTION_CHARS
            if len(description) > limit:
                description = description[:limit].rstrip() + " … [truncated]"
            out += ["", "## Description", description]

        employer_info = _clean_text(data.get("arbeitgeberdarstellung"))
        if employer_info:
            out += ["", "## About the employer", employer_info[:1500]]

        out.append("")
        if data.get("arbeitgeberdarstellungUrl"):
            out.append(f"**Employer website:** {data['arbeitgeberdarstellungUrl']}")
        partner = data.get("allianzpartnerName") or data.get("allianzpartner")
        if data.get("allianzpartnerUrl") and partner not in (
            None,
            "arbeitsagentur.de",
            "Anonymous",
        ):
            out.append(f"**Source ({partner}):** {data['allianzpartnerUrl']}")
        out.append(
            f"**Apply / view on arbeitsagentur.de:** {JOB_PAGE_URL.format(refnr=refnr)}"
        )

        return "\n".join(out)
