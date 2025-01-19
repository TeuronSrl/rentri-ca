# SignAlgorithms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algos** | **List[str]** | Elenco degli algoritmi di firma supportati dal servizio. | [optional] 
**algo_params** | **List[str]** | Elenco degli eventuali parametri di firma. | [optional] 

## Example

```python
from rentri_ca.models.sign_algorithms import SignAlgorithms

# TODO update the JSON string below
json = "{}"
# create an instance of SignAlgorithms from a JSON string
sign_algorithms_instance = SignAlgorithms.from_json(json)
# print the JSON string representation of the object
print(SignAlgorithms.to_json())

# convert the object into a dict
sign_algorithms_dict = sign_algorithms_instance.to_dict()
# create an instance of SignAlgorithms from a dict
sign_algorithms_from_dict = SignAlgorithms.from_dict(sign_algorithms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


