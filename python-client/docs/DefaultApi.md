# jobsuche.DefaultApi

All URIs are relative to *https://rest.arbeitsagentur.de/jobboerse/jobsuche-service*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ed_v1_arbeitgeberlogo_hash_id_get**](DefaultApi.md#ed_v1_arbeitgeberlogo_hash_id_get) | **GET** /ed/v1/arbeitgeberlogo/{hashID} | Unternehmen Logo
[**pc_v2_jobdetails_encoded_hash_id_get**](DefaultApi.md#pc_v2_jobdetails_encoded_hash_id_get) | **GET** /pc/v2/jobdetails/{encodedHashID} | Jobdetail
[**pc_v4_app_jobs_get**](DefaultApi.md#pc_v4_app_jobs_get) | **GET** /pc/v4/app/jobs | Jobsuche via App
[**pc_v4_jobs_get**](DefaultApi.md#pc_v4_jobs_get) | **GET** /pc/v4/jobs | Jobsuche


# **ed_v1_arbeitgeberlogo_hash_id_get**
> file_type ed_v1_arbeitgeberlogo_hash_id_get(hash_id)

Unternehmen Logo

Abrufen des Logos eines Unternehmens

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
    hash_id = "VK2qoXBe0s-UAdH_qxLDRrZrY5iY8a1PJt3MjJCXsdo=" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unternehmen Logo
        api_response = api_instance.ed_v1_arbeitgeberlogo_hash_id_get(hash_id)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->ed_v1_arbeitgeberlogo_hash_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash_id** | **str**|  |

### Return type

**file_type**

### Authorization

[APIKeyHeaders](../README.md#APIKeyHeaders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pc_v2_jobdetails_encoded_hash_id_get**
> JobDetails pc_v2_jobdetails_encoded_hash_id_get(encoded_hash_id)

Jobdetail

Abrufen von Details zu einem Job.

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
    encoded_hash_id = "VK2qoXBe0s-UAdH_qxLDRrZrY5iY8a1PJt3MjJCXsdo=" # str | Hash-ID eines Jobs (siehe JobSearchResponse), enkodiert mit Base64

    # example passing only required values which don't have defaults set
    try:
        # Jobdetail
        api_response = api_instance.pc_v2_jobdetails_encoded_hash_id_get(encoded_hash_id)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->pc_v2_jobdetails_encoded_hash_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encoded_hash_id** | **str**| Hash-ID eines Jobs (siehe JobSearchResponse), enkodiert mit Base64 |

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

