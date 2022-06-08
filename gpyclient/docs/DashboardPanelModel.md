# DashboardPanelModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | [**DashboardPanelDatasourceModel**](DashboardPanelDatasourceModel.md) |  | [optional] 
**description** | **str** | Description. | [optional] 
**field_config** | [**DashboardPanelFieldConfigModel**](DashboardPanelFieldConfigModel.md) |  | 
**grid_pos** | [**DashboardPanelGridPosModel**](DashboardPanelGridPosModel.md) |  | [optional] 
**id** | **int** | TODO docs | [optional] 
**interval** | **str** | TODO docs TODO tighter constraint | [optional] 
**links** | [**list[DashboardDashboardLinkModel]**](DashboardDashboardLinkModel.md) | Panel links. TODO fill this out - seems there are a couple variants? | [optional] 
**max_data_points** | **float** | TODO docs | [optional] 
**options** | **object** | options is specified by the PanelOptions field in panel plugin schemas. | 
**plugin_version** | **str** | FIXME this almost certainly has to be changed in favor of scuemata versions | [optional] 
**repeat** | **str** | Name of template variable to repeat for. | [optional] 
**repeat_direction** | **str** | Direction to repeat in if &#39;repeat&#39; is set. \&quot;h\&quot; for horizontal, \&quot;v\&quot; for vertical. | [default to 'h']
**tags** | **list[str]** | TODO docs | [optional] 
**targets** | [**list[DashboardTargetModel]**](DashboardTargetModel.md) | TODO docs | [optional] 
**thresholds** | **list[object]** | TODO docs | [optional] 
**time_from** | **str** | TODO docs TODO tighter constraint | [optional] 
**time_regions** | **list[object]** | TODO docs | [optional] 
**time_shift** | **str** | TODO docs TODO tighter constraint | [optional] 
**title** | **str** | Panel title. | [optional] 
**transformations** | [**list[DashboardPanelTransformationsModel]**](DashboardPanelTransformationsModel.md) |  | 
**transparent** | **bool** | Whether to display the panel without a background. | [default to False]
**type** | **str** | The panel plugin type id. May not be empty. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


