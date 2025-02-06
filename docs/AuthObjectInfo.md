# AuthObjectInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**generator** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from rentri_ca.models.auth_object_info import AuthObjectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AuthObjectInfo from a JSON string
auth_object_info_instance = AuthObjectInfo.from_json(json)
# print the JSON string representation of the object
print AuthObjectInfo.to_json()

# convert the object into a dict
auth_object_info_dict = auth_object_info_instance.to_dict()
# create an instance of AuthObjectInfo from a dict
auth_object_info_from_dict = AuthObjectInfo.from_dict(auth_object_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


