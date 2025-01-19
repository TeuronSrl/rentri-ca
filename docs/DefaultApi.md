# rentri_ca.DefaultApi

All URIs are relative to *https://demoapi.rentri.gov.it/ca-rentri/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get**](DefaultApi.md#status_get) | **GET** /status | Stato API


# **status_get**
> status_get()

Stato API

Verifica dello stato dell'API.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre un codice di stato 422) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/ca-rentri/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_ca.Configuration(
    host = "https://demoapi.rentri.gov.it/ca-rentri/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_ca.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_ca.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_ca.DefaultApi(api_client)

    try:
        # Stato API
        api_instance.status_get()
    except Exception as e:
        print("Exception when calling DefaultApi->status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

