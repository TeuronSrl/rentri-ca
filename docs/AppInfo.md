# AppInfo

Informazioni sulla App.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nome dell&#39;applicazione. | 
**package_name** | **str** | Nome del package o identificativo dell&#39;applicazione. | 
**version** | **str** | Versione dell&#39;applicazione. | 
**build** | **str** | Numero della build della versione dell&#39;applicazione. | 

## Example

```python
from rentri_ca.models.app_info import AppInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppInfo from a JSON string
app_info_instance = AppInfo.from_json(json)
# print the JSON string representation of the object
print(AppInfo.to_json())

# convert the object into a dict
app_info_dict = app_info_instance.to_dict()
# create an instance of AppInfo from a dict
app_info_from_dict = AppInfo.from_dict(app_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


