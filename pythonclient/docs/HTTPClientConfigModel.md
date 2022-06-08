# HTTPClientConfigModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**AuthorizationModel**](AuthorizationModel.md) |  | [optional] 
**basic_auth** | [**BasicAuthModel**](BasicAuthModel.md) |  | [optional] 
**bearer_token** | [**SecretModel**](SecretModel.md) |  | [optional] 
**bearer_token_file** | **str** | The bearer token file for the targets. Deprecated in favour of Authorization.CredentialsFile. | [optional] 
**follow_redirects** | **bool** | FollowRedirects specifies whether the client should follow HTTP 3xx redirects. The omitempty flag is not set, because it would be hidden from the marshalled configuration when set to false. | [optional] 
**oauth2** | [**OAuth2Model**](OAuth2Model.md) |  | [optional] 
**proxy_url** | [**URLModel**](URLModel.md) |  | [optional] 
**tls_config** | [**TLSConfigModel**](TLSConfigModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


