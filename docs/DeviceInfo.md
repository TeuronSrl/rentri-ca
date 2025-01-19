# DeviceInfo

Informazioni sul dispositivo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Identificativo del dispositivo. | 
**model** | **str** | Modello del dispositivo. | 
**manufacturer** | **str** | Produttore del dispositivo. | 
**name** | **str** | Nome del dispositivo. | 
**os_version** | **str** | Versione del Sistema Operativo del dispositivo. | 
**form_factor** | **str** | Stile del dispositivo. | 
**type** | [**DeviceType**](DeviceType.md) | Tipo di dispositivo.&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;Physical&lt;/i&gt; - Dispositivo fisico&lt;/li&gt;&lt;li&gt;&lt;i&gt;Virtual&lt;/i&gt; - Dispositivo virtuale&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | 
**platform** | **str** | Piattaforma del dispositivo. | 
**notification_callback_uri** | **str** | URI di callback alla quale verranno inviati in POST i dati delle notifiche RENTRI. | 
**notification_callback_parameters** | **Dict[str, str]** | Dizionario di parametri custom che verranno inviati, tra i dati delle notifiche, all&#39;URI di callback. | 

## Example

```python
from rentri_ca.models.device_info import DeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInfo from a JSON string
device_info_instance = DeviceInfo.from_json(json)
# print the JSON string representation of the object
print(DeviceInfo.to_json())

# convert the object into a dict
device_info_dict = device_info_instance.to_dict()
# create an instance of DeviceInfo from a dict
device_info_from_dict = DeviceInfo.from_dict(device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


