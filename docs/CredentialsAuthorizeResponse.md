# CredentialsAuthorizeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sad** | **str** | SAD (Signature Activation Data), solo nel caso in cui la richiesta di autorizzazione abbia avuto successo. | [optional] 
**expires_in** | **int** | La durata del SAD espressa in secondi (default 3600), solo nel caso in cui l&#39;autorizzazione sia stata concessa. | [optional] 
**handle** | **str** | Handle del SAD per verificare lo stato di autorizzazione della richiesta. | [optional] 

## Example

```python
from rentri_ca.models.credentials_authorize_response import CredentialsAuthorizeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsAuthorizeResponse from a JSON string
credentials_authorize_response_instance = CredentialsAuthorizeResponse.from_json(json)
# print the JSON string representation of the object
print CredentialsAuthorizeResponse.to_json()

# convert the object into a dict
credentials_authorize_response_dict = credentials_authorize_response_instance.to_dict()
# create an instance of CredentialsAuthorizeResponse from a dict
credentials_authorize_response_from_dict = CredentialsAuthorizeResponse.from_dict(credentials_authorize_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


