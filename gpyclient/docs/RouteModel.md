# RouteModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_continue** | **bool** |  | [optional] 
**group_by** | **list[str]** |  | [optional] 
**group_interval** | [**DurationModel**](DurationModel.md) |  | [optional] 
**group_wait** | [**DurationModel**](DurationModel.md) |  | [optional] 
**match** | **dict(str, str)** | Deprecated. Remove before v1.0 release. | [optional] 
**match_re** | [**MatchRegexpsModel**](MatchRegexpsModel.md) |  | [optional] 
**matchers** | [**MatchersModel**](MatchersModel.md) |  | [optional] 
**mute_time_intervals** | **list[str]** |  | [optional] 
**object_matchers** | [**ObjectMatchersModel**](ObjectMatchersModel.md) |  | [optional] 
**provenance** | [**ProvenanceModel**](ProvenanceModel.md) |  | [optional] 
**receiver** | **str** |  | [optional] 
**repeat_interval** | [**DurationModel**](DurationModel.md) |  | [optional] 
**routes** | [**list[RouteModel]**](RouteModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


