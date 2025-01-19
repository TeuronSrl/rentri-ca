# CertData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**CertStatus**](CertStatus.md) | Stato del certificato.&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;Valid&lt;/i&gt; - Valido.&lt;/li&gt;&lt;li&gt;&lt;i&gt;Expired&lt;/i&gt; - Scaduto.&lt;/li&gt;&lt;li&gt;&lt;i&gt;Revoked&lt;/i&gt; - Revocato.&lt;/li&gt;&lt;li&gt;&lt;i&gt;Suspended&lt;/i&gt; - Sospeso.&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**certificates** | **List[str]** | Codifica base 64 dei certificati X.509. Se il parametro certificates è \&quot;chain\&quot;, è presente l&#39;intera catena di certificati con il certificato dell&#39;ente finale nella prima posizione dell&#39;elenco. Se il parametro certificates è “single”, è presente solo il certificato dell&#39;entità finale. Se il parametro certificates è \&quot;none\&quot;, non è presente alcun certificato. | [optional] 
**issuer_dn** | **str** | Emittente del certificato. | 
**serial_number** | **str** | Serial number del certificato. | 
**subject_dn** | **str** | Soggetto del certificato. | 
**valid_from** | **datetime** | Data di inizio validità del certificato (formato ISO 8601 UTC). | 
**valid_to** | **datetime** | Data di fine validità del certificato (formato ISO 8601 UTC). | 

## Example

```python
from rentri_ca.models.cert_data import CertData

# TODO update the JSON string below
json = "{}"
# create an instance of CertData from a JSON string
cert_data_instance = CertData.from_json(json)
# print the JSON string representation of the object
print(CertData.to_json())

# convert the object into a dict
cert_data_dict = cert_data_instance.to_dict()
# create an instance of CertData from a dict
cert_data_from_dict = CertData.from_dict(cert_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


