# CreateUpdateCredentialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo_soggetto** | **str** | Codice Fiscale di un Operatore iscritto. | 
**num_iscr_sito** | **str** | Numero iscrizione unità locale | [optional] 
**identificativo** | **str** | Identificativo del soggetto associato alle credenziali. | 
**identificativo_altro** | **str** | Identificativo alternativo del soggetto associato alle credenziali. | [optional] 
**user_name** | **str** | Identificativo dell&#39;utente (da SPID, CIE, CNS). | [optional] 
**device_info** | [**DeviceInfo**](DeviceInfo.md) | Informazioni sul dispositivo. | 
**app_info** | [**AppInfo**](AppInfo.md) | Informazioni sulla App. | 

## Example

```python
from rentri_ca.models.create_update_credentials_request import CreateUpdateCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdateCredentialsRequest from a JSON string
create_update_credentials_request_instance = CreateUpdateCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUpdateCredentialsRequest.to_json())

# convert the object into a dict
create_update_credentials_request_dict = create_update_credentials_request_instance.to_dict()
# create an instance of CreateUpdateCredentialsRequest from a dict
create_update_credentials_request_from_dict = CreateUpdateCredentialsRequest.from_dict(create_update_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


