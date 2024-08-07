# flake8: noqa

"""
    Arbeitsagentur Jobsuche API

    Die größte Stellendatenbank Deutschlands durchsuchen, Details zu Stellenanzeigen und Informationen über Arbeitgeber abrufen. <br><br>Die Authentifizierung funktioniert über die clientId:<br><br>clientId: jobboerse-jobsuche<br><br>Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.  # noqa: E501

    The version of the OpenAPI document: 2.0.2
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


__version__ = "0.1.0"

# import ApiClient
from deutschland.jobsuche.api_client import ApiClient

# import Configuration
from deutschland.jobsuche.configuration import Configuration

# import exceptions
from deutschland.jobsuche.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)
