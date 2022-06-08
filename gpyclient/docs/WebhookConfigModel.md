# WebhookConfigModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_config** | [**HTTPClientConfigModel**](HTTPClientConfigModel.md) |  | [optional] 
**max_alerts** | **int** | MaxAlerts is the maximum number of alerts to be sent per webhook message. Alerts exceeding this threshold will be truncated. Setting this to 0 allows an unlimited number of alerts. | [optional] 
**send_resolved** | **bool** |  | [optional] 
**url** | [**URLModel**](URLModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


