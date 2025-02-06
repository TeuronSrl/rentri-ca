# CredentialsListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_ids** | **List[str]** | Uno o più identificativi delle credenziali associate al dispositivo. | [optional] 
**credentials_infos** | [**List[CredentialsInfo]**](CredentialsInfo.md) | Specifiche relative a ciascun identificativo delle credenziali. | [optional] 
**only_valid** | **bool** | Indica se sono state incluse nella risposta solo credenziali utilizzabili per creare una firma valida. | [optional] 

## Example

```python
from rentri_ca.models.credentials_list_response import CredentialsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsListResponse from a JSON string
credentials_list_response_instance = CredentialsListResponse.from_json(json)
# print the JSON string representation of the object
print CredentialsListResponse.to_json()

# convert the object into a dict
credentials_list_response_dict = credentials_list_response_instance.to_dict()
# create an instance of CredentialsListResponse from a dict
credentials_list_response_from_dict = CredentialsListResponse.from_dict(credentials_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


