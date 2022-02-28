"""
    Arbeitsagentur Jobsuche API

    Die größte Stellendatenbank Deutschlands durchsuchen, Details zu Stellenanzeigen und Informationen über Arbeitgeber abrufen. <br><br> Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:<br><br> **ClientID:** c003a37f-024f-462a-b36d-b001be4cd24a <br> **ClientSecret:** 32a39620-32b3-4307-9aa1-511e3d7f48a8. **Achtung**: der OAuth header muss 'OAuthAccessToken' heißen.<br><br> Die API verfügt außerdem nicht über ein gültiges TLS Zertifikat. Deswegen sollte die TLS-Validierung deaktiviert werden.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.jobsuche.model.job_application_details_angebotskontakt import (
    JobApplicationDetailsAngebotskontakt,
)

from deutschland import jobsuche

globals()["JobApplicationDetailsAngebotskontakt"] = JobApplicationDetailsAngebotskontakt
from deutschland.jobsuche.model.job_application_details import JobApplicationDetails


class TestJobApplicationDetails(unittest.TestCase):
    """JobApplicationDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobApplicationDetails(self):
        """Test JobApplicationDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JobApplicationDetails()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()