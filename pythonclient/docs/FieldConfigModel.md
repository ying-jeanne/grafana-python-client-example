# FieldConfigModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **dict(str, object)** | Map values to a display color NOTE: this interface is under development in the frontend... so simple map for now | [optional] 
**custom** | **dict(str, object)** | Panel Specific Values | [optional] 
**decimals** | **int** |  | [optional] 
**description** | **str** | Description is human readable field metadata | [optional] 
**display_name** | **str** | DisplayName overrides Grafana default naming, should not be used from a data source | [optional] 
**display_name_from_ds** | **str** | DisplayNameFromDS overrides Grafana default naming in a better way that allows users to override it easily. | [optional] 
**filterable** | **bool** | Filterable indicates if the Field&#39;s data can be filtered by additional calls. | [optional] 
**interval** | **float** | Interval indicates the expected regular step between values in the series. When an interval exists, consumers can identify \&quot;missing\&quot; values when the expected value is not present. The grafana timeseries visualization will render disconnected values when missing values are found it the time field. The interval uses the same units as the values.  For time.Time, this is defined in milliseconds. | [optional] 
**links** | [**list[DataLinkModel]**](DataLinkModel.md) | The behavior when clicking on a result | [optional] 
**mappings** | [**ValueMappingsModel**](ValueMappingsModel.md) |  | [optional] 
**max** | [**ConfFloat64Model**](ConfFloat64Model.md) |  | [optional] 
**min** | [**ConfFloat64Model**](ConfFloat64Model.md) |  | [optional] 
**no_value** | **str** | Alternative to empty string | [optional] 
**path** | **str** | Path is an explicit path to the field in the datasource. When the frame meta includes a path, this will default to &#x60;${frame.meta.path}/${field.name}  When defined, this value can be used as an identifier within the datasource scope, and may be used as an identifier to update values in a subsequent request | [optional] 
**thresholds** | [**ThresholdsConfigModel**](ThresholdsConfigModel.md) |  | [optional] 
**unit** | **str** | Numeric Options | [optional] 
**writeable** | **bool** | Writeable indicates that the datasource knows how to update this value | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


