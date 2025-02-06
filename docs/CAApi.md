# rentri_ca.CAApi

All URIs are relative to *https://demoapi.rentri.gov.it/ca-rentri/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ca_num_seriale_ca_cert_crl_get**](CAApi.md#ca_num_seriale_ca_cert_crl_get) | **GET** /ca/{num_seriale_ca_cert}/crl | CRL
[**ca_num_seriale_ca_cert_get**](CAApi.md#ca_num_seriale_ca_cert_get) | **GET** /ca/{num_seriale_ca_cert} | Certificato CA


# **ca_num_seriale_ca_cert_crl_get**
> bytearray ca_num_seriale_ca_cert_crl_get(num_seriale_ca_cert)

CRL

Ottiene la CRL della CA RENTRI.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
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
    api_instance = rentri_ca.CAApi(api_client)
    num_seriale_ca_cert = 56 # int | Numero di serire del certificato CA

    try:
        # CRL
        api_response = api_instance.ca_num_seriale_ca_cert_crl_get(num_seriale_ca_cert)
        print("The response of CAApi->ca_num_seriale_ca_cert_crl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CAApi->ca_num_seriale_ca_cert_crl_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_seriale_ca_cert** | **int**| Numero di serire del certificato CA | 

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CRL della CA RENTRI. |  -  |
**403** | Operazione non consentita. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ca_num_seriale_ca_cert_get**
> CertificateModel ca_num_seriale_ca_cert_get(num_seriale_ca_cert)

Certificato CA

Ottiene il certificato di CA col numero di serie specificato<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_ca
from rentri_ca.models.certificate_model import CertificateModel
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
    api_instance = rentri_ca.CAApi(api_client)
    num_seriale_ca_cert = 56 # int | Numero di serire del certificato CA

    try:
        # Certificato CA
        api_response = api_instance.ca_num_seriale_ca_cert_get(num_seriale_ca_cert)
        print("The response of CAApi->ca_num_seriale_ca_cert_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CAApi->ca_num_seriale_ca_cert_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_seriale_ca_cert** | **int**| Numero di serire del certificato CA | 

### Return type

[**CertificateModel**](CertificateModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CRL della CA RENTRI. |  -  |
**403** | Operazione non consentita. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

