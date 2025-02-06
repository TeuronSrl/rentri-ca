# BoardingAccessResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo_soggetto** | **str** | Identificativo del soggetto. | [optional] 
**denominazione_soggetto** | **str** | Denominazione del soggetto. | [optional] 
**num_iscr_operatore** | **str** | Numero di iscrizione dell&#39;operatore. | [optional] 
**num_iscr_sito** | **str** | Numero di iscrizione del sito. | [optional] 
**nome_sito** | **str** | Nome del sito. | [optional] 

## Example

```python
from rentri_ca.models.boarding_access_response import BoardingAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BoardingAccessResponse from a JSON string
boarding_access_response_instance = BoardingAccessResponse.from_json(json)
# print the JSON string representation of the object
print BoardingAccessResponse.to_json()

# convert the object into a dict
boarding_access_response_dict = boarding_access_response_instance.to_dict()
# create an instance of BoardingAccessResponse from a dict
boarding_access_response_from_dict = BoardingAccessResponse.from_dict(boarding_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


