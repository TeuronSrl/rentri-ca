# SignatureRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_id** | **str** | Identificativo delle credenziali di firma. | 
**sad** | **str** | SAD (Signature Activation Data). | 
**hashes** | **List[str]** | Elenco dei codici hash da firmare in formato base 64. Attualmente è consentito l&#39;invio di un solo codice hash. | 
**hash_algo** | **str** | OID dell&#39;algoritmo utilizzato per calcolare l&#39;hash. Questo parametro deve essere omesso o ignorato se l&#39;algoritmo hash è implicitamente specificato dal parametro SignAlgo. | [optional] 
**sign_algo** | **str** | OID dell&#39;algoritmo da utilizzare per la firma. Deve essere uno dei valori consentiti dalle credenziali. | 
**sign_algo_params** | **str** | I parametri per l&#39;algoritmo di firma, se richiesti dall&#39;algoritmo di firma. | [optional] 
**client_data** | **str** | Dati arbitrari dell&#39;applicazione di firma. | [optional] 

## Example

```python
from rentri_ca.models.signature_request import SignatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureRequest from a JSON string
signature_request_instance = SignatureRequest.from_json(json)
# print the JSON string representation of the object
print SignatureRequest.to_json()

# convert the object into a dict
signature_request_dict = signature_request_instance.to_dict()
# create an instance of SignatureRequest from a dict
signature_request_from_dict = SignatureRequest.from_dict(signature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


