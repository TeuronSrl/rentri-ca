# CertificateModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificato** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**data_rilascio** | **datetime** | Formato ISO 8601 UTC | [optional] 
**data_scadenza** | **datetime** | Formato ISO 8601 UTC | [optional] 

## Example

```python
from rentri_ca.models.certificate_model import CertificateModel

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateModel from a JSON string
certificate_model_instance = CertificateModel.from_json(json)
# print the JSON string representation of the object
print CertificateModel.to_json()

# convert the object into a dict
certificate_model_dict = certificate_model_instance.to_dict()
# create an instance of CertificateModel from a dict
certificate_model_from_dict = CertificateModel.from_dict(certificate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


