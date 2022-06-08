# EmailConfigModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_identity** | **str** |  | [optional] 
**auth_password** | [**SecretModel**](SecretModel.md) |  | [optional] 
**auth_secret** | [**SecretModel**](SecretModel.md) |  | [optional] 
**auth_username** | **str** |  | [optional] 
**_from** | **str** |  | [optional] 
**headers** | **dict(str, str)** |  | [optional] 
**hello** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**require_tls** | **bool** |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**smarthost** | [**HostPortModel**](HostPortModel.md) |  | [optional] 
**text** | **str** |  | [optional] 
**tls_config** | [**TLSConfigModel**](TLSConfigModel.md) |  | [optional] 
**to** | **str** | Email address to notify. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


