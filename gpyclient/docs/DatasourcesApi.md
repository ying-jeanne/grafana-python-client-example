# gpyclient.DatasourcesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_datasource**](DatasourcesApi.md#add_datasource) | **POST** /datasources | Create a data source.
[**check_datasource_health**](DatasourcesApi.md#check_datasource_health) | **GET** /datasources/uid/{uid}/health | Check data source health by Id.
[**check_datasource_health_by_id**](DatasourcesApi.md#check_datasource_health_by_id) | **GET** /datasources/{id}/health | Check data source health by Id.
[**datasource_proxy_delet_ecalls**](DatasourcesApi.md#datasource_proxy_delet_ecalls) | **DELETE** /datasources/proxy/{id}/{datasource_proxy_route} | Data source proxy DELETE calls.
[**datasource_proxy_delete_by_ui_dcalls**](DatasourcesApi.md#datasource_proxy_delete_by_ui_dcalls) | **DELETE** /datasources/proxy/uid/{uid}/{datasource_proxy_route} | Data source proxy DELETE calls.
[**datasource_proxy_ge_tcalls**](DatasourcesApi.md#datasource_proxy_ge_tcalls) | **GET** /datasources/proxy/{id}/{datasource_proxy_route} | Data source proxy GET calls.
[**datasource_proxy_get_by_ui_dcalls**](DatasourcesApi.md#datasource_proxy_get_by_ui_dcalls) | **GET** /datasources/proxy/uid/{uid}/{datasource_proxy_route} | Data source proxy GET calls.
[**datasource_proxy_pos_tcalls**](DatasourcesApi.md#datasource_proxy_pos_tcalls) | **POST** /datasources/proxy/{id}/{datasource_proxy_route} | Data source proxy POST calls.
[**datasource_proxy_post_by_ui_dcalls**](DatasourcesApi.md#datasource_proxy_post_by_ui_dcalls) | **POST** /datasources/proxy/uid/{uid}/{datasource_proxy_route} | Data source proxy POST calls.
[**delete_datasource_by_id**](DatasourcesApi.md#delete_datasource_by_id) | **DELETE** /datasources/{id} | Delete an existing data source by id.
[**delete_datasource_by_name**](DatasourcesApi.md#delete_datasource_by_name) | **DELETE** /datasources/name/{name} | Delete an existing data source by name.
[**delete_datasource_by_uid**](DatasourcesApi.md#delete_datasource_by_uid) | **DELETE** /datasources/uid/{uid} | Delete an existing data source by UID.
[**fetch_datasource_resources**](DatasourcesApi.md#fetch_datasource_resources) | **GET** /datasources/uid/{uid}/resources/{datasource_proxy_route} | Fetch data source resources.
[**fetch_datasource_resources_by_id**](DatasourcesApi.md#fetch_datasource_resources_by_id) | **GET** /datasources/{id}/resources/{datasource_proxy_route} | Fetch data source resources by Id.
[**get_datasource_by_id**](DatasourcesApi.md#get_datasource_by_id) | **GET** /datasources/{id} | Get a single data source by Id.
[**get_datasource_by_name**](DatasourcesApi.md#get_datasource_by_name) | **GET** /datasources/name/{name} | Get a single data source by Name.
[**get_datasource_by_uid**](DatasourcesApi.md#get_datasource_by_uid) | **GET** /datasources/uid/{uid} | Get a single data source by UID.
[**get_datasource_id_by_name**](DatasourcesApi.md#get_datasource_id_by_name) | **GET** /datasources/id/{name} | Get data source Id by Name.
[**get_datasources**](DatasourcesApi.md#get_datasources) | **GET** /datasources | Get all data sources.
[**query_datasource**](DatasourcesApi.md#query_datasource) | **POST** /tsdb/query | Query metrics.
[**update_datasource_by_id**](DatasourcesApi.md#update_datasource_by_id) | **PUT** /datasources/{id} | Update an existing data source by its sequential ID.
[**update_datasource_by_uid**](DatasourcesApi.md#update_datasource_by_uid) | **PUT** /datasources/uid/{uid} | Update an existing data source.


# **add_datasource**
> InlineResponse2006Model add_datasource(body)

Create a data source.

By defining `password` and `basicAuthPassword` under secureJsonData property Grafana encrypts them securely as an encrypted blob in the database. The response then lists the encrypted fields under secureJsonFields.  If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:create`

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
body = gpyclient.AddDataSourceCommandModel() # AddDataSourceCommandModel | 

try:
    # Create a data source.
    api_response = api_instance.add_datasource(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->add_datasource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddDataSourceCommandModel**](AddDataSourceCommandModel.md)|  | 

### Return type

[**InlineResponse2006Model**](InlineResponse2006Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_datasource_health**
> SuccessResponseBodyModel check_datasource_health(uid)

Check data source health by Id.

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Check data source health by Id.
    api_response = api_instance.check_datasource_health(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->check_datasource_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_datasource_health_by_id**
> SuccessResponseBodyModel check_datasource_health_by_id(id)

Check data source health by Id.

Please refer to [updated API](#/datasources/checkDatasourceHealth) instead

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Check data source health by Id.
    api_response = api_instance.check_datasource_health_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->check_datasource_health_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_delet_ecalls**
> datasource_proxy_delet_ecalls(id, datasource_proxy_route)

Data source proxy DELETE calls.

Proxies all calls to the actual data source.  Please refer to [updated API](#/datasources/datasourceProxyDELETEByUIDcalls) instead

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
id = 'id_example' # str | 
datasource_proxy_route = 'datasource_proxy_route_example' # str | 

try:
    # Data source proxy DELETE calls.
    api_instance.datasource_proxy_delet_ecalls(id, datasource_proxy_route)
except ApiException as e:
    print("Exception when calling DatasourcesApi->datasource_proxy_delet_ecalls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **datasource_proxy_route** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_delete_by_ui_dcalls**
> datasource_proxy_delete_by_ui_dcalls(uid, datasource_proxy_route)

Data source proxy DELETE calls.

Proxies all calls to the actual data source.

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 
datasource_proxy_route = 'datasource_proxy_route_example' # str | 

try:
    # Data source proxy DELETE calls.
    api_instance.datasource_proxy_delete_by_ui_dcalls(uid, datasource_proxy_route)
except ApiException as e:
    print("Exception when calling DatasourcesApi->datasource_proxy_delete_by_ui_dcalls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **datasource_proxy_route** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_ge_tcalls**
> datasource_proxy_ge_tcalls(id, datasource_proxy_route)

Data source proxy GET calls.

Proxies all calls to the actual data source.  Please refer to [updated API](#/datasources/datasourceProxyGETByUIDcalls) instead

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
id = 'id_example' # str | 
datasource_proxy_route = 'datasource_proxy_route_example' # str | 

try:
    # Data source proxy GET calls.
    api_instance.datasource_proxy_ge_tcalls(id, datasource_proxy_route)
except ApiException as e:
    print("Exception when calling DatasourcesApi->datasource_proxy_ge_tcalls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **datasource_proxy_route** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_get_by_ui_dcalls**
> datasource_proxy_get_by_ui_dcalls(uid, datasource_proxy_route)

Data source proxy GET calls.

Proxies all calls to the actual data source.

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 
datasource_proxy_route = 'datasource_proxy_route_example' # str | 

try:
    # Data source proxy GET calls.
    api_instance.datasource_proxy_get_by_ui_dcalls(uid, datasource_proxy_route)
except ApiException as e:
    print("Exception when calling DatasourcesApi->datasource_proxy_get_by_ui_dcalls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **datasource_proxy_route** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_pos_tcalls**
> datasource_proxy_pos_tcalls(id, datasource_proxy_route, datasource_proxy_param)

Data source proxy POST calls.

Proxies all calls to the actual data source. The data source should support POST methods for the specific path and role as defined  Please refer to [updated API](#/datasources/datasourceProxyPOSTByUIDcalls) instead

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
id = 'id_example' # str | 
datasource_proxy_route = 'datasource_proxy_route_example' # str | 
datasource_proxy_param = NULL # object | 

try:
    # Data source proxy POST calls.
    api_instance.datasource_proxy_pos_tcalls(id, datasource_proxy_route, datasource_proxy_param)
except ApiException as e:
    print("Exception when calling DatasourcesApi->datasource_proxy_pos_tcalls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **datasource_proxy_route** | **str**|  | 
 **datasource_proxy_param** | **object**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_post_by_ui_dcalls**
> datasource_proxy_post_by_ui_dcalls(uid, datasource_proxy_route)

Data source proxy POST calls.

Proxies all calls to the actual data source. The data source should support POST methods for the specific path and role as defined

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 
datasource_proxy_route = 'datasource_proxy_route_example' # str | 

try:
    # Data source proxy POST calls.
    api_instance.datasource_proxy_post_by_ui_dcalls(uid, datasource_proxy_route)
except ApiException as e:
    print("Exception when calling DatasourcesApi->datasource_proxy_post_by_ui_dcalls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **datasource_proxy_route** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datasource_by_id**
> SuccessResponseBodyModel delete_datasource_by_id(id)

Delete an existing data source by id.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:delete` and scopes: `datasources:*`, `datasources:id:*` and `datasources:id:1` (single data source).  Please refer to [updated API](#/datasources/deleteDatasourceByUID) instead

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete an existing data source by id.
    api_response = api_instance.delete_datasource_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->delete_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datasource_by_name**
> InlineResponse2008Model delete_datasource_by_name(name)

Delete an existing data source by name.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:delete` and scopes: `datasources:*`, `datasources:name:*` and `datasources:name:test_datasource` (single data source).

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Delete an existing data source by name.
    api_response = api_instance.delete_datasource_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->delete_datasource_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**InlineResponse2008Model**](InlineResponse2008Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datasource_by_uid**
> SuccessResponseBodyModel delete_datasource_by_uid(uid)

Delete an existing data source by UID.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:delete` and scopes: `datasources:*`, `datasources:uid:*` and `datasources:uid:kLtEtcRGk` (single data source).

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Delete an existing data source by UID.
    api_response = api_instance.delete_datasource_by_uid(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->delete_datasource_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_datasource_resources**
> SuccessResponseBodyModel fetch_datasource_resources(uid, datasource_proxy_route)

Fetch data source resources.

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 
datasource_proxy_route = 'datasource_proxy_route_example' # str | 

try:
    # Fetch data source resources.
    api_response = api_instance.fetch_datasource_resources(uid, datasource_proxy_route)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->fetch_datasource_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **datasource_proxy_route** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_datasource_resources_by_id**
> SuccessResponseBodyModel fetch_datasource_resources_by_id(id, datasource_proxy_route)

Fetch data source resources by Id.

Please refer to [updated API](#/datasources/fetchDatasourceResources) instead

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
id = 'id_example' # str | 
datasource_proxy_route = 'datasource_proxy_route_example' # str | 

try:
    # Fetch data source resources by Id.
    api_response = api_instance.fetch_datasource_resources_by_id(id, datasource_proxy_route)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->fetch_datasource_resources_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **datasource_proxy_route** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasource_by_id**
> DataSourceModel get_datasource_by_id(id)

Get a single data source by Id.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:read` and scopes: `datasources:*`, `datasources:id:*` and `datasources:id:1` (single data source).  Please refer to [updated API](#/datasources/getDatasourceByUID) instead

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a single data source by Id.
    api_response = api_instance.get_datasource_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->get_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DataSourceModel**](DataSourceModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasource_by_name**
> DataSourceModel get_datasource_by_name(name)

Get a single data source by Name.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:read` and scopes: `datasources:*`, `datasources:name:*` and `datasources:name:test_datasource` (single data source).

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Get a single data source by Name.
    api_response = api_instance.get_datasource_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->get_datasource_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**DataSourceModel**](DataSourceModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasource_by_uid**
> DataSourceModel get_datasource_by_uid(uid)

Get a single data source by UID.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:read` and scopes: `datasources:*`, `datasources:uid:*` and `datasources:uid:kLtEtcRGk` (single data source).

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Get a single data source by UID.
    api_response = api_instance.get_datasource_by_uid(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->get_datasource_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**DataSourceModel**](DataSourceModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasource_id_by_name**
> InlineResponse2007Model get_datasource_id_by_name(name)

Get data source Id by Name.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:read` and scopes: `datasources:*`, `datasources:name:*` and `datasources:name:test_datasource` (single data source).

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Get data source Id by Name.
    api_response = api_instance.get_datasource_id_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->get_datasource_id_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**InlineResponse2007Model**](InlineResponse2007Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasources**
> DataSourceListModel get_datasources()

Get all data sources.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:read` and scope: `datasources:*`.

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))

try:
    # Get all data sources.
    api_response = api_instance.get_datasources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->get_datasources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DataSourceListModel**](DataSourceListModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_datasource**
> DataResponseModel query_datasource(body)

Query metrics.

Please refer to [updated API](#/ds/queryMetricsWithExpressions) instead  Queries a data source having backend implementation.  Most of Grafana’s builtin data sources have backend implementation.  If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:query`.

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
body = gpyclient.MetricRequestModel() # MetricRequestModel | 

try:
    # Query metrics.
    api_response = api_instance.query_datasource(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->query_datasource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetricRequestModel**](MetricRequestModel.md)|  | 

### Return type

[**DataResponseModel**](DataResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_datasource_by_id**
> InlineResponse2006Model update_datasource_by_id(id, body)

Update an existing data source by its sequential ID.

Similar to creating a data source, `password` and `basicAuthPassword` should be defined under secureJsonData in order to be stored securely as an encrypted blob in the database. Then, the encrypted fields are listed under secureJsonFields section in the response.  If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:write` and scopes: `datasources:*`, `datasources:id:*` and `datasources:id:1` (single data source).  Please refer to [updated API](#/datasources/updateDatasourceByUID) instead

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
id = 'id_example' # str | 
body = gpyclient.UpdateDataSourceCommandModel() # UpdateDataSourceCommandModel | 

try:
    # Update an existing data source by its sequential ID.
    api_response = api_instance.update_datasource_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->update_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**UpdateDataSourceCommandModel**](UpdateDataSourceCommandModel.md)|  | 

### Return type

[**InlineResponse2006Model**](InlineResponse2006Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_datasource_by_uid**
> InlineResponse2006Model update_datasource_by_uid(uid, body)

Update an existing data source.

Similar to creating a data source, `password` and `basicAuthPassword` should be defined under secureJsonData in order to be stored securely as an encrypted blob in the database. Then, the encrypted fields are listed under secureJsonFields section in the response.  If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:write` and scopes: `datasources:*`, `datasources:uid:*` and `datasources:uid:1` (single data source).

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
api_instance = gpyclient.DatasourcesApi(gpyclient.ApiClient(configuration))
uid = 'uid_example' # str | 
body = gpyclient.UpdateDataSourceCommandModel() # UpdateDataSourceCommandModel | 

try:
    # Update an existing data source.
    api_response = api_instance.update_datasource_by_uid(uid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->update_datasource_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **body** | [**UpdateDataSourceCommandModel**](UpdateDataSourceCommandModel.md)|  | 

### Return type

[**InlineResponse2006Model**](InlineResponse2006Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

