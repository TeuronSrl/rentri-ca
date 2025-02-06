# InfoData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specs** | **str** | Versione della specifica CSC implementata. | [optional] 
**name** | **str** | Nome commerciale del servizio. | [optional] 
**logo** | **str** | L&#39;URI del file immagine del logo del servizio. | [optional] 
**region** | **str** | Codice ISO 3166-1 del paese in cui il fornitore di servizi è stabilito. | [optional] 
**lang** | **str** | Lingua utilizzata per la risposta, specificata secondo RFC 5646. | [optional] 
**description** | **str** | Descrizione del servizio. | [optional] 
**auth_type** | **List[str]** | Metodi di autenticazione supportati dal servizio. | [optional] 
**oauth2** | **str** | URI di base del server di autorizzazione OAuth 2.0. | [optional] 
**methods** | **List[str]** | Elenco dei nomi di tutti i metodi API implementati dal servizio. | [optional] 
**sign_algorithms** | [**SignAlgorithms**](SignAlgorithms.md) | Algoritmi di firma supportati dal servizio. | [optional] 
**signature_formats** | [**SignatureFormats**](SignatureFormats.md) | Formati di firma supportati dal servizio. | [optional] 
**conformance_levels** | **List[str]** | Elenco dei livelli di conformità della firma supportati dal servizio. | [optional] 

## Example

```python
from rentri_ca.models.info_data import InfoData

# TODO update the JSON string below
json = "{}"
# create an instance of InfoData from a JSON string
info_data_instance = InfoData.from_json(json)
# print the JSON string representation of the object
print InfoData.to_json()

# convert the object into a dict
info_data_dict = info_data_instance.to_dict()
# create an instance of InfoData from a dict
info_data_from_dict = InfoData.from_dict(info_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


