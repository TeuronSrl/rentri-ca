# CredentialsModel

Dati delle credenziali.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Identificativo delle credenziali. | [optional] 
**identificativo** | **str** | Identificativo del soggetto associato alle credenziali. | [optional] 
**identificativo_altro** | **str** | Identificativo alternativo del soggetto associato alle credenziali. | [optional] 
**user_name** | **str** | Identificativo dell&#39;utente (da SPID, CIE, CNS). | [optional] 
**ultimo_accesso** | **datetime** | Data dell&#39;ultimo accesso effettuato (formato ISO 8601 UTC). | [optional] 
**data_eliminazione** | **datetime** | Data di eliminazione (formato ISO 8601 UTC). | [optional] 
**data_scadenza_richiesta_pin_reset** | **datetime** | Data di scadenza della richiesta di reset del PIN (formato ISO 8601 UTC). | [optional] 
**stato** | [**Stato**](Stato.md) | Stato. | [optional] 
**siti** | **List[str]** | Elenco delle unità locali sulle quali è possibile operare. | [optional] 
**device_identifier** | **str** | Identificativo del dispositivo. | [optional] 
**device_is_banned** | **bool** | Indica se il device è stato bloccato. | [optional] 

## Example

```python
from rentri_ca.models.credentials_model import CredentialsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsModel from a JSON string
credentials_model_instance = CredentialsModel.from_json(json)
# print the JSON string representation of the object
print(CredentialsModel.to_json())

# convert the object into a dict
credentials_model_dict = credentials_model_instance.to_dict()
# create an instance of CredentialsModel from a dict
credentials_model_from_dict = CredentialsModel.from_dict(credentials_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


