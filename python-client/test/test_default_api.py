"""
    Arbeitsagentur Jobsuche API

    Die größte Stellendatenbank Deutschlands durchsuchen, Details zu Stellenanzeigen und Informationen über Arbeitgeber abrufen. <br><br>Die Authentifizierung funktioniert über die clientId:<br><br>clientId: jobboerse-jobsuche<br><br>Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.  # noqa: E501

    The version of the OpenAPI document: 2.0.2
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""

import unittest

from deutschland.jobsuche.api.default_api import DefaultApi  # noqa: E501

from deutschland import jobsuche


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ed_v1_arbeitgeberlogo_hash_id_get(self):
        """Test case for ed_v1_arbeitgeberlogo_hash_id_get

        Unternehmen Logo  # noqa: E501
        """
        pass

    def test_pc_v4_app_jobs_get(self):
        """Test case for pc_v4_app_jobs_get

        Jobsuche via App  # noqa: E501
        """
        pass

    def test_pc_v4_jobs_get(self):
        """Test case for pc_v4_jobs_get

        Jobsuche  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
