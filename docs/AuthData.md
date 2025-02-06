# AuthData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**AuthMode**](AuthMode.md) | Modalità di autorizzazione.&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;Implicit&lt;/i&gt; - Il processo autorizzativo è gestito dal servizio. I fattori autenticativi sono gestiti dal servizio interagendo direttamente con l&#39;utente, e non con l&#39;applicazione di firma.&lt;/li&gt;&lt;li&gt;&lt;i&gt;Explicit&lt;/i&gt; - Il processo autorizzativo è gestito dall&#39;applicazione di firma, che gestisce i fattori di autenticazione come PIN o One-Time Password (OTP).&lt;/li&gt;&lt;li&gt;&lt;i&gt;Oauth2Code&lt;/i&gt; - Il processo autorizzativo è gestito da un servizio di autenticazione utilizzando OAuth 2.0.&lt;/li&gt;&lt;li&gt;&lt;i&gt;Oauth2Token&lt;/i&gt; - Il processo autorizzativo è gestito da un servizio di autenticazione utilizzando OAuth 2.0.&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**expression** | **str** |  | [optional] 
**objects** | [**List[AuthObjectInfo]**](AuthObjectInfo.md) | Informazioni sui metodi di autenticazione disponibili. | [optional] 

## Example

```python
from rentri_ca.models.auth_data import AuthData

# TODO update the JSON string below
json = "{}"
# create an instance of AuthData from a JSON string
auth_data_instance = AuthData.from_json(json)
# print the JSON string representation of the object
print AuthData.to_json()

# convert the object into a dict
auth_data_dict = auth_data_instance.to_dict()
# create an instance of AuthData from a dict
auth_data_from_dict = AuthData.from_dict(auth_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


