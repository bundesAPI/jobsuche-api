import base64
import urllib.parse
from typing import Any, Dict, Optional

import requests

HEADERS = {
    'User-Agent': 'Jobsuche/2.9.2 (de.arbeitsagentur.jobboerse; build:1077; iOS 15.1.0) Alamofire/5.4.4',
    'Host': 'rest.arbeitsagentur.de',
    'X-API-Key': 'jobboerse-jobsuche',
    'Connection': 'keep-alive',
}


def search(what: str, where: str) -> Dict[str, Any]:
    """Stellenanzeigen suchen.

    Die verfügbaren Parameter sind unter https://jobsuche.api.bund.dev/
    dokumentiert.
    """
    params = (
        ('angebotsart', '1'),
        ('page', '1'),
        ('pav', 'false'),
        ('size', '100'),
        ('umkreis', '25'),
        ('was', what),
        ('wo', where),
    )
    response = requests.get(
        'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/app/jobs',
        headers=HEADERS, params=params, timeout=60)
    response.raise_for_status()
    return response.json()


def get_job_details(refnr: str) -> Dict[str, Any]:
    """Jobdetails anhand der Referenznummer abrufen.

    Die ``refnr`` wird vor dem Aufruf Base64-kodiert.
    """
    encrypted = base64.b64encode(refnr.encode()).decode()
    response = requests.get(
        f'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobdetails/{encrypted}',
        headers=HEADERS, timeout=60)
    response.raise_for_status()
    return response.json()


def get_employer_logo(kundennummer_hash: str) -> Optional[bytes]:
    """Arbeitgeberlogo anhand des ``arbeitgeberKundennummerHash`` abrufen.

    Gibt ``None`` zurück, wenn kein Logo für diesen Arbeitgeber hinterlegt
    ist (HTTP 404). Dies ist ein regulärer Fall, kein Fehler.
    """
    encoded_hash = urllib.parse.quote(kundennummer_hash, safe='')
    response = requests.get(
        f'https://rest.arbeitsagentur.de/vermittlung/ag-darstellung-service/ct/v1/arbeitgeberlogo/{encoded_hash}',
        headers=HEADERS, timeout=60)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.content


if __name__ == "__main__":
    result = search("bahn", "berlin")

    refnr = result['stellenangebote'][0]["refnr"]
    print("refnr:", refnr)

    details = get_job_details(refnr)
    print("Titel:", details.get("stellenangebotsTitel") or details.get("titel"))

    kundennummer_hash = details.get("arbeitgeberKundennummerHash")
    if kundennummer_hash:
        logo = get_employer_logo(kundennummer_hash)
        if logo:
            print("Logo gefunden, Größe:", len(logo), "Bytes")
        else:
            print("Kein Logo für diesen Arbeitgeber vorhanden.")
    else:
        print("Kein arbeitgeberKundennummerHash – kein Logo verfügbar.")
