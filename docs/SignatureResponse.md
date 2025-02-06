# SignatureResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signatures** | **List[str]** | Lista delle firme applicate. | [optional] 

## Example

```python
from rentri_ca.models.signature_response import SignatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureResponse from a JSON string
signature_response_instance = SignatureResponse.from_json(json)
# print the JSON string representation of the object
print SignatureResponse.to_json()

# convert the object into a dict
signature_response_dict = signature_response_instance.to_dict()
# create an instance of SignatureResponse from a dict
signature_response_from_dict = SignatureResponse.from_dict(signature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


