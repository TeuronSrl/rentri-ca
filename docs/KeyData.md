# KeyData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**KeyStatus**](KeyStatus.md) | Stato della chiave di firma.&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;Enabled&lt;/i&gt; - Chiave abilitata ed utilizzabile per la firma.&lt;/li&gt;&lt;li&gt;&lt;i&gt;Disabled&lt;/i&gt; - Chiave disabilitata e non utilizzabile per la firma.&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**algo** | **List[str]** | Elenco degli OID degli algoritmi chiave supportati. | [optional] 
**len** | **int** | Lunghezza della chiave crittografica in bit. | [optional] 
**curve** | **str** | OID della curva ECDSA. | [optional] 

## Example

```python
from rentri_ca.models.key_data import KeyData

# TODO update the JSON string below
json = "{}"
# create an instance of KeyData from a JSON string
key_data_instance = KeyData.from_json(json)
# print the JSON string representation of the object
print KeyData.to_json()

# convert the object into a dict
key_data_dict = key_data_instance.to_dict()
# create an instance of KeyData from a dict
key_data_from_dict = KeyData.from_dict(key_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


