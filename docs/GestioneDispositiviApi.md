# rentri_ca.GestioneDispositiviApi

All URIs are relative to *https://demoapi.rentri.gov.it/ca-rentri/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_device_id_identificativo_soggetto_get**](GestioneDispositiviApi.md#devices_device_id_identificativo_soggetto_get) | **GET** /devices/{device_id}/{identificativo_soggetto} | Dettaglio dispositivo
[**devices_get**](GestioneDispositiviApi.md#devices_get) | **GET** /devices | Elenco dispositivi
[**devices_sync_put**](GestioneDispositiviApi.md#devices_sync_put) | **PUT** /devices/sync | Sincronizza dispositivo


# **devices_device_id_identificativo_soggetto_get**
> DeviceModel devices_device_id_identificativo_soggetto_get(device_id, identificativo_soggetto)

Dettaglio dispositivo

Ottiene informazioni di dettaglio di un dispositivo.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.device_model import DeviceModel
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
    api_instance = rentri_ca.GestioneDispositiviApi(api_client)
    device_id = 'device_id_example' # str | Criteri di ricerca dei dispositivi.
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Identificativo del soggetto.

    try:
        # Dettaglio dispositivo
        api_response = api_instance.devices_device_id_identificativo_soggetto_get(device_id, identificativo_soggetto)
        print("The response of GestioneDispositiviApi->devices_device_id_identificativo_soggetto_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GestioneDispositiviApi->devices_device_id_identificativo_soggetto_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Criteri di ricerca dei dispositivi. | 
 **identificativo_soggetto** | **str**| Identificativo del soggetto. | 

### Return type

[**DeviceModel**](DeviceModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Informazioni su dispositivo, app e credenziali. |  -  |
**403** | Operazione non consentita per il Soggetto. |  -  |
**404** | Dispositivo non trovati. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get**
> List[DeviceModel] devices_get(identificativo_soggetto, user_name=user_name, device_id=device_id, credentials_id=credentials_id, attivi=attivi, paging_page=paging_page, paging_page_size=paging_page_size)

Elenco dispositivi

Ottiene l'elenco dei dispositivi, filtrati in base ai criteri specificati.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.device_model import DeviceModel
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
    api_instance = rentri_ca.GestioneDispositiviApi(api_client)
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Identificativo del soggetto.
    user_name = 'user_name_example' # str | Identificativo dell'utente (da SPID, CIE, CNS). (optional)
    device_id = 'device_id_example' # str | Identificativo del dispositivo. (optional)
    credentials_id = 'credentials_id_example' # str | Identificativo delle credenziali. (optional)
    attivi = True # bool | Indica se includere solamente i dispositivi attivi. (optional)
    paging_page = 1 # int | Valore per l'header Paging-Page. (optional) (default to 1)
    paging_page_size = 50 # int | Valore per l'header Paging-PageSize. (optional) (default to 50)

    try:
        # Elenco dispositivi
        api_response = api_instance.devices_get(identificativo_soggetto, user_name=user_name, device_id=device_id, credentials_id=credentials_id, attivi=attivi, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of GestioneDispositiviApi->devices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GestioneDispositiviApi->devices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo_soggetto** | **str**| Identificativo del soggetto. | 
 **user_name** | **str**| Identificativo dell&#39;utente (da SPID, CIE, CNS). | [optional] 
 **device_id** | **str**| Identificativo del dispositivo. | [optional] 
 **credentials_id** | **str**| Identificativo delle credenziali. | [optional] 
 **attivi** | **bool**| Indica se includere solamente i dispositivi attivi. | [optional] 
 **paging_page** | **int**| Valore per l&#39;header Paging-Page. | [optional] [default to 1]
 **paging_page_size** | **int**| Valore per l&#39;header Paging-PageSize. | [optional] [default to 50]

### Return type

[**List[DeviceModel]**](DeviceModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elenco dei dispositivi corrispondenti ai criteri di ricerca specificati. |  * Paging-PageCount - Numero totale di pagine. <br>  * Paging-Page - Numero di pagina. <br>  * Paging-PageSize - Dimensione della pagina. <br>  * Paging-TotalRecordCount - Numero totale di record. <br>  |
**403** | Operazione non consentita per il Soggetto. |  -  |
**404** | Dispositivi non trovati. |  -  |
**422** | Unprocessable Content |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_sync_put**
> devices_sync_put(sync_device_info_request=sync_device_info_request)

Sincronizza dispositivo

Sincronizza le informazioni del dispositivo specificato e dell'app installata.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.sync_device_info_request import SyncDeviceInfoRequest
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
    api_instance = rentri_ca.GestioneDispositiviApi(api_client)
    sync_device_info_request = rentri_ca.SyncDeviceInfoRequest() # SyncDeviceInfoRequest | Dati del dispositivo. (optional)

    try:
        # Sincronizza dispositivo
        api_instance.devices_sync_put(sync_device_info_request=sync_device_info_request)
    except Exception as e:
        print("Exception when calling GestioneDispositiviApi->devices_sync_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_device_info_request** | [**SyncDeviceInfoRequest**](SyncDeviceInfoRequest.md)| Dati del dispositivo. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Informazioni del dispositivo sincronizzate correttamente. |  -  |
**401** | Dispositivo non autorizzato. |  -  |
**403** | Operazione non consentita per il dispositivo. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

