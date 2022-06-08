# pythonclient.UserPreferencesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_preferences**](UserPreferencesApi.md#get_user_preferences) | **GET** /user/preferences | Get user preferences.
[**patch_user_preferences**](UserPreferencesApi.md#patch_user_preferences) | **PATCH** /user/preferences | Patch user preferences.
[**update_user_preferences**](UserPreferencesApi.md#update_user_preferences) | **PUT** /user/preferences | Update user preferences.


# **get_user_preferences**
> PrefsModel get_user_preferences()

Get user preferences.

### Example
```python
from __future__ import print_function
import time
import pythonclient
from pythonclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = pythonclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = pythonclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pythonclient.UserPreferencesApi(pythonclient.ApiClient(configuration))

try:
    # Get user preferences.
    api_response = api_instance.get_user_preferences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPreferencesApi->get_user_preferences: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PrefsModel**](PrefsModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_user_preferences**
> SuccessResponseBodyModel patch_user_preferences(body)

Patch user preferences.

### Example
```python
from __future__ import print_function
import time
import pythonclient
from pythonclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = pythonclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = pythonclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pythonclient.UserPreferencesApi(pythonclient.ApiClient(configuration))
body = pythonclient.PatchPrefsCmdModel() # PatchPrefsCmdModel | 

try:
    # Patch user preferences.
    api_response = api_instance.patch_user_preferences(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPreferencesApi->patch_user_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchPrefsCmdModel**](PatchPrefsCmdModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_preferences**
> SuccessResponseBodyModel update_user_preferences(body)

Update user preferences.

Omitting a key (`theme`, `homeDashboardId`, `timezone`) will cause the current value to be replaced with the system default value.

### Example
```python
from __future__ import print_function
import time
import pythonclient
from pythonclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = pythonclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = pythonclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pythonclient.UserPreferencesApi(pythonclient.ApiClient(configuration))
body = pythonclient.UpdatePrefsCmdModel() # UpdatePrefsCmdModel | 

try:
    # Update user preferences.
    api_response = api_instance.update_user_preferences(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPreferencesApi->update_user_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePrefsCmdModel**](UpdatePrefsCmdModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

