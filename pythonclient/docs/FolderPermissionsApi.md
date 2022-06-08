# pythonclient.FolderPermissionsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_folder_permissions**](FolderPermissionsApi.md#get_folder_permissions) | **GET** /folders/{folder_uid}/permissions | Gets all existing permissions for the folder with the given &#x60;uid&#x60;.
[**update_folder_permissions**](FolderPermissionsApi.md#update_folder_permissions) | **POST** /folders/{folder_uid}/permissions | Updates permissions for a folder. This operation will remove existing permissions if they’re not included in the request.


# **get_folder_permissions**
> list[DashboardAclInfoDTOModel] get_folder_permissions(folder_uid)

Gets all existing permissions for the folder with the given `uid`.

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
api_instance = pythonclient.FolderPermissionsApi(pythonclient.ApiClient(configuration))
folder_uid = 'folder_uid_example' # str | 

try:
    # Gets all existing permissions for the folder with the given `uid`.
    api_response = api_instance.get_folder_permissions(folder_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderPermissionsApi->get_folder_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_uid** | **str**|  | 

### Return type

[**list[DashboardAclInfoDTOModel]**](DashboardAclInfoDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder_permissions**
> SuccessResponseBodyModel update_folder_permissions(body, folder_uid)

Updates permissions for a folder. This operation will remove existing permissions if they’re not included in the request.

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
api_instance = pythonclient.FolderPermissionsApi(pythonclient.ApiClient(configuration))
body = pythonclient.UpdateDashboardAclCommandModel() # UpdateDashboardAclCommandModel | 
folder_uid = 'folder_uid_example' # str | 

try:
    # Updates permissions for a folder. This operation will remove existing permissions if they’re not included in the request.
    api_response = api_instance.update_folder_permissions(body, folder_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderPermissionsApi->update_folder_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDashboardAclCommandModel**](UpdateDashboardAclCommandModel.md)|  | 
 **folder_uid** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

