# gpyclient.ApiKeysApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ap_ikey**](ApiKeysApi.md#add_ap_ikey) | **POST** /auth/keys | Creates an API key.
[**delete_ap_ikey**](ApiKeysApi.md#delete_ap_ikey) | **DELETE** /auth/keys/{id} | Delete API key.
[**get_ap_ikeys**](ApiKeysApi.md#get_ap_ikeys) | **GET** /auth/keys | Get auth keys.


# **add_ap_ikey**
> NewApiKeyResultModel add_ap_ikey(body)

Creates an API key.

Will return details of the created API key

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gpyclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.ApiKeysApi(gpyclient.ApiClient(configuration))
body = gpyclient.AddApiKeyCommandModel() # AddApiKeyCommandModel | 

try:
    # Creates an API key.
    api_response = api_instance.add_ap_ikey(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->add_ap_ikey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddApiKeyCommandModel**](AddApiKeyCommandModel.md)|  | 

### Return type

[**NewApiKeyResultModel**](NewApiKeyResultModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ap_ikey**
> SuccessResponseBodyModel delete_ap_ikey(id)

Delete API key.

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gpyclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.ApiKeysApi(gpyclient.ApiClient(configuration))
id = 789 # int | 

try:
    # Delete API key.
    api_response = api_instance.delete_ap_ikey(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->delete_ap_ikey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ap_ikeys**
> list[ApiKeyDTOModel] get_ap_ikeys(include_expired=include_expired)

Get auth keys.

Will return auth keys.

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gpyclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.ApiKeysApi(gpyclient.ApiClient(configuration))
include_expired = false # bool | Show expired keys (optional) (default to false)

try:
    # Get auth keys.
    api_response = api_instance.get_ap_ikeys(include_expired=include_expired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->get_ap_ikeys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_expired** | **bool**| Show expired keys | [optional] [default to false]

### Return type

[**list[ApiKeyDTOModel]**](ApiKeyDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

