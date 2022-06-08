# gpyclient.DashboardPermissionsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard_permissions**](DashboardPermissionsApi.md#get_dashboard_permissions) | **GET** /dashboards/id/{DashboardID}/permissions | Gets all existing permissions for the given dashboard.
[**get_dashboard_permissions_with_uid**](DashboardPermissionsApi.md#get_dashboard_permissions_with_uid) | **GET** /dashboards/uid/{uid}/permissions | Gets all existing permissions for the given dashboard.
[**post_dashboard_permissions**](DashboardPermissionsApi.md#post_dashboard_permissions) | **POST** /dashboards/id/{DashboardID}/permissions | Updates permissions for a dashboard.
[**post_dashboard_permissions_with_uid**](DashboardPermissionsApi.md#post_dashboard_permissions_with_uid) | **POST** /dashboards/uid/{uid}/permissions | Updates permissions for a dashboard.


# **get_dashboard_permissions**
> list[DashboardAclInfoDTOModel] get_dashboard_permissions(dashboard_id)

Gets all existing permissions for the given dashboard.

Please refer to [updated API](#/dashboard_permissions/getDashboardPermissionsWithUid) instead

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
api_instance = gpyclient.DashboardPermissionsApi(gpyclient.ApiClient(configuration))
dashboard_id = 789 # int | 

try:
    # Gets all existing permissions for the given dashboard.
    api_response = api_instance.get_dashboard_permissions(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardPermissionsApi->get_dashboard_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 

### Return type

[**list[DashboardAclInfoDTOModel]**](DashboardAclInfoDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_permissions_with_uid**
> list[DashboardAclInfoDTOModel] get_dashboard_permissions_with_uid(uid)

Gets all existing permissions for the given dashboard.

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
api_instance = gpyclient.DashboardPermissionsApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Gets all existing permissions for the given dashboard.
    api_response = api_instance.get_dashboard_permissions_with_uid(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardPermissionsApi->get_dashboard_permissions_with_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**list[DashboardAclInfoDTOModel]**](DashboardAclInfoDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dashboard_permissions**
> SuccessResponseBodyModel post_dashboard_permissions(body, dashboard_id)

Updates permissions for a dashboard.

Please refer to [updated API](#/dashboard_permissions/postDashboardPermissionsWithUid) instead  This operation will remove existing permissions if they’re not included in the request.

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
api_instance = gpyclient.DashboardPermissionsApi(gpyclient.ApiClient(configuration))
body = gpyclient.UpdateDashboardAclCommandModel() # UpdateDashboardAclCommandModel | 
dashboard_id = 789 # int | 

try:
    # Updates permissions for a dashboard.
    api_response = api_instance.post_dashboard_permissions(body, dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardPermissionsApi->post_dashboard_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDashboardAclCommandModel**](UpdateDashboardAclCommandModel.md)|  | 
 **dashboard_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dashboard_permissions_with_uid**
> SuccessResponseBodyModel post_dashboard_permissions_with_uid(uid, body)

Updates permissions for a dashboard.

This operation will remove existing permissions if they’re not included in the request.

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
api_instance = gpyclient.DashboardPermissionsApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 
body = gpyclient.UpdateDashboardAclCommandModel() # UpdateDashboardAclCommandModel | 

try:
    # Updates permissions for a dashboard.
    api_response = api_instance.post_dashboard_permissions_with_uid(uid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardPermissionsApi->post_dashboard_permissions_with_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **body** | [**UpdateDashboardAclCommandModel**](UpdateDashboardAclCommandModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

