# GlobalConfigModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_config** | [**HTTPClientConfigModel**](HTTPClientConfigModel.md) |  | [optional] 
**opsgenie_api_key** | [**SecretModel**](SecretModel.md) |  | [optional] 
**opsgenie_api_key_file** | **str** |  | [optional] 
**opsgenie_api_url** | [**URLModel**](URLModel.md) |  | [optional] 
**pagerduty_url** | [**URLModel**](URLModel.md) |  | [optional] 
**resolve_timeout** | [**DurationModel**](DurationModel.md) |  | [optional] 
**slack_api_url** | [**SecretURLModel**](SecretURLModel.md) |  | [optional] 
**slack_api_url_file** | **str** |  | [optional] 
**smtp_auth_identity** | **str** |  | [optional] 
**smtp_auth_password** | [**SecretModel**](SecretModel.md) |  | [optional] 
**smtp_auth_secret** | [**SecretModel**](SecretModel.md) |  | [optional] 
**smtp_auth_username** | **str** |  | [optional] 
**smtp_from** | **str** |  | [optional] 
**smtp_hello** | **str** |  | [optional] 
**smtp_require_tls** | **bool** |  | [optional] 
**smtp_smarthost** | [**HostPortModel**](HostPortModel.md) |  | [optional] 
**victorops_api_key** | [**SecretModel**](SecretModel.md) |  | [optional] 
**victorops_api_url** | [**URLModel**](URLModel.md) |  | [optional] 
**wechat_api_corp_id** | **str** |  | [optional] 
**wechat_api_secret** | [**SecretModel**](SecretModel.md) |  | [optional] 
**wechat_api_url** | [**URLModel**](URLModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


