# gpyclient.OrgPreferencesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_preferences**](OrgPreferencesApi.md#get_org_preferences) | **GET** /org/preferences | Get Current Org Prefs.
[**patch_org_preferences**](OrgPreferencesApi.md#patch_org_preferences) | **PATCH** /org/preferences | Patch Current Org Prefs.
[**update_org_preferences**](OrgPreferencesApi.md#update_org_preferences) | **PUT** /org/preferences | Update Current Org Prefs.


# **get_org_preferences**
> PrefsModel get_org_preferences()

Get Current Org Prefs.

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
api_instance = gpyclient.OrgPreferencesApi(gpyclient.ApiClient(configuration))

try:
    # Get Current Org Prefs.
    api_response = api_instance.get_org_preferences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgPreferencesApi->get_org_preferences: %s\n" % e)
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

# **patch_org_preferences**
> InlineResponse20010Model patch_org_preferences(body)

Patch Current Org Prefs.

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
api_instance = gpyclient.OrgPreferencesApi(gpyclient.ApiClient(configuration))
body = gpyclient.PatchPrefsCmdModel() # PatchPrefsCmdModel | 

try:
    # Patch Current Org Prefs.
    api_response = api_instance.patch_org_preferences(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgPreferencesApi->patch_org_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchPrefsCmdModel**](PatchPrefsCmdModel.md)|  | 

### Return type

[**InlineResponse20010Model**](InlineResponse20010Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_preferences**
> InlineResponse20010Model update_org_preferences(body)

Update Current Org Prefs.

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
api_instance = gpyclient.OrgPreferencesApi(gpyclient.ApiClient(configuration))
body = gpyclient.UpdatePrefsCmdModel() # UpdatePrefsCmdModel | 

try:
    # Update Current Org Prefs.
    api_response = api_instance.update_org_preferences(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgPreferencesApi->update_org_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePrefsCmdModel**](UpdatePrefsCmdModel.md)|  | 

### Return type

[**InlineResponse20010Model**](InlineResponse20010Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

