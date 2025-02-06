# CredentialsSito


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** |  | [optional] 
**nome** | **str** |  | [optional] 
**indirizzo** | **str** |  | [optional] 
**civico** | **str** |  | [optional] 
**comune_id** | **str** |  | [optional] 
**provincia_id** | **str** |  | [optional] 

## Example

```python
from rentri_ca.models.credentials_sito import CredentialsSito

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsSito from a JSON string
credentials_sito_instance = CredentialsSito.from_json(json)
# print the JSON string representation of the object
print CredentialsSito.to_json()

# convert the object into a dict
credentials_sito_dict = credentials_sito_instance.to_dict()
# create an instance of CredentialsSito from a dict
credentials_sito_from_dict = CredentialsSito.from_dict(credentials_sito_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


