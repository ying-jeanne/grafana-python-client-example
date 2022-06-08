# DashboardPanelFieldConfigDefaultsModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**DashboardFieldColorModel**](DashboardFieldColorModel.md) |  | [optional] 
**custom** | **object** | custom is specified by the PanelFieldConfig field in panel plugin schemas. | [optional] 
**decimals** | **float** | Significant digits (for display) | [optional] 
**description** | **str** | Human readable field metadata | [optional] 
**display_name** | **str** | The display value for this field.  This supports template variables blank is auto | [optional] 
**display_name_from_ds** | **str** | This can be used by data sources that return and explicit naming structure for values and labels When this property is configured, this value is used rather than the default naming strategy. | [optional] 
**filterable** | **bool** | True if data source field supports ad-hoc filters | [optional] 
**links** | **list[object]** | // The behavior when clicking on a result | [optional] 
**mappings** | **list[object]** | Convert input values into a display string  TODO this one corresponds to a complex type with generics on the typescript side. Ouch. Will either need special care, or we&#39;ll just need to accept a very loosely specified schema. It&#39;s very unlikely we&#39;ll be able to translate cue to typescript generics in the general case, though this particular one *may* be able to work. | [optional] 
**max** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**no_value** | **str** | Alternative to empty string | [optional] 
**path** | **str** | An explict path to the field in the datasource.  When the frame meta includes a path, This will default to &#x60;${frame.meta.path}/${field.name}  When defined, this value can be used as an identifier within the datasource scope, and may be used to update the results | [optional] 
**thresholds** | [**DashboardThresholdsConfigModel**](DashboardThresholdsConfigModel.md) |  | [optional] 
**unit** | **str** | Numeric Options | [optional] 
**writeable** | **bool** | True if data source can write a value to the path.  Auth/authz are supported separately | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


