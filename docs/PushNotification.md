# PushNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PushNotificationType**](PushNotificationType.md) |  | [optional] [readonly] 
**credentials_id** | **str** |  | [optional] 
**device** | [**PushNotificationDevice**](PushNotificationDevice.md) |  | 
**rentri_push_notification** | [**RentriPushNotification**](RentriPushNotification.md) |  | 

## Example

```python
from rentri_ca.models.push_notification import PushNotification

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotification from a JSON string
push_notification_instance = PushNotification.from_json(json)
# print the JSON string representation of the object
print(PushNotification.to_json())

# convert the object into a dict
push_notification_dict = push_notification_instance.to_dict()
# create an instance of PushNotification from a dict
push_notification_from_dict = PushNotification.from_dict(push_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


