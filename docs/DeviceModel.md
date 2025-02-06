# DeviceModel

Dati di base del dispositivo e informazioni sulla registrazione al servizio di smistamento delle notifiche RENTRI.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Identificativo del dispositivo. | [optional] 
**name** | **str** | Nome. | [optional] 
**model** | **str** | Modello. | [optional] 
**manufacturer** | **str** | Produttore. | [optional] 
**os_version** | **str** | Versione del Sistema Operativo. | [optional] 
**form_factor** | **str** | Formato. | [optional] 
**type** | [**DeviceType**](DeviceType.md) | Tipo di dispositivo (fisico, virtuale).&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;Physical&lt;/i&gt; - Dispositivo fisico&lt;/li&gt;&lt;li&gt;&lt;i&gt;Virtual&lt;/i&gt; - Dispositivo virtuale&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**platform** | **str** | Piattaforma o Sistema Operativo (Android, iOS, Windows). | [optional] 
**data_registrazione** | **datetime** | Data di registrazione (formato ISO 8601 UTC). | [optional] 
**is_banned** | **bool** | Indica se il dispositivo è stato bloccato. | [optional] 
**stato** | [**Stato**](Stato.md) | Stato. | [optional] 
**app_name** | **str** | Nome dell&#39;app installata. | [optional] 
**app_package_name** | **str** | Nome del package dell&#39;app installata. | [optional] 
**app_version** | **str** | Versione dell&#39;app installata. | [optional] 
**app_build** | **str** | Numero di build dell&#39;app installata. | [optional] 
**notification_callback_uri** | **str** | URI di callback alla quale verranno inviati in POST i dati delle notifiche RENTRI. | [optional] 
**notification_callback_parameters** | **Dict[str, str]** | Dizionario di parametri custom che verranno inviati, tra i dati delle notifiche, all&#39;URI di callback. | [optional] 
**siti** | **List[str]** | Elenco delle unità locali abbinate. | [optional] 

## Example

```python
from rentri_ca.models.device_model import DeviceModel

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceModel from a JSON string
device_model_instance = DeviceModel.from_json(json)
# print the JSON string representation of the object
print DeviceModel.to_json()

# convert the object into a dict
device_model_dict = device_model_instance.to_dict()
# create an instance of DeviceModel from a dict
device_model_from_dict = DeviceModel.from_dict(device_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


