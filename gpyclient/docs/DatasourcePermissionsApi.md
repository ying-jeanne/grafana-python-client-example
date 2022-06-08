# gpyclient.DatasourcePermissionsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_permissions**](DatasourcePermissionsApi.md#delete_permissions) | **DELETE** /datasources/{datasourceId}/permissions/{permissionId} | Remove permission for a data source.
[**disable_permissions**](DatasourcePermissionsApi.md#disable_permissions) | **POST** /datasources/{datasourceId}/disable-permissions | Disable permissions for a data source.
[**enable_permissions**](DatasourcePermissionsApi.md#enable_permissions) | **POST** /datasources/{datasourceId}/enable-permissions | Enable permissions for a data source.
[**get_permissions**](DatasourcePermissionsApi.md#get_permissions) | **GET** /datasources/{datasourceId}/permissions | Get permissions for a data source.


# **delete_permissions**
> SuccessResponseBodyModel delete_permissions(datasource_id, permission_id)

Remove permission for a data source.

Removes the permission with the given permissionId for the data source with the given id.  You need to have a permission with action `datasources.permissions:delete` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).

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
api_instance = gpyclient.DatasourcePermissionsApi(gpyclient.ApiClient(configuration))
datasource_id = 'datasource_id_example' # str | 
permission_id = 'permission_id_example' # str | 

try:
    # Remove permission for a data source.
    api_response = api_instance.delete_permissions(datasource_id, permission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcePermissionsApi->delete_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 
 **permission_id** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_permissions**
> InlineResponse2006Model disable_permissions(datasource_id)

Disable permissions for a data source.

Disables permissions for the data source with the given id. All existing permissions will be removed and anyone will be able to query the data source.  You need to have a permission with action `datasources.permissions:toggle` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).

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
api_instance = gpyclient.DatasourcePermissionsApi(gpyclient.ApiClient(configuration))
datasource_id = 'datasource_id_example' # str | 

try:
    # Disable permissions for a data source.
    api_response = api_instance.disable_permissions(datasource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcePermissionsApi->disable_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 

### Return type

[**InlineResponse2006Model**](InlineResponse2006Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_permissions**
> InlineResponse2006Model enable_permissions(datasource_id)

Enable permissions for a data source.

Enables permissions for the data source with the given id. No one except Org Admins will be able to query the data source until permissions have been added which permit certain users or teams to query the data source.  You need to have a permission with action `datasources.permissions:toggle` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).

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
api_instance = gpyclient.DatasourcePermissionsApi(gpyclient.ApiClient(configuration))
datasource_id = 'datasource_id_example' # str | 

try:
    # Enable permissions for a data source.
    api_response = api_instance.enable_permissions(datasource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcePermissionsApi->enable_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 

### Return type

[**InlineResponse2006Model**](InlineResponse2006Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permissions**
> AddPermissionDTOModel get_permissions(datasource_id)

Get permissions for a data source.

Gets all existing permissions for the data source with the given id.  You need to have a permission with action `datasources.permissions:read` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).

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
api_instance = gpyclient.DatasourcePermissionsApi(gpyclient.ApiClient(configuration))
datasource_id = 'datasource_id_example' # str | 

try:
    # Get permissions for a data source.
    api_response = api_instance.get_permissions(datasource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcePermissionsApi->get_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 

### Return type

[**AddPermissionDTOModel**](AddPermissionDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

