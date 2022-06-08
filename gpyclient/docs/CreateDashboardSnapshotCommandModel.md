# CreateDashboardSnapshotCommandModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**DashboardSnapshotModel**](DashboardSnapshotModel.md) |  | [optional] 
**dashboard** | [**DashboardModel**](DashboardModel.md) |  | 
**delete_key** | **str** | Unique key used to delete the snapshot. It is different from the &#x60;key&#x60; so that only the creator can delete the snapshot. Required if &#x60;external&#x60; is &#x60;true&#x60;. | [optional] 
**expires** | **int** | When the snapshot should expire in seconds in seconds. Default is never to expire. | [optional] [default to 0]
**external** | **bool** | these are passed when storing an external snapshot ref Save the snapshot on an external server rather than locally. | [optional] [default to False]
**key** | **str** | Define the unique key. Required if &#x60;external&#x60; is &#x60;true&#x60;. | [optional] 
**name** | **str** | Snapshot name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


