# SignatureFormats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formats** | **List[str]** | Elenco dei formati di firma supportati dal servizio. | [optional] 
**envelope_properties** | **List[List[str]]** | Elenco delle proprietà riguardanti la busta firmata. | [optional] 

## Example

```python
from rentri_ca.models.signature_formats import SignatureFormats

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureFormats from a JSON string
signature_formats_instance = SignatureFormats.from_json(json)
# print the JSON string representation of the object
print SignatureFormats.to_json()

# convert the object into a dict
signature_formats_dict = signature_formats_instance.to_dict()
# create an instance of SignatureFormats from a dict
signature_formats_from_dict = SignatureFormats.from_dict(signature_formats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


