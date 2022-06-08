# gpyclient.DashboardVersionsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard_version**](DashboardVersionsApi.md#get_dashboard_version) | **GET** /dashboards/id/{DashboardID}/versions/{DashboardVersionID} | Get a specific dashboard version.
[**get_dashboard_version_by_uid**](DashboardVersionsApi.md#get_dashboard_version_by_uid) | **GET** /dashboards/uid/{uid}/versions/{DashboardVersionID} | Get a specific dashboard version using UID.
[**get_dashboard_versions**](DashboardVersionsApi.md#get_dashboard_versions) | **GET** /dashboards/id/{DashboardID}/versions | Gets all existing versions for the dashboard.
[**get_dashboard_versions_by_uid**](DashboardVersionsApi.md#get_dashboard_versions_by_uid) | **GET** /dashboards/uid/{uid}/versions | Gets all existing versions for the dashboard using UID.
[**restore_dashboard_version**](DashboardVersionsApi.md#restore_dashboard_version) | **POST** /dashboards/id/{DashboardID}/restore | Restore a dashboard to a given dashboard version.
[**restore_dashboard_version_by_uid**](DashboardVersionsApi.md#restore_dashboard_version_by_uid) | **POST** /dashboards/uid/{uid}/restore | Restore a dashboard to a given dashboard version using UID.


# **get_dashboard_version**
> DashboardVersionMetaModel get_dashboard_version(dashboard_id, dashboard_version_id)

Get a specific dashboard version.

Please refer to [updated API](#/dashboard_versions/getDashboardVersionByUID) instead

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
api_instance = gpyclient.DashboardVersionsApi(gpyclient.ApiClient(configuration))
dashboard_id = 789 # int | 
dashboard_version_id = 789 # int | 

try:
    # Get a specific dashboard version.
    api_response = api_instance.get_dashboard_version(dashboard_id, dashboard_version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardVersionsApi->get_dashboard_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 
 **dashboard_version_id** | **int**|  | 

### Return type

[**DashboardVersionMetaModel**](DashboardVersionMetaModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_version_by_uid**
> DashboardVersionMetaModel get_dashboard_version_by_uid(uid, dashboard_version_id)

Get a specific dashboard version using UID.

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
api_instance = gpyclient.DashboardVersionsApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 
dashboard_version_id = 789 # int | 

try:
    # Get a specific dashboard version using UID.
    api_response = api_instance.get_dashboard_version_by_uid(uid, dashboard_version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardVersionsApi->get_dashboard_version_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **dashboard_version_id** | **int**|  | 

### Return type

[**DashboardVersionMetaModel**](DashboardVersionMetaModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_versions**
> list[DashboardVersionDTOModel] get_dashboard_versions(dashboard_id, limit=limit, start=start)

Gets all existing versions for the dashboard.

Please refer to [updated API](#/dashboard_versions/getDashboardVersionsByUID) instead

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
api_instance = gpyclient.DashboardVersionsApi(gpyclient.ApiClient(configuration))
dashboard_id = 789 # int | 
limit = 0 # int | Maximum number of results to return (optional) (default to 0)
start = 0 # int | Version to start from when returning queries (optional) (default to 0)

try:
    # Gets all existing versions for the dashboard.
    api_response = api_instance.get_dashboard_versions(dashboard_id, limit=limit, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardVersionsApi->get_dashboard_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 0]
 **start** | **int**| Version to start from when returning queries | [optional] [default to 0]

### Return type

[**list[DashboardVersionDTOModel]**](DashboardVersionDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_versions_by_uid**
> list[DashboardVersionDTOModel] get_dashboard_versions_by_uid(uid, limit=limit, start=start)

Gets all existing versions for the dashboard using UID.

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
api_instance = gpyclient.DashboardVersionsApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 
limit = 0 # int | Maximum number of results to return (optional) (default to 0)
start = 0 # int | Version to start from when returning queries (optional) (default to 0)

try:
    # Gets all existing versions for the dashboard using UID.
    api_response = api_instance.get_dashboard_versions_by_uid(uid, limit=limit, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardVersionsApi->get_dashboard_versions_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 0]
 **start** | **int**| Version to start from when returning queries | [optional] [default to 0]

### Return type

[**list[DashboardVersionDTOModel]**](DashboardVersionDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_dashboard_version**
> InlineResponse2004Model restore_dashboard_version(dashboard_id, body)

Restore a dashboard to a given dashboard version.

Please refer to [updated API](#/dashboard_versions/restoreDashboardVersionByUID) instead

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
api_instance = gpyclient.DashboardVersionsApi(gpyclient.ApiClient(configuration))
dashboard_id = 789 # int | 
body = gpyclient.RestoreDashboardVersionCommandModel() # RestoreDashboardVersionCommandModel | 

try:
    # Restore a dashboard to a given dashboard version.
    api_response = api_instance.restore_dashboard_version(dashboard_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardVersionsApi->restore_dashboard_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 
 **body** | [**RestoreDashboardVersionCommandModel**](RestoreDashboardVersionCommandModel.md)|  | 

### Return type

[**InlineResponse2004Model**](InlineResponse2004Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_dashboard_version_by_uid**
> InlineResponse2004Model restore_dashboard_version_by_uid(uid, body)

Restore a dashboard to a given dashboard version using UID.

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
api_instance = gpyclient.DashboardVersionsApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 
body = gpyclient.RestoreDashboardVersionCommandModel() # RestoreDashboardVersionCommandModel | 

try:
    # Restore a dashboard to a given dashboard version using UID.
    api_response = api_instance.restore_dashboard_version_by_uid(uid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardVersionsApi->restore_dashboard_version_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **body** | [**RestoreDashboardVersionCommandModel**](RestoreDashboardVersionCommandModel.md)|  | 

### Return type

[**InlineResponse2004Model**](InlineResponse2004Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

