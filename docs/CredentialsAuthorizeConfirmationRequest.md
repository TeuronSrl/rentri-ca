# CredentialsAuthorizeConfirmationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_id** | **str** | Identificativo delle credenziali. | 
**handle** | **str** | Handle del SAD da autorizzare. | 
**otp** | **str** | OTP ricevuto con la notifica. | 
**allowed** | **bool** | Consenso. | 
**pin** | **str** | PIN delle credenziali. | 

## Example

```python
from rentri_ca.models.credentials_authorize_confirmation_request import CredentialsAuthorizeConfirmationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsAuthorizeConfirmationRequest from a JSON string
credentials_authorize_confirmation_request_instance = CredentialsAuthorizeConfirmationRequest.from_json(json)
# print the JSON string representation of the object
print CredentialsAuthorizeConfirmationRequest.to_json()

# convert the object into a dict
credentials_authorize_confirmation_request_dict = credentials_authorize_confirmation_request_instance.to_dict()
# create an instance of CredentialsAuthorizeConfirmationRequest from a dict
credentials_authorize_confirmation_request_from_dict = CredentialsAuthorizeConfirmationRequest.from_dict(credentials_authorize_confirmation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


