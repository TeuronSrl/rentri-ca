# CredentialsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PushNotificationType**](PushNotificationType.md) |  | [optional] [readonly] 
**is_credentials_deletion** | **bool** |  | [optional] 
**credentials_id** | **str** |  | [optional] 
**device** | [**PushNotificationDevice**](PushNotificationDevice.md) |  | 
**identificativo_soggetto** | **str** |  | 
**user_name** | **str** |  | [optional] 
**rentri_push_notification** | [**RentriPushNotification**](RentriPushNotification.md) |  | 

## Example

```python
from rentri_ca.models.credentials_post_request import CredentialsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsPostRequest from a JSON string
credentials_post_request_instance = CredentialsPostRequest.from_json(json)
# print the JSON string representation of the object
print CredentialsPostRequest.to_json()

# convert the object into a dict
credentials_post_request_dict = credentials_post_request_instance.to_dict()
# create an instance of CredentialsPostRequest from a dict
credentials_post_request_from_dict = CredentialsPostRequest.from_dict(credentials_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


