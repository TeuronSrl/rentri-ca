# CredentialsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_id** | **str** | Identificativo delle credenziali. | [optional] 
**description** | **str** | Descrizione delle credenziali. | [optional] 
**signature_qualifier** | [**SignatureQualifier**](SignatureQualifier.md) | Identificativo che qualifica il tipo di firma per cui sono adatte le credenziali. | [optional] 
**key** | [**KeyData**](KeyData.md) | Informazioni sulla chiave di firma. | [optional] 
**cert** | [**CertData**](CertData.md) | Informazioni sul certificato. | [optional] 
**auth** | [**AuthData**](AuthData.md) | Informazioni sulla modalità di autorizzazione. | [optional] 
**scal** | **str** | Indica se il servizio di autorizzazione genera un Signature Activation Data (SAD) che contiene un collegamento con i codici hash da firmare. 1 - non collegato (default) 2 - collegato | [optional] 
**multisign** | **int** | Numero massimo di firme che possono essere create con queste credenziali con una singola richiesta. | [optional] 
**lang** | **str** | Lingua prescelta per la risposta, specificata secondo RFC 5646. | [optional] 

## Example

```python
from rentri_ca.models.credentials_info import CredentialsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsInfo from a JSON string
credentials_info_instance = CredentialsInfo.from_json(json)
# print the JSON string representation of the object
print(CredentialsInfo.to_json())

# convert the object into a dict
credentials_info_dict = credentials_info_instance.to_dict()
# create an instance of CredentialsInfo from a dict
credentials_info_from_dict = CredentialsInfo.from_dict(credentials_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


