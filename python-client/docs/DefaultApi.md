# jobsuche.DefaultApi

All URIs are relative to *https://rest.arbeitsagentur.de/jobboerse/jobsuche-service*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ct_v1_arbeitgeberlogo_kundennummer_hash_get**](DefaultApi.md#ct_v1_arbeitgeberlogo_kundennummer_hash_get) | **GET** /ct/v1/arbeitgeberlogo/{kundennummerHash} | Unternehmen Logo
[**pc_v3_jobdetails_encrypted_job_code_get**](DefaultApi.md#pc_v3_jobdetails_encrypted_job_code_get) | **GET** /pc/v3/jobdetails/{encryptedJobCode} | Jobdetails (v3)
[**pc_v4_app_jobs_get**](DefaultApi.md#pc_v4_app_jobs_get) | **GET** /pc/v4/app/jobs | Jobsuche via App
[**pc_v4_jobdetails_encrypted_job_code_get**](DefaultApi.md#pc_v4_jobdetails_encrypted_job_code_get) | **GET** /pc/v4/jobdetails/{encryptedJobCode} | Jobdetails (v4)
[**pc_v4_jobs_get**](DefaultApi.md#pc_v4_jobs_get) | **GET** /pc/v4/jobs | Jobsuche


# **ct_v1_arbeitgeberlogo_kundennummer_hash_get**
> file_type ct_v1_arbeitgeberlogo_kundennummer_hash_get(kundennummer_hash)

Unternehmen Logo

Abrufen des Logos eines Unternehmens anhand des arbeitgeberKundennummerHash aus der Jobdetail-Antwort. Gibt 404 zurück, wenn kein Logo vorhanden ist.

### Example

* Api Key Authentication (APIKeyHeaders):

```python
import time
from deutschland import jobsuche
from deutschland.jobsuche.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.arbeitsagentur.de/jobboerse/jobsuche-service
# See configuration.py for a list of all supported configuration parameters.
configuration = jobsuche.Configuration(
    host = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeaders
configuration.api_key['APIKeyHeaders'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeaders'] = 'Bearer'

# Enter a context with an instance of the API client
with jobsuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    kundennummer_hash = "Z-HzVkUCLGQiQFxQSAICs302sSdB9Sp7XtgOiO4GGCA=" # str | Wert des Feldes arbeitgeberKundennummerHash aus der Jobdetail-Antwort (URL-kodiert falls nötig).

    # example passing only required values which don't have defaults set
    try:
        # Unternehmen Logo
        api_response = api_instance.ct_v1_arbeitgeberlogo_kundennummer_hash_get(kundennummer_hash)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->ct_v1_arbeitgeberlogo_kundennummer_hash_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kundennummer_hash** | **str**| Wert des Feldes arbeitgeberKundennummerHash aus der Jobdetail-Antwort (URL-kodiert falls nötig). |

### Return type

**file_type**

### Authorization

[APIKeyHeaders](../README.md#APIKeyHeaders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/webp, image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Kein Logo für diesen Arbeitgeber vorhanden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pc_v3_jobdetails_encrypted_job_code_get**
> JobDetails pc_v3_jobdetails_encrypted_job_code_get(encrypted_job_code)

Jobdetails (v3)

Abrufen der Details einer Stellenanzeige anhand des Base64-kodierten Referenzwertes (base64(refnr)).

### Example

* Api Key Authentication (APIKeyHeaders):

```python
import time
from deutschland import jobsuche
from deutschland.jobsuche.api import default_api
from deutschland.jobsuche.model.job_details import JobDetails
from pprint import pprint
# Defining the host is optional and defaults to https://rest.arbeitsagentur.de/jobboerse/jobsuche-service
# See configuration.py for a list of all supported configuration parameters.
configuration = jobsuche.Configuration(
    host = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeaders
configuration.api_key['APIKeyHeaders'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeaders'] = 'Bearer'

# Enter a context with an instance of the API client
with jobsuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    encrypted_job_code = "MTAwMDEtMTAwMjcxNjkyMi1T" # str | Base64-kodierter Wert der refnr aus der Jobsuche. Beispiel: base64('10001-1002716922-S') = 'MTAwMDEtMTAwMjcxNjkyMi1T'

    # example passing only required values which don't have defaults set
    try:
        # Jobdetails (v3)
        api_response = api_instance.pc_v3_jobdetails_encrypted_job_code_get(encrypted_job_code)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->pc_v3_jobdetails_encrypted_job_code_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypted_job_code** | **str**| Base64-kodierter Wert der refnr aus der Jobsuche. Beispiel: base64(&#39;10001-1002716922-S&#39;) &#x3D; &#39;MTAwMDEtMTAwMjcxNjkyMi1T&#39; |

### Return type

[**JobDetails**](JobDetails.md)

### Authorization

[APIKeyHeaders](../README.md#APIKeyHeaders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pc_v4_app_jobs_get**
> JobSearchResponse pc_v4_app_jobs_get()

Jobsuche via App

Die Jobsuche via App ermöglicht verfügbare Jobangebote mit verschiedenen get Parametern zu filtern.

### Example

* Api Key Authentication (APIKeyHeaders):

```python
import time
from deutschland import jobsuche
from deutschland.jobsuche.api import default_api
from deutschland.jobsuche.model.job_search_response import JobSearchResponse
from pprint import pprint
# Defining the host is optional and defaults to https://rest.arbeitsagentur.de/jobboerse/jobsuche-service
# See configuration.py for a list of all supported configuration parameters.
configuration = jobsuche.Configuration(
    host = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeaders
configuration.api_key['APIKeyHeaders'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeaders'] = 'Bearer'

# Enter a context with an instance of the API client
with jobsuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    was = "Referatsleiter" # str | Freitext suche Jobtitel (optional)
    wo = "Berlin" # str | Freitext suche Beschäftigungsort (optional)
    berufsfeld = "Informatik" # str | Freitext suche Berufsfeld (optional)
    page = 1 # int | Ergebnissseite (optional)
    size = 50 # int | Anzahl von Ergebnissen (optional)
    arbeitgeber = "Deutsche%20Bahn%20AG" # str | Arbeitgeber der Stelle (optional)
    veroeffentlichtseit = 30 # int | Anzahl der Tage, seit der Job veröffentlicht wurde. Kann zwischen 0 und 100 Tagen liegen. (optional)
    zeitarbeit = True # bool | Gibt an, ob Jobs von Zeitarbeitsfirmen in die Suchergebnisse einbezogen werden sollen (default true). (optional)
    angebotsart = 1 # int | 1=ARBEIT; 2=SELBSTAENDIGKEIT, 4=AUSBILDUNG/Duales Studium, 34=Praktikum/Trainee (optional)
    befristung = 1 # int | Semikolon-separierte mehrere Werte möglich (z.B. befristung=1;2) 1 = befristet; 2 = unbefristet (optional)
    arbeitszeit = "vz" # str | Semikolon-separierte mehrere Werte möglich (z.B. arbeitszeit=vz;tz) vz=VOLLZEIT, tz=TEILZEIT, snw=SCHICHT_NACHTARBEIT_WOCHENENDE, ho=HEIM_TELEARBEIT, mj=MINIJOB (optional)
    behinderung = True # bool |  (optional)
    corona = True # bool | Wenn true, werden nur Jobs die im Kontext von Corona angeboten werden angezeigt. (optional)
    umkreis = 25 # int | Umkreis in Kilometern von Wo-Parameter. (z.B. 25 oder 200) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Jobsuche via App
        api_response = api_instance.pc_v4_app_jobs_get(was=was, wo=wo, berufsfeld=berufsfeld, page=page, size=size, arbeitgeber=arbeitgeber, veroeffentlichtseit=veroeffentlichtseit, zeitarbeit=zeitarbeit, angebotsart=angebotsart, befristung=befristung, arbeitszeit=arbeitszeit, behinderung=behinderung, corona=corona, umkreis=umkreis)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->pc_v4_app_jobs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **was** | **str**| Freitext suche Jobtitel | [optional]
 **wo** | **str**| Freitext suche Beschäftigungsort | [optional]
 **berufsfeld** | **str**| Freitext suche Berufsfeld | [optional]
 **page** | **int**| Ergebnissseite | [optional]
 **size** | **int**| Anzahl von Ergebnissen | [optional]
 **arbeitgeber** | **str**| Arbeitgeber der Stelle | [optional]
 **veroeffentlichtseit** | **int**| Anzahl der Tage, seit der Job veröffentlicht wurde. Kann zwischen 0 und 100 Tagen liegen. | [optional]
 **zeitarbeit** | **bool**| Gibt an, ob Jobs von Zeitarbeitsfirmen in die Suchergebnisse einbezogen werden sollen (default true). | [optional]
 **angebotsart** | **int**| 1&#x3D;ARBEIT; 2&#x3D;SELBSTAENDIGKEIT, 4&#x3D;AUSBILDUNG/Duales Studium, 34&#x3D;Praktikum/Trainee | [optional]
 **befristung** | **int**| Semikolon-separierte mehrere Werte möglich (z.B. befristung&#x3D;1;2) 1 &#x3D; befristet; 2 &#x3D; unbefristet | [optional]
 **arbeitszeit** | **str**| Semikolon-separierte mehrere Werte möglich (z.B. arbeitszeit&#x3D;vz;tz) vz&#x3D;VOLLZEIT, tz&#x3D;TEILZEIT, snw&#x3D;SCHICHT_NACHTARBEIT_WOCHENENDE, ho&#x3D;HEIM_TELEARBEIT, mj&#x3D;MINIJOB | [optional]
 **behinderung** | **bool**|  | [optional]
 **corona** | **bool**| Wenn true, werden nur Jobs die im Kontext von Corona angeboten werden angezeigt. | [optional]
 **umkreis** | **int**| Umkreis in Kilometern von Wo-Parameter. (z.B. 25 oder 200) | [optional]

### Return type

[**JobSearchResponse**](JobSearchResponse.md)

### Authorization

[APIKeyHeaders](../README.md#APIKeyHeaders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pc_v4_jobdetails_encrypted_job_code_get**
> JobDetails pc_v4_jobdetails_encrypted_job_code_get(encrypted_job_code)

Jobdetails (v4)

Abrufen der Details einer Stellenanzeige anhand des Base64-kodierten Referenzwertes (base64(refnr)). Empfohlene Version.

### Example

* Api Key Authentication (APIKeyHeaders):

```python
import time
from deutschland import jobsuche
from deutschland.jobsuche.api import default_api
from deutschland.jobsuche.model.job_details import JobDetails
from pprint import pprint
# Defining the host is optional and defaults to https://rest.arbeitsagentur.de/jobboerse/jobsuche-service
# See configuration.py for a list of all supported configuration parameters.
configuration = jobsuche.Configuration(
    host = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeaders
configuration.api_key['APIKeyHeaders'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeaders'] = 'Bearer'

# Enter a context with an instance of the API client
with jobsuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    encrypted_job_code = "MTAwMDEtMTAwMjcxNjkyMi1T" # str | Base64-kodierter Wert der refnr aus der Jobsuche. Beispiel: base64('10001-1002716922-S') = 'MTAwMDEtMTAwMjcxNjkyMi1T'

    # example passing only required values which don't have defaults set
    try:
        # Jobdetails (v4)
        api_response = api_instance.pc_v4_jobdetails_encrypted_job_code_get(encrypted_job_code)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->pc_v4_jobdetails_encrypted_job_code_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypted_job_code** | **str**| Base64-kodierter Wert der refnr aus der Jobsuche. Beispiel: base64(&#39;10001-1002716922-S&#39;) &#x3D; &#39;MTAwMDEtMTAwMjcxNjkyMi1T&#39; |

### Return type

[**JobDetails**](JobDetails.md)

### Authorization

[APIKeyHeaders](../README.md#APIKeyHeaders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pc_v4_jobs_get**
> JobSearchResponse pc_v4_jobs_get()

Jobsuche

Die Jobsuche ermöglicht verfügbare Jobangebote mit verschiedenen get Parametern zu filtern.

### Example

* Api Key Authentication (APIKeyHeaders):

```python
import time
from deutschland import jobsuche
from deutschland.jobsuche.api import default_api
from deutschland.jobsuche.model.job_search_response import JobSearchResponse
from pprint import pprint
# Defining the host is optional and defaults to https://rest.arbeitsagentur.de/jobboerse/jobsuche-service
# See configuration.py for a list of all supported configuration parameters.
configuration = jobsuche.Configuration(
    host = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeaders
configuration.api_key['APIKeyHeaders'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeaders'] = 'Bearer'

# Enter a context with an instance of the API client
with jobsuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    was = "Referatsleiter" # str | Freitext suche Jobtitel (optional)
    wo = "Berlin" # str | Freitext suche Beschäftigungsort (optional)
    berufsfeld = "Informatik" # str | Freitext suche Berufsfeld (optional)
    page = 1 # int | Ergebnissseite (optional)
    size = 50 # int | Anzahl von Ergebnissen (optional)
    arbeitgeber = "Deutsche%20Bahn%20AG" # str | Arbeitgeber der Stelle (optional)
    veroeffentlichtseit = 30 # int | Anzahl der Tage, seit der Job veröffentlicht wurde. Kann zwischen 0 und 100 Tagen liegen. (optional)
    zeitarbeit = True # bool | Gibt an, ob Jobs von Zeitarbeitsfirmen in die Suchergebnisse einbezogen werden sollen (default true). (optional)
    angebotsart = 1 # int | 1=ARBEIT; 2=SELBSTAENDIGKEIT, 4=AUSBILDUNG/Duales Studium, 34=Praktikum/Trainee (optional)
    befristung = 1 # int | Semikolon-separierte mehrere Werte möglich (z.B. befristung=1;2) 1 = befristet; 2 = unbefristet (optional)
    arbeitszeit = "vz" # str | Semikolon-separierte mehrere Werte möglich (z.B. arbeitszeit=vz;tz) vz=VOLLZEIT, tz=TEILZEIT, snw=SCHICHT_NACHTARBEIT_WOCHENENDE, ho=HEIM_TELEARBEIT, mj=MINIJOB (optional)
    behinderung = True # bool |  (optional)
    corona = True # bool | Wenn true, werden nur Jobs die im Kontext von Corona angeboten werden angezeigt. (optional)
    umkreis = 25 # int | Umkreis in Kilometern von Wo-Parameter. (z.B. 25 oder 200) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Jobsuche
        api_response = api_instance.pc_v4_jobs_get(was=was, wo=wo, berufsfeld=berufsfeld, page=page, size=size, arbeitgeber=arbeitgeber, veroeffentlichtseit=veroeffentlichtseit, zeitarbeit=zeitarbeit, angebotsart=angebotsart, befristung=befristung, arbeitszeit=arbeitszeit, behinderung=behinderung, corona=corona, umkreis=umkreis)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->pc_v4_jobs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **was** | **str**| Freitext suche Jobtitel | [optional]
 **wo** | **str**| Freitext suche Beschäftigungsort | [optional]
 **berufsfeld** | **str**| Freitext suche Berufsfeld | [optional]
 **page** | **int**| Ergebnissseite | [optional]
 **size** | **int**| Anzahl von Ergebnissen | [optional]
 **arbeitgeber** | **str**| Arbeitgeber der Stelle | [optional]
 **veroeffentlichtseit** | **int**| Anzahl der Tage, seit der Job veröffentlicht wurde. Kann zwischen 0 und 100 Tagen liegen. | [optional]
 **zeitarbeit** | **bool**| Gibt an, ob Jobs von Zeitarbeitsfirmen in die Suchergebnisse einbezogen werden sollen (default true). | [optional]
 **angebotsart** | **int**| 1&#x3D;ARBEIT; 2&#x3D;SELBSTAENDIGKEIT, 4&#x3D;AUSBILDUNG/Duales Studium, 34&#x3D;Praktikum/Trainee | [optional]
 **befristung** | **int**| Semikolon-separierte mehrere Werte möglich (z.B. befristung&#x3D;1;2) 1 &#x3D; befristet; 2 &#x3D; unbefristet | [optional]
 **arbeitszeit** | **str**| Semikolon-separierte mehrere Werte möglich (z.B. arbeitszeit&#x3D;vz;tz) vz&#x3D;VOLLZEIT, tz&#x3D;TEILZEIT, snw&#x3D;SCHICHT_NACHTARBEIT_WOCHENENDE, ho&#x3D;HEIM_TELEARBEIT, mj&#x3D;MINIJOB | [optional]
 **behinderung** | **bool**|  | [optional]
 **corona** | **bool**| Wenn true, werden nur Jobs die im Kontext von Corona angeboten werden angezeigt. | [optional]
 **umkreis** | **int**| Umkreis in Kilometern von Wo-Parameter. (z.B. 25 oder 200) | [optional]

### Return type

[**JobSearchResponse**](JobSearchResponse.md)

### Authorization

[APIKeyHeaders](../README.md#APIKeyHeaders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

