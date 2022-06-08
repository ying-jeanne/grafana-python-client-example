# FrameMetaModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Channel is the path to a stream in grafana live that has real-time updates for this data. | [optional] 
**custom** | **object** | Custom datasource specific values. | [optional] 
**executed_query_string** | **str** | ExecutedQueryString is the raw query sent to the underlying system. All macros and templating have been applied.  When metadata contains this value, it will be shown in the query inspector. | [optional] 
**notices** | [**list[NoticeModel]**](NoticeModel.md) | Notices provide additional information about the data in the Frame that Grafana can display to the user in the user interface. | [optional] 
**path** | **str** | Path is a browsable path on the datasource. | [optional] 
**path_separator** | **str** | PathSeparator defines the separator pattern to decode a hiearchy. The default separator is &#39;/&#39;. | [optional] 
**preferred_visualisation_type** | [**VisTypeModel**](VisTypeModel.md) |  | [optional] 
**stats** | [**list[QueryStatModel]**](QueryStatModel.md) | Stats is an array of query result statistics. | [optional] 
**type** | [**FrameTypeModel**](FrameTypeModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


