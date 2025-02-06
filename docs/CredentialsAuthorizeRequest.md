# CredentialsAuthorizeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_id** | **str** | Identificativo delle credenziali. | 
**num_signatures** | **int** |  | 
**hashes** | **List[str]** | Elenco dei codici hash da firmare in formato base 64. Attualmente è consentito l&#39;invio di un solo codice hash. | 
**hash_algo** | **str** | OID dell&#39;algoritmo utilizzato per calcolare l&#39;hash fisso a 2.16.840.1.101.3.4.2.1 (SHA256) | 
**description** | **str** | Descrizione della transazione di autenticazione. | [optional] 
**auth_data** | [**List[AuthObjectData]**](AuthObjectData.md) | Informazioni sui metodi di autenticazione disponibili. | 
**client_data** | **str** | Dati arbitrari dell&#39;applicazione di firma. | [optional] 

## Example

```python
from rentri_ca.models.credentials_authorize_request import CredentialsAuthorizeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsAuthorizeRequest from a JSON string
credentials_authorize_request_instance = CredentialsAuthorizeRequest.from_json(json)
# print the JSON string representation of the object
print CredentialsAuthorizeRequest.to_json()

# convert the object into a dict
credentials_authorize_request_dict = credentials_authorize_request_instance.to_dict()
# create an instance of CredentialsAuthorizeRequest from a dict
credentials_authorize_request_from_dict = CredentialsAuthorizeRequest.from_dict(credentials_authorize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


