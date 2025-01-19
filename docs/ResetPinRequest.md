# ResetPinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token della richiesta di reset. | 
**new_pin** | **str** | Nuovo PIN. | [optional] 
**abort** | **bool** | Annullamento della procedura. | [optional] 

## Example

```python
from rentri_ca.models.reset_pin_request import ResetPinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResetPinRequest from a JSON string
reset_pin_request_instance = ResetPinRequest.from_json(json)
# print the JSON string representation of the object
print(ResetPinRequest.to_json())

# convert the object into a dict
reset_pin_request_dict = reset_pin_request_instance.to_dict()
# create an instance of ResetPinRequest from a dict
reset_pin_request_from_dict = ResetPinRequest.from_dict(reset_pin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


