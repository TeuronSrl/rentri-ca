# rentri_ca.CSCFirmaRemotaRENTRIApi

All URIs are relative to *https://demoapi.rentri.gov.it/ca-rentri/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credentials_authorize_check_handle_get**](CSCFirmaRemotaRENTRIApi.md#credentials_authorize_check_handle_get) | **GET** /credentials/authorize-check/{handle} | Verifica autorizzazione credenziali
[**credentials_authorize_check_handle_get_0**](CSCFirmaRemotaRENTRIApi.md#credentials_authorize_check_handle_get_0) | **GET** /credentials/authorizeCheck/{handle} | ⚠️[DEPRECATO] - utilizzare /credentials/authorize-check/{handle} - Verifica autorizzazione credenziali
[**credentials_authorize_confirmation_put**](CSCFirmaRemotaRENTRIApi.md#credentials_authorize_confirmation_put) | **PUT** /credentials/authorize-confirmation | Imposta autorizzazione credenziali
[**credentials_authorize_confirmation_put_0**](CSCFirmaRemotaRENTRIApi.md#credentials_authorize_confirmation_put_0) | **PUT** /credentials/authorizeConfirmation | ⚠️[DEPRECATO] - utilizzare /credentials/authorize-confirmation - Imposta autorizzazione credenziali
[**credentials_authorize_post**](CSCFirmaRemotaRENTRIApi.md#credentials_authorize_post) | **POST** /credentials/authorize | Autorizza credenziali
[**credentials_info_get**](CSCFirmaRemotaRENTRIApi.md#credentials_info_get) | **GET** /credentials/info | Informazioni credenziali
[**credentials_list_get**](CSCFirmaRemotaRENTRIApi.md#credentials_list_get) | **GET** /credentials/list | Elenco credenziali soggetto
[**credentials_post**](CSCFirmaRemotaRENTRIApi.md#credentials_post) | **POST** /credentials | Crea/aggiorna credenziali
[**info_get**](CSCFirmaRemotaRENTRIApi.md#info_get) | **GET** /info | Info servizio
[**signatures_sign_hash_post**](CSCFirmaRemotaRENTRIApi.md#signatures_sign_hash_post) | **POST** /signatures/sign-hash | Firma hash
[**signatures_sign_hash_post_0**](CSCFirmaRemotaRENTRIApi.md#signatures_sign_hash_post_0) | **POST** /signatures/signHash | ⚠️[DEPRECATO] - utilizzare /signatures/sign-hash - Firma hash


# **credentials_authorize_check_handle_get**
> CredentialsAuthorizeResponse credentials_authorize_check_handle_get(handle)

Verifica autorizzazione credenziali

Verifica lo stato dell'autorizzazione delle credenziali.  Per ulteriori informazioni consultare la documentazione del CSC (Cloud Signature Consortium) al link: https://cloudsignatureconsortium.org/download-api-specifications/.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.credentials_authorize_response import CredentialsAuthorizeResponse
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
    api_instance = rentri_ca.CSCFirmaRemotaRENTRIApi(api_client)
    handle = 'handle_example' # str | Handle del SAD per verificare lo stato di autorizzazione della richiesta.

    try:
        # Verifica autorizzazione credenziali
        api_response = api_instance.credentials_authorize_check_handle_get(handle)
        print("The response of CSCFirmaRemotaRENTRIApi->credentials_authorize_check_handle_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSCFirmaRemotaRENTRIApi->credentials_authorize_check_handle_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**| Handle del SAD per verificare lo stato di autorizzazione della richiesta. | 

### Return type

[**CredentialsAuthorizeResponse**](CredentialsAuthorizeResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Autorizzazione concessa. |  -  |
**202** | Autorizzazione in attesa. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**422** | Notifica al dispositivo per la richiesta di autorizzazione non inviata. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_authorize_check_handle_get_0**
> CredentialsAuthorizeResponse credentials_authorize_check_handle_get_0(handle)

⚠️[DEPRECATO] - utilizzare /credentials/authorize-check/{handle} - Verifica autorizzazione credenziali

Verifica lo stato dell'autorizzazione delle credenziali.  Per ulteriori informazioni consultare la documentazione del CSC (Cloud Signature Consortium) al link: https://cloudsignatureconsortium.org/download-api-specifications/.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.credentials_authorize_response import CredentialsAuthorizeResponse
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
    api_instance = rentri_ca.CSCFirmaRemotaRENTRIApi(api_client)
    handle = 'handle_example' # str | Handle del SAD per verificare lo stato di autorizzazione della richiesta.

    try:
        # ⚠️[DEPRECATO] - utilizzare /credentials/authorize-check/{handle} - Verifica autorizzazione credenziali
        api_response = api_instance.credentials_authorize_check_handle_get_0(handle)
        print("The response of CSCFirmaRemotaRENTRIApi->credentials_authorize_check_handle_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSCFirmaRemotaRENTRIApi->credentials_authorize_check_handle_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**| Handle del SAD per verificare lo stato di autorizzazione della richiesta. | 

### Return type

[**CredentialsAuthorizeResponse**](CredentialsAuthorizeResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Autorizzazione concessa. |  -  |
**202** | Autorizzazione in attesa. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**422** | Notifica al dispositivo per la richiesta di autorizzazione non inviata. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_authorize_confirmation_put**
> credentials_authorize_confirmation_put(credentials_authorize_confirmation_request=credentials_authorize_confirmation_request)

Imposta autorizzazione credenziali

Imposta lo stato di una richiesta di autorizzazione delle credenziali.  Per ulteriori informazioni consultare la documentazione del CSC (Cloud Signature Consortium) al link: https://cloudsignatureconsortium.org/download-api-specifications/.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.credentials_authorize_confirmation_request import CredentialsAuthorizeConfirmationRequest
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
    api_instance = rentri_ca.CSCFirmaRemotaRENTRIApi(api_client)
    credentials_authorize_confirmation_request = rentri_ca.CredentialsAuthorizeConfirmationRequest() # CredentialsAuthorizeConfirmationRequest | Dati per l'impostazione dell'autorizzazione. (optional)

    try:
        # Imposta autorizzazione credenziali
        api_instance.credentials_authorize_confirmation_put(credentials_authorize_confirmation_request=credentials_authorize_confirmation_request)
    except Exception as e:
        print("Exception when calling CSCFirmaRemotaRENTRIApi->credentials_authorize_confirmation_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_authorize_confirmation_request** | [**CredentialsAuthorizeConfirmationRequest**](CredentialsAuthorizeConfirmationRequest.md)| Dati per l&#39;impostazione dell&#39;autorizzazione. | [optional] 

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
**202** | Stato dell&#39;autorizzazione aggiornato. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Credenziali non trovate. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_authorize_confirmation_put_0**
> credentials_authorize_confirmation_put_0(credentials_authorize_confirmation_request=credentials_authorize_confirmation_request)

⚠️[DEPRECATO] - utilizzare /credentials/authorize-confirmation - Imposta autorizzazione credenziali

Imposta lo stato di una richiesta di autorizzazione delle credenziali.  Per ulteriori informazioni consultare la documentazione del CSC (Cloud Signature Consortium) al link: https://cloudsignatureconsortium.org/download-api-specifications/.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.credentials_authorize_confirmation_request import CredentialsAuthorizeConfirmationRequest
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
    api_instance = rentri_ca.CSCFirmaRemotaRENTRIApi(api_client)
    credentials_authorize_confirmation_request = rentri_ca.CredentialsAuthorizeConfirmationRequest() # CredentialsAuthorizeConfirmationRequest | Dati per l'impostazione dell'autorizzazione. (optional)

    try:
        # ⚠️[DEPRECATO] - utilizzare /credentials/authorize-confirmation - Imposta autorizzazione credenziali
        api_instance.credentials_authorize_confirmation_put_0(credentials_authorize_confirmation_request=credentials_authorize_confirmation_request)
    except Exception as e:
        print("Exception when calling CSCFirmaRemotaRENTRIApi->credentials_authorize_confirmation_put_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_authorize_confirmation_request** | [**CredentialsAuthorizeConfirmationRequest**](CredentialsAuthorizeConfirmationRequest.md)| Dati per l&#39;impostazione dell&#39;autorizzazione. | [optional] 

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
**202** | Stato dell&#39;autorizzazione aggiornato. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Credenziali non trovate. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_authorize_post**
> CredentialsAuthorizeResponse credentials_authorize_post(credentials_authorize_request=credentials_authorize_request)

Autorizza credenziali

Autorizza l'accesso alle credenziali per la firma.  Per ulteriori informazioni consultare la documentazione del CSC (Cloud Signature Consortium) al link: https://cloudsignatureconsortium.org/download-api-specifications/.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.credentials_authorize_request import CredentialsAuthorizeRequest
from rentri_ca.models.credentials_authorize_response import CredentialsAuthorizeResponse
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
    api_instance = rentri_ca.CSCFirmaRemotaRENTRIApi(api_client)
    credentials_authorize_request = rentri_ca.CredentialsAuthorizeRequest() # CredentialsAuthorizeRequest | Dati delle credenziali da autorizzare. (optional)

    try:
        # Autorizza credenziali
        api_response = api_instance.credentials_authorize_post(credentials_authorize_request=credentials_authorize_request)
        print("The response of CSCFirmaRemotaRENTRIApi->credentials_authorize_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSCFirmaRemotaRENTRIApi->credentials_authorize_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_authorize_request** | [**CredentialsAuthorizeRequest**](CredentialsAuthorizeRequest.md)| Dati delle credenziali da autorizzare. | [optional] 

### Return type

[**CredentialsAuthorizeResponse**](CredentialsAuthorizeResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Autorizzazione concessa. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Credenziali non trovate. |  -  |
**422** | Invio della notifica al dispositivo non riuscita. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_info_get**
> CredentialsInfoResponse credentials_info_get(credentials_id, certificates=certificates, cert_info=cert_info, auth_info=auth_info, lang=lang, client_data=client_data)

Informazioni credenziali

Ottiene le informazioni sull'identità principale ed il certificato (o la catena di certificati) ad esso associata.  Per ulteriori informazioni consultare la documentazione del CSC (Cloud Signature Consortium) al link: https://cloudsignatureconsortium.org/download-api-specifications/.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.credentials_info_response import CredentialsInfoResponse
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
    api_instance = rentri_ca.CSCFirmaRemotaRENTRIApi(api_client)
    credentials_id = 'credentials_id_example' # str | Identificativo delle credenziali.
    certificates = rentri_ca.CredentialsCertificate() # CredentialsCertificate | Specifica quali certificati dalla catena devono essere restituiti. - none: nessuno - single: solo il certificato dell'identità finale - chain: l'intera catena dei certificati (optional)
    cert_info = True # bool | Indica se includere nella risposta anche i parametri contenenti informazioni relative al certificato. (optional)
    auth_info = True # bool | Indica se includere nella risposta anche i parametri contenenti informazioni sul meccanismo di autorizzazione supportato dalle credenziali. (optional)
    lang = 'lang_example' # str | Lingua prescelta per la risposta, specificata secondo RFC 5646. (optional)
    client_data = 'client_data_example' # str | Dati arbitrari dell'applicazione di firma. (optional)

    try:
        # Informazioni credenziali
        api_response = api_instance.credentials_info_get(credentials_id, certificates=certificates, cert_info=cert_info, auth_info=auth_info, lang=lang, client_data=client_data)
        print("The response of CSCFirmaRemotaRENTRIApi->credentials_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSCFirmaRemotaRENTRIApi->credentials_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| Identificativo delle credenziali. | 
 **certificates** | [**CredentialsCertificate**](.md)| Specifica quali certificati dalla catena devono essere restituiti. - none: nessuno - single: solo il certificato dell&#39;identità finale - chain: l&#39;intera catena dei certificati | [optional] 
 **cert_info** | **bool**| Indica se includere nella risposta anche i parametri contenenti informazioni relative al certificato. | [optional] 
 **auth_info** | **bool**| Indica se includere nella risposta anche i parametri contenenti informazioni sul meccanismo di autorizzazione supportato dalle credenziali. | [optional] 
 **lang** | **str**| Lingua prescelta per la risposta, specificata secondo RFC 5646. | [optional] 
 **client_data** | **str**| Dati arbitrari dell&#39;applicazione di firma. | [optional] 

### Return type

[**CredentialsInfoResponse**](CredentialsInfoResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Informazioni sulle credenziali. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Credenziali non trovate. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_list_get**
> CredentialsListResponse credentials_list_get(identificativo_soggetto, user_name=user_name, credential_info=credential_info, only_valid=only_valid, certificates=certificates, cert_info=cert_info, auth_info=auth_info, lang=lang, client_data=client_data)

Elenco credenziali soggetto

Ottiene l'elenco delle credenziali associate ad un soggetto.  Per ulteriori informazioni consultare la documentazione del CSC (Cloud Signature Consortium) al link: https://cloudsignatureconsortium.org/download-api-specifications/.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.credentials_list_response import CredentialsListResponse
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
    api_instance = rentri_ca.CSCFirmaRemotaRENTRIApi(api_client)
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Codice Fiscale di un Operatore iscritto.
    user_name = 'user_name_example' # str | Identificativo dell'utente (da SPID, CIE, CNS). (optional)
    credential_info = True # bool | Indica se includere nella risposta anche le informazioni relative alla chiave pubblica del certificato ed il certificato stesso, oppure la catena di certificati associata alle credenziali. (optional)
    only_valid = True # bool | Indica se includere nella risposta solo credenziali utilizzabili per creare una firma valida. (optional)
    certificates = rentri_ca.CredentialsCertificate() # CredentialsCertificate | Specifica quali certificati dalla catena devono essere restituiti. - none: nessuno - single: solo il certificato dell'identità finale - chain: l'intera catena dei certificati (optional)
    cert_info = True # bool | Indica se includere nella risposta anche i parametri contenenti informazioni relative al certificato. (optional)
    auth_info = True # bool | Indica se includere nella risposta anche i parametri contenenti informazioni sul meccanismo di autorizzazione supportato dalle credenziali. (optional)
    lang = 'lang_example' # str | Lingua prescelta per la risposta, specificata secondo RFC 5646. (optional)
    client_data = 'client_data_example' # str | Dati arbitrari dell'applicazione di firma. (optional)

    try:
        # Elenco credenziali soggetto
        api_response = api_instance.credentials_list_get(identificativo_soggetto, user_name=user_name, credential_info=credential_info, only_valid=only_valid, certificates=certificates, cert_info=cert_info, auth_info=auth_info, lang=lang, client_data=client_data)
        print("The response of CSCFirmaRemotaRENTRIApi->credentials_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSCFirmaRemotaRENTRIApi->credentials_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo_soggetto** | **str**| Codice Fiscale di un Operatore iscritto. | 
 **user_name** | **str**| Identificativo dell&#39;utente (da SPID, CIE, CNS). | [optional] 
 **credential_info** | **bool**| Indica se includere nella risposta anche le informazioni relative alla chiave pubblica del certificato ed il certificato stesso, oppure la catena di certificati associata alle credenziali. | [optional] 
 **only_valid** | **bool**| Indica se includere nella risposta solo credenziali utilizzabili per creare una firma valida. | [optional] 
 **certificates** | [**CredentialsCertificate**](.md)| Specifica quali certificati dalla catena devono essere restituiti. - none: nessuno - single: solo il certificato dell&#39;identità finale - chain: l&#39;intera catena dei certificati | [optional] 
 **cert_info** | **bool**| Indica se includere nella risposta anche i parametri contenenti informazioni relative al certificato. | [optional] 
 **auth_info** | **bool**| Indica se includere nella risposta anche i parametri contenenti informazioni sul meccanismo di autorizzazione supportato dalle credenziali. | [optional] 
 **lang** | **str**| Lingua prescelta per la risposta, specificata secondo RFC 5646. | [optional] 
 **client_data** | **str**| Dati arbitrari dell&#39;applicazione di firma. | [optional] 

### Return type

[**CredentialsListResponse**](CredentialsListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elenco delle credenziali. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Credenziali non trovate. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_post**
> CreateUpdateCredentialsResponse credentials_post(create_update_credentials_request=create_update_credentials_request)

Crea/aggiorna credenziali

Crea delle nuove credenziali associate al soggetto e al dispositivo specificati, oppure aggiorna le informazioni associate a credenziali esistenti.  Per ulteriori informazioni consultare la documentazione del CSC (Cloud Signature Consortium) al link: https://cloudsignatureconsortium.org/download-api-specifications/.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.create_update_credentials_request import CreateUpdateCredentialsRequest
from rentri_ca.models.create_update_credentials_response import CreateUpdateCredentialsResponse
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
    api_instance = rentri_ca.CSCFirmaRemotaRENTRIApi(api_client)
    create_update_credentials_request = rentri_ca.CreateUpdateCredentialsRequest() # CreateUpdateCredentialsRequest | Dati delle credenziali. (optional)

    try:
        # Crea/aggiorna credenziali
        api_response = api_instance.credentials_post(create_update_credentials_request=create_update_credentials_request)
        print("The response of CSCFirmaRemotaRENTRIApi->credentials_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSCFirmaRemotaRENTRIApi->credentials_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_credentials_request** | [**CreateUpdateCredentialsRequest**](CreateUpdateCredentialsRequest.md)| Dati delle credenziali. | [optional] 

### Return type

[**CreateUpdateCredentialsResponse**](CreateUpdateCredentialsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Identificativo delle credenziali create/aggiornate. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**422** | Registrazione del dispositivo non riuscita. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_get**
> InfoData info_get(lang=lang)

Info servizio

Restituisce informazioni sul servizio e l'elenco dei metodi API implementati.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.info_data import InfoData
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
    api_instance = rentri_ca.CSCFirmaRemotaRENTRIApi(api_client)
    lang = 'it-IT' # str | Lingua prescelta per la risposta, specificata secondo RFC 5646. (optional) (default to 'it-IT')

    try:
        # Info servizio
        api_response = api_instance.info_get(lang=lang)
        print("The response of CSCFirmaRemotaRENTRIApi->info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSCFirmaRemotaRENTRIApi->info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| Lingua prescelta per la risposta, specificata secondo RFC 5646. | [optional] [default to &#39;it-IT&#39;]

### Return type

[**InfoData**](InfoData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signatures_sign_hash_post**
> SignatureResponse signatures_sign_hash_post(signature_request=signature_request)

Firma hash

Calcola la firma di uno o più hash specificati.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.signature_request import SignatureRequest
from rentri_ca.models.signature_response import SignatureResponse
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
    api_instance = rentri_ca.CSCFirmaRemotaRENTRIApi(api_client)
    signature_request = rentri_ca.SignatureRequest() # SignatureRequest |  (optional)

    try:
        # Firma hash
        api_response = api_instance.signatures_sign_hash_post(signature_request=signature_request)
        print("The response of CSCFirmaRemotaRENTRIApi->signatures_sign_hash_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSCFirmaRemotaRENTRIApi->signatures_sign_hash_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature_request** | [**SignatureRequest**](SignatureRequest.md)|  | [optional] 

### Return type

[**SignatureResponse**](SignatureResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Firma applicata correttamente. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**422** | Problema con il SAD o durante la firma. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signatures_sign_hash_post_0**
> SignatureResponse signatures_sign_hash_post_0(signature_request=signature_request)

⚠️[DEPRECATO] - utilizzare /signatures/sign-hash - Firma hash

Calcola la firma di uno o più hash specificati.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_ca
from rentri_ca.models.signature_request import SignatureRequest
from rentri_ca.models.signature_response import SignatureResponse
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
    api_instance = rentri_ca.CSCFirmaRemotaRENTRIApi(api_client)
    signature_request = rentri_ca.SignatureRequest() # SignatureRequest |  (optional)

    try:
        # ⚠️[DEPRECATO] - utilizzare /signatures/sign-hash - Firma hash
        api_response = api_instance.signatures_sign_hash_post_0(signature_request=signature_request)
        print("The response of CSCFirmaRemotaRENTRIApi->signatures_sign_hash_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSCFirmaRemotaRENTRIApi->signatures_sign_hash_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature_request** | [**SignatureRequest**](SignatureRequest.md)|  | [optional] 

### Return type

[**SignatureResponse**](SignatureResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Firma applicata correttamente. |  -  |
**400** | Richiesta non valida. |  -  |
**403** | Operazione non consentita. |  -  |
**422** | Problema con il SAD o durante la firma. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

