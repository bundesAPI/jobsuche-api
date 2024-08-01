import requests

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
    headers = {
        'User-Agent': 'Jobsuche/2.9.2 (de.arbeitsagentur.jobboerse; build:1077; iOS 15.1.0) Alamofire/5.4.4',
        'Host': 'rest.arbeitsagentur.de',
        'X-API-Key': 'jobboerse-jobsuche',
        'Connection': 'keep-alive',
    }
    response = requests.get('https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/app/jobs',
                            headers=headers, params=params, verify=False)
    return response.json()

result = search("bahn", "berlin")

print(result['stellenangebote'][0]["refnr"])
