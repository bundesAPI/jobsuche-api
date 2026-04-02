import base64
import requests

HEADERS = {
    'User-Agent': 'Jobsuche/2.9.2 (de.arbeitsagentur.jobboerse; build:1077; iOS 15.1.0) Alamofire/5.4.4',
    'Host': 'rest.arbeitsagentur.de',
    'X-API-Key': 'jobboerse-jobsuche',
    'Connection': 'keep-alive',
}

def search(what, where):
    """search for jobs. params can be found here: https://jobsuche.api.bund.dev/"""
    params = (
        ('angebotsart', '1'),
        ('page', '1'),
        ('pav', 'false'),
        ('size', '100'),
        ('umkreis', '25'),
        ('was', what),
        ('wo', where),
    )
    response = requests.get('https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/app/jobs',
                            headers=HEADERS, params=params, verify=False)
    return response.json()


def get_job_details(refnr):
    """Retrieve job details by refnr. The refnr is base64-encoded before sending."""
    encrypted = base64.b64encode(refnr.encode()).decode()
    response = requests.get(
        f'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobdetails/{encrypted}',
        headers=HEADERS, verify=False)
    return response.json()


def get_employer_logo(kundennummer_hash):
    """Retrieve employer logo by arbeitgeberKundennummerHash from job details.
    Returns None if no logo is available (404).
    """
    import urllib.parse
    encoded_hash = urllib.parse.quote(kundennummer_hash, safe='')
    response = requests.get(
        f'https://rest.arbeitsagentur.de/vermittlung/ag-darstellung-service/ct/v1/arbeitgeberlogo/{encoded_hash}',
        headers=HEADERS, verify=False)
    if response.status_code == 404:
        return None
    return response.content


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
