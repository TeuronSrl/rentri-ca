# PushNotificationDeviceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PushNotificationType**](PushNotificationType.md) |  | [optional] [readonly] 
**is_credentials_deletion** | **bool** |  | [optional] 
**credentials_id** | **str** |  | [optional] 
**device** | [**PushNotificationDevice**](PushNotificationDevice.md) |  | 
**identificativo_soggetto** | **str** |  | 
**user_name** | **str** |  | [optional] 

## Example

```python
from rentri_ca.models.push_notification_device_info import PushNotificationDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotificationDeviceInfo from a JSON string
push_notification_device_info_instance = PushNotificationDeviceInfo.from_json(json)
# print the JSON string representation of the object
print(PushNotificationDeviceInfo.to_json())

# convert the object into a dict
push_notification_device_info_dict = push_notification_device_info_instance.to_dict()
# create an instance of PushNotificationDeviceInfo from a dict
push_notification_device_info_from_dict = PushNotificationDeviceInfo.from_dict(push_notification_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


