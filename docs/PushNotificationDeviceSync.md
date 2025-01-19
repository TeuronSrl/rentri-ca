# PushNotificationDeviceSync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PushNotificationType**](PushNotificationType.md) |  | [optional] [readonly] 
**device** | [**PushNotificationDevice**](PushNotificationDevice.md) |  | 

## Example

```python
from rentri_ca.models.push_notification_device_sync import PushNotificationDeviceSync

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotificationDeviceSync from a JSON string
push_notification_device_sync_instance = PushNotificationDeviceSync.from_json(json)
# print the JSON string representation of the object
print(PushNotificationDeviceSync.to_json())

# convert the object into a dict
push_notification_device_sync_dict = push_notification_device_sync_instance.to_dict()
# create an instance of PushNotificationDeviceSync from a dict
push_notification_device_sync_from_dict = PushNotificationDeviceSync.from_dict(push_notification_device_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


