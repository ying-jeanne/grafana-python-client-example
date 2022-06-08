# MetricRequestModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debug** | **bool** |  | [optional] 
**_from** | **str** | From Start time in epoch timestamps in milliseconds or relative using Grafana time units. | 
**queries** | [**list[JsonModel]**](JsonModel.md) | queries.refId – Specifies an identifier of the query. Is optional and default to “A”. queries.datasourceId – Specifies the data source to be queried. Each query in the request must have an unique datasourceId. queries.maxDataPoints - Species maximum amount of data points that dashboard panel can render. Is optional and default to 100. queries.intervalMs - Specifies the time interval in milliseconds of time series. Is optional and defaults to 1000. | 
**to** | **str** | To End time in epoch timestamps in milliseconds or relative using Grafana time units. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


