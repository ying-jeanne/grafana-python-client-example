# pythonclient.DashboardsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calc_dashboard_diff**](DashboardsApi.md#calc_dashboard_diff) | **POST** /dashboards/calculate-diff | Perform diff on two dashboards.
[**delete_dashboard_by_uid**](DashboardsApi.md#delete_dashboard_by_uid) | **DELETE** /dashboards/uid/{uid} | Delete dashboard by uid.
[**get_dashboard_by_uid**](DashboardsApi.md#get_dashboard_by_uid) | **GET** /dashboards/uid/{uid} | Get dashboard by uid.
[**get_dashboard_tags**](DashboardsApi.md#get_dashboard_tags) | **GET** /dashboards/tags | Get all dashboards tags of an organisation.
[**get_home_dashboard**](DashboardsApi.md#get_home_dashboard) | **GET** /dashboards/home | Get home dashboard.
[**import_dashboard**](DashboardsApi.md#import_dashboard) | **POST** /dashboards/import | Import dashboard.
[**post_dashboard**](DashboardsApi.md#post_dashboard) | **POST** /dashboards/db | Create / Update dashboard
[**trim_dashboard**](DashboardsApi.md#trim_dashboard) | **POST** /dashboards/trim | Trim defaults from dashboard.


# **calc_dashboard_diff**
> list[int] calc_dashboard_diff(body)

Perform diff on two dashboards.

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
api_instance = pythonclient.DashboardsApi(pythonclient.ApiClient(configuration))
body = pythonclient.BodyModel() # BodyModel | 

try:
    # Perform diff on two dashboards.
    api_response = api_instance.calc_dashboard_diff(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->calc_dashboard_diff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BodyModel**](BodyModel.md)|  | 

### Return type

**list[int]**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_by_uid**
> InlineResponse2005Model delete_dashboard_by_uid(uid)

Delete dashboard by uid.

Will delete the dashboard given the specified unique identifier (uid).

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
api_instance = pythonclient.DashboardsApi(pythonclient.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Delete dashboard by uid.
    api_response = api_instance.delete_dashboard_by_uid(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->delete_dashboard_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**InlineResponse2005Model**](InlineResponse2005Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_by_uid**
> DashboardFullWithMetaModel get_dashboard_by_uid(uid)

Get dashboard by uid.

Will return the dashboard given the dashboard unique identifier (uid).

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
api_instance = pythonclient.DashboardsApi(pythonclient.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Get dashboard by uid.
    api_response = api_instance.get_dashboard_by_uid(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->get_dashboard_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**DashboardFullWithMetaModel**](DashboardFullWithMetaModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_tags**
> list[DashboardTagCloudItemModel] get_dashboard_tags()

Get all dashboards tags of an organisation.

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
api_instance = pythonclient.DashboardsApi(pythonclient.ApiClient(configuration))

try:
    # Get all dashboards tags of an organisation.
    api_response = api_instance.get_dashboard_tags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->get_dashboard_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DashboardTagCloudItemModel]**](DashboardTagCloudItemModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_home_dashboard**
> GetHomeDashboardResponseModel get_home_dashboard()

Get home dashboard.

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
api_instance = pythonclient.DashboardsApi(pythonclient.ApiClient(configuration))

try:
    # Get home dashboard.
    api_response = api_instance.get_home_dashboard()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->get_home_dashboard: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetHomeDashboardResponseModel**](GetHomeDashboardResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_dashboard**
> ImportDashboardResponseModel import_dashboard(body)

Import dashboard.

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
api_instance = pythonclient.DashboardsApi(pythonclient.ApiClient(configuration))
body = pythonclient.ImportDashboardRequestModel() # ImportDashboardRequestModel | 

try:
    # Import dashboard.
    api_response = api_instance.import_dashboard(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->import_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportDashboardRequestModel**](ImportDashboardRequestModel.md)|  | 

### Return type

[**ImportDashboardResponseModel**](ImportDashboardResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dashboard**
> InlineResponse2004Model post_dashboard(body)

Create / Update dashboard

Creates a new dashboard or updates an existing dashboard.

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
api_instance = pythonclient.DashboardsApi(pythonclient.ApiClient(configuration))
body = pythonclient.SaveDashboardCommandModel() # SaveDashboardCommandModel | 

try:
    # Create / Update dashboard
    api_response = api_instance.post_dashboard(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->post_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaveDashboardCommandModel**](SaveDashboardCommandModel.md)|  | 

### Return type

[**InlineResponse2004Model**](InlineResponse2004Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trim_dashboard**
> TrimDashboardFullWithMetaModel trim_dashboard(body)

Trim defaults from dashboard.

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
api_instance = pythonclient.DashboardsApi(pythonclient.ApiClient(configuration))
body = pythonclient.TrimDashboardCommandModel() # TrimDashboardCommandModel | 

try:
    # Trim defaults from dashboard.
    api_response = api_instance.trim_dashboard(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->trim_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrimDashboardCommandModel**](TrimDashboardCommandModel.md)|  | 

### Return type

[**TrimDashboardFullWithMetaModel**](TrimDashboardFullWithMetaModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

