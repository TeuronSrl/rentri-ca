# CreateUpdateCredentialsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_id** | **str** | Identificativo delle credenziali. | [optional] 
**pin** | **str** | PIN. | [optional] 

## Example

```python
from rentri_ca.models.create_update_credentials_response import CreateUpdateCredentialsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdateCredentialsResponse from a JSON string
create_update_credentials_response_instance = CreateUpdateCredentialsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateUpdateCredentialsResponse.to_json())

# convert the object into a dict
create_update_credentials_response_dict = create_update_credentials_response_instance.to_dict()
# create an instance of CreateUpdateCredentialsResponse from a dict
create_update_credentials_response_from_dict = CreateUpdateCredentialsResponse.from_dict(create_update_credentials_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


