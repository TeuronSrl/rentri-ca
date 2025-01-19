# ChangePinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_pin** | **str** | PIN corrente. | 
**new_pin** | **str** | Nuovo PIN. | 

## Example

```python
from rentri_ca.models.change_pin_request import ChangePinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePinRequest from a JSON string
change_pin_request_instance = ChangePinRequest.from_json(json)
# print the JSON string representation of the object
print(ChangePinRequest.to_json())

# convert the object into a dict
change_pin_request_dict = change_pin_request_instance.to_dict()
# create an instance of ChangePinRequest from a dict
change_pin_request_from_dict = ChangePinRequest.from_dict(change_pin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


