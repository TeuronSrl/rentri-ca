# SyncDeviceInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Identificativo del dispositivo. | 
**name** | **str** | Nome. | 
**os_version** | **str** | Versione del Sistema Operativo. | 
**notification_callback_uri** | **str** | URI di callback alla quale verranno inviati in POST i dati delle notifiche RENTRI. | 
**notification_callback_parameters** | **Dict[str, str]** | Dizionario di parametri custom che verranno inviati, tra i dati delle notifiche, all&#39;URI di callback. | 
**app_info** | [**AppInfo**](AppInfo.md) | Informazioni sulla App installata. | [optional] 

## Example

```python
from rentri_ca.models.sync_device_info_request import SyncDeviceInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncDeviceInfoRequest from a JSON string
sync_device_info_request_instance = SyncDeviceInfoRequest.from_json(json)
# print the JSON string representation of the object
print SyncDeviceInfoRequest.to_json()

# convert the object into a dict
sync_device_info_request_dict = sync_device_info_request_instance.to_dict()
# create an instance of SyncDeviceInfoRequest from a dict
sync_device_info_request_from_dict = SyncDeviceInfoRequest.from_dict(sync_device_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


