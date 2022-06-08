# AlertQueryModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource_uid** | **str** | Grafana data source unique identifier; it should be &#39;-100&#39; for a Server Side Expression operation. | [optional] 
**model** | **object** | JSON is the raw JSON query and includes the above properties as well as custom properties. | [optional] 
**query_type** | **str** | QueryType is an optional identifier for the type of query. It can be used to distinguish different types of queries. | [optional] 
**ref_id** | **str** | RefID is the unique identifier of the query, set by the frontend call. | [optional] 
**relative_time_range** | [**RelativeTimeRangeModel**](RelativeTimeRangeModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


