# rentri_ca.GestioneCredenzialiApi

All URIs are relative to *https://api.rentri.gov.it/ca-rentri/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credentials_boarding_qrcode_token_get**](GestioneCredenzialiApi.md#credentials_boarding_qrcode_token_get) | **GET** /credentials/boarding/{qrcode_token} | Informazioni boarding
[**credentials_credentials_id_change_pin_put**](GestioneCredenzialiApi.md#credentials_credentials_id_change_pin_put) | **PUT** /credentials/{credentials_id}/change-pin | Cambio PIN
[**credentials_credentials_id_delete**](GestioneCredenzialiApi.md#credentials_credentials_id_delete) | **DELETE** /credentials/{credentials_id} | Elimina credenziali
[**credentials_credentials_id_get**](GestioneCredenzialiApi.md#credentials_credentials_id_get) | **GET** /credentials/{credentials_id} | Dettaglio credenziali
[**credentials_credentials_id_reset_pin_put**](GestioneCredenzialiApi.md#credentials_credentials_id_reset_pin_put) | **PUT** /credentials/{credentials_id}/reset-pin | Reset PIN
[**credentials_credentials_id_rimuovi_associazione_delete**](GestioneCredenzialiApi.md#credentials_credentials_id_rimuovi_associazione_delete) | **DELETE** /credentials/{credentials_id}/rimuovi-associazione | Rimuovi associazione credenziali
[**credentials_credentials_id_status_get**](GestioneCredenzialiApi.md#credentials_credentials_id_status_get) | **GET** /credentials/{credentials_id}/status | Stato credenziali


# **credentials_boarding_qrcode_token_get**
> BoardingAccessResponse credentials_boarding_qrcode_token_get(qrcode_token, pin)

Informazioni boarding

Verifica se il codice di boarding specificato è attivo e restituisce le informazioni necessarie al dispositivo per creare delle nuove credenziali.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_ca
from rentri_ca.models.boarding_access_response import BoardingAccessResponse
from rentri_ca.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/ca-rentri/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_ca.Configuration(
    host = "https://api.rentri.gov.it/ca-rentri/v1.0"
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
    api_instance = rentri_ca.GestioneCredenzialiApi(api_client)
    qrcode_token = 'qrcode_token_example' # str | Token letto dal QR Code di boarding.
    pin = 'pin_example' # str | PIN di boarding.

    try:
        # Informazioni boarding
        api_response = api_instance.credentials_boarding_qrcode_token_get(qrcode_token, pin)
        print("The response of GestioneCredenzialiApi->credentials_boarding_qrcode_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GestioneCredenzialiApi->credentials_boarding_qrcode_token_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qrcode_token** | **str**| Token letto dal QR Code di boarding. | 
 **pin** | **str**| PIN di boarding. | 

### Return type

[**BoardingAccessResponse**](BoardingAccessResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accesso consentito. |  -  |
**403** | Parametri per il boarding non validi. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_credentials_id_change_pin_put**
> credentials_credentials_id_change_pin_put(credentials_id, change_pin_request=change_pin_request)

Cambio PIN

Imposta un nuovo PIN operativo per le credenziali specificate.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_ca
from rentri_ca.models.change_pin_request import ChangePinRequest
from rentri_ca.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/ca-rentri/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_ca.Configuration(
    host = "https://api.rentri.gov.it/ca-rentri/v1.0"
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
    api_instance = rentri_ca.GestioneCredenzialiApi(api_client)
    credentials_id = 'credentials_id_example' # str | Identificativo delle credenziali
    change_pin_request = rentri_ca.ChangePinRequest() # ChangePinRequest | Dati delle credenziali e nuovo PIN. (optional)

    try:
        # Cambio PIN
        api_instance.credentials_credentials_id_change_pin_put(credentials_id, change_pin_request=change_pin_request)
    except Exception as e:
        print("Exception when calling GestioneCredenzialiApi->credentials_credentials_id_change_pin_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| Identificativo delle credenziali | 
 **change_pin_request** | [**ChangePinRequest**](ChangePinRequest.md)| Dati delle credenziali e nuovo PIN. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PIN operativo modificato correttamente. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Credenziali non trovate. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_credentials_id_delete**
> credentials_credentials_id_delete(credentials_id)

Elimina credenziali

Elimina le credenziali indicate.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_ca
from rentri_ca.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/ca-rentri/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_ca.Configuration(
    host = "https://api.rentri.gov.it/ca-rentri/v1.0"
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
    api_instance = rentri_ca.GestioneCredenzialiApi(api_client)
    credentials_id = 'credentials_id_example' # str | Identificativo delle credenziali da eliminare.

    try:
        # Elimina credenziali
        api_instance.credentials_credentials_id_delete(credentials_id)
    except Exception as e:
        print("Exception when calling GestioneCredenzialiApi->credentials_credentials_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| Identificativo delle credenziali da eliminare. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Credenziali eliminate. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Credenziali non trovate. |  -  |
**422** | Eliminazione del dispositivo associato non riuscita. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_credentials_id_get**
> CredentialsModel credentials_credentials_id_get(credentials_id)

Dettaglio credenziali

Ottiene le informazioni di dettaglio delle credenziali specificate.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_ca
from rentri_ca.models.credentials_model import CredentialsModel
from rentri_ca.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/ca-rentri/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_ca.Configuration(
    host = "https://api.rentri.gov.it/ca-rentri/v1.0"
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
    api_instance = rentri_ca.GestioneCredenzialiApi(api_client)
    credentials_id = 'credentials_id_example' # str | Identificativo delle credenziali.

    try:
        # Dettaglio credenziali
        api_response = api_instance.credentials_credentials_id_get(credentials_id)
        print("The response of GestioneCredenzialiApi->credentials_credentials_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GestioneCredenzialiApi->credentials_credentials_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| Identificativo delle credenziali. | 

### Return type

[**CredentialsModel**](CredentialsModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dettaglio delle credenziali. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Credenziali non trovate. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_credentials_id_reset_pin_put**
> credentials_credentials_id_reset_pin_put(credentials_id, reset_pin_request=reset_pin_request)

Reset PIN

Completa la procedura di reset del PIN operativo avviata tramite la dashboard di gestione dei dispositivi, impostando un nuovo PIN per le credenziali specificate.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_ca
from rentri_ca.models.reset_pin_request import ResetPinRequest
from rentri_ca.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/ca-rentri/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_ca.Configuration(
    host = "https://api.rentri.gov.it/ca-rentri/v1.0"
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
    api_instance = rentri_ca.GestioneCredenzialiApi(api_client)
    credentials_id = 'credentials_id_example' # str | Identificativo delle credenziali
    reset_pin_request = rentri_ca.ResetPinRequest() # ResetPinRequest | Dati delle credenziali e nuovo PIN. (optional)

    try:
        # Reset PIN
        api_instance.credentials_credentials_id_reset_pin_put(credentials_id, reset_pin_request=reset_pin_request)
    except Exception as e:
        print("Exception when calling GestioneCredenzialiApi->credentials_credentials_id_reset_pin_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| Identificativo delle credenziali | 
 **reset_pin_request** | [**ResetPinRequest**](ResetPinRequest.md)| Dati delle credenziali e nuovo PIN. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Procedura di reset del PIN operativo completata e nuovo PIN impostato correttamente. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Credenziali non trovate. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_credentials_id_rimuovi_associazione_delete**
> credentials_credentials_id_rimuovi_associazione_delete(credentials_id, num_iscr_sito)

Rimuovi associazione credenziali

Rimuove l'associazione delle credenziali con l'operatore o con l'unità locale specificata.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_ca
from rentri_ca.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/ca-rentri/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_ca.Configuration(
    host = "https://api.rentri.gov.it/ca-rentri/v1.0"
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
    api_instance = rentri_ca.GestioneCredenzialiApi(api_client)
    credentials_id = 'credentials_id_example' # str | Identificativo delle credenziali.
    num_iscr_sito = 'num_iscr_sito_example' # str | Identificativo dell'unità locale da rimuovere.

    try:
        # Rimuovi associazione credenziali
        api_instance.credentials_credentials_id_rimuovi_associazione_delete(credentials_id, num_iscr_sito)
    except Exception as e:
        print("Exception when calling GestioneCredenzialiApi->credentials_credentials_id_rimuovi_associazione_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| Identificativo delle credenziali. | 
 **num_iscr_sito** | **str**| Identificativo dell&#39;unità locale da rimuovere. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Associazione eliminata. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Credenziali non trovate. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_credentials_id_status_get**
> CredentialsStatusResponse credentials_credentials_id_status_get(credentials_id)

Stato credenziali

Ottiene le informazioni sullo stato delle credenziali.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_ca
from rentri_ca.models.credentials_status_response import CredentialsStatusResponse
from rentri_ca.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/ca-rentri/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_ca.Configuration(
    host = "https://api.rentri.gov.it/ca-rentri/v1.0"
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
    api_instance = rentri_ca.GestioneCredenzialiApi(api_client)
    credentials_id = 'credentials_id_example' # str | Identificativo delle credenziali.

    try:
        # Stato credenziali
        api_response = api_instance.credentials_credentials_id_status_get(credentials_id)
        print("The response of GestioneCredenzialiApi->credentials_credentials_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GestioneCredenzialiApi->credentials_credentials_id_status_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| Identificativo delle credenziali. | 

### Return type

[**CredentialsStatusResponse**](CredentialsStatusResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stato delle credenziali. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Credenziali non trovate. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

