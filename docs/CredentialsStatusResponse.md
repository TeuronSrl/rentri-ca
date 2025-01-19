# CredentialsStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Identificativo delle credenziali. | [optional] 
**identificativo** | **str** | Identificativo del soggetto associato alle credenziali. | [optional] 
**identificativo_altro** | **str** | Identificativo alternativo del soggetto associato alle credenziali. | [optional] 
**user_name** | **str** | Identificativo dell&#39;utente (da SPID, CIE, CNS). | [optional] 
**pin** | **str** | PIN. | [optional] 
**stato** | [**Stato**](Stato.md) | Stato. | [optional] 
**siti** | [**List[CredentialsSito]**](CredentialsSito.md) | Elenco delle unità locali sulle quali è possibile operare. | [optional] 
**is_abbinato_solo_soggetto** | **bool** | Indica se le credenziali sono abbinate direttamente al soggetto. | [optional] 

## Example

```python
from rentri_ca.models.credentials_status_response import CredentialsStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsStatusResponse from a JSON string
credentials_status_response_instance = CredentialsStatusResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialsStatusResponse.to_json())

# convert the object into a dict
credentials_status_response_dict = credentials_status_response_instance.to_dict()
# create an instance of CredentialsStatusResponse from a dict
credentials_status_response_from_dict = CredentialsStatusResponse.from_dict(credentials_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


