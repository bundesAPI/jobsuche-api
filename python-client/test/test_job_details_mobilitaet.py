"""
    Arbeitsagentur Jobsuche API

    Die größte Stellendatenbank Deutschlands durchsuchen, Details zu Stellenanzeigen und Informationen über Arbeitgeber abrufen. <br><br>Die Authentifizierung funktioniert über die clientId:<br><br>clientId: jobboerse-jobsuche<br><br>Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.  # noqa: E501

    The version of the OpenAPI document: 2.0.2
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.jobsuche.model.job_details_mobilitaet import JobDetailsMobilitaet

from deutschland import jobsuche


class TestJobDetailsMobilitaet(unittest.TestCase):
    """JobDetailsMobilitaet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobDetailsMobilitaet(self):
        """Test JobDetailsMobilitaet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JobDetailsMobilitaet()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
