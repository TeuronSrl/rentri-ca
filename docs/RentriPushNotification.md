# RentriPushNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**handle** | **str** |  | [optional] 
**otp** | **str** |  | [optional] 
**credentials_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**body** | **str** |  | [optional] 

## Example

```python
from rentri_ca.models.rentri_push_notification import RentriPushNotification

# TODO update the JSON string below
json = "{}"
# create an instance of RentriPushNotification from a JSON string
rentri_push_notification_instance = RentriPushNotification.from_json(json)
# print the JSON string representation of the object
print RentriPushNotification.to_json()

# convert the object into a dict
rentri_push_notification_dict = rentri_push_notification_instance.to_dict()
# create an instance of RentriPushNotification from a dict
rentri_push_notification_from_dict = RentriPushNotification.from_dict(rentri_push_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


