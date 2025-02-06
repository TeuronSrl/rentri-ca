# PushNotificationDevice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**notification_callback_uri** | **str** |  | 
**notification_callback_parameters** | **Dict[str, str]** |  | 

## Example

```python
from rentri_ca.models.push_notification_device import PushNotificationDevice

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotificationDevice from a JSON string
push_notification_device_instance = PushNotificationDevice.from_json(json)
# print the JSON string representation of the object
print PushNotificationDevice.to_json()

# convert the object into a dict
push_notification_device_dict = push_notification_device_instance.to_dict()
# create an instance of PushNotificationDevice from a dict
push_notification_device_from_dict = PushNotificationDevice.from_dict(push_notification_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


