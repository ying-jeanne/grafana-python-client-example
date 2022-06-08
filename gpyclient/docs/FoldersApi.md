# gpyclient.FoldersApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folder**](FoldersApi.md#create_folder) | **POST** /folders | Create folder.
[**delete_folder**](FoldersApi.md#delete_folder) | **DELETE** /folders/{folder_uid} | Delete folder.
[**get_folder_by_id**](FoldersApi.md#get_folder_by_id) | **GET** /folders/id/{folder_id} | Get folder by id.
[**get_folder_by_uid**](FoldersApi.md#get_folder_by_uid) | **GET** /folders/{folder_uid} | Get folder by uid.
[**get_folders**](FoldersApi.md#get_folders) | **GET** /folders | Get all folders.
[**update_folder**](FoldersApi.md#update_folder) | **PUT** /folders/{folder_uid} | Update folder.


# **create_folder**
> FolderModel create_folder(body)

Create folder.

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
api_instance = gpyclient.FoldersApi(gpyclient.ApiClient(configuration))
body = gpyclient.CreateFolderCommandModel() # CreateFolderCommandModel | 

try:
    # Create folder.
    api_response = api_instance.create_folder(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFolderCommandModel**](CreateFolderCommandModel.md)|  | 

### Return type

[**FolderModel**](FolderModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> InlineResponse2009Model delete_folder(folder_uid, force_delete_rules=force_delete_rules)

Delete folder.

Deletes an existing folder identified by UID along with all dashboards (and their alerts) stored in the folder. This operation cannot be reverted.

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
api_instance = gpyclient.FoldersApi(gpyclient.ApiClient(configuration))
folder_uid = 'folder_uid_example' # str | 
force_delete_rules = false # bool | If `true` any Grafana 8 Alerts under this folder will be deleted. Set to `false` so that the request will fail if the folder contains any Grafana 8 Alerts. (optional) (default to false)

try:
    # Delete folder.
    api_response = api_instance.delete_folder(folder_uid, force_delete_rules=force_delete_rules)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_uid** | **str**|  | 
 **force_delete_rules** | **bool**| If &#x60;true&#x60; any Grafana 8 Alerts under this folder will be deleted. Set to &#x60;false&#x60; so that the request will fail if the folder contains any Grafana 8 Alerts. | [optional] [default to false]

### Return type

[**InlineResponse2009Model**](InlineResponse2009Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_id**
> FolderModel get_folder_by_id(folder_id)

Get folder by id.

Returns the folder identified by id.

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
api_instance = gpyclient.FoldersApi(gpyclient.ApiClient(configuration))
folder_id = 789 # int | 

try:
    # Get folder by id.
    api_response = api_instance.get_folder_by_id(folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->get_folder_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**|  | 

### Return type

[**FolderModel**](FolderModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_uid**
> get_folder_by_uid(folder_uid)

Get folder by uid.

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
api_instance = gpyclient.FoldersApi(gpyclient.ApiClient(configuration))
folder_uid = 'folder_uid_example' # str | 

try:
    # Get folder by uid.
    api_instance.get_folder_by_uid(folder_uid)
except ApiException as e:
    print("Exception when calling FoldersApi->get_folder_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_uid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders**
> list[FolderSearchHitModel] get_folders(limit=limit, page=page)

Get all folders.

Returns all folders that the authenticated user has permission to view.

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
api_instance = gpyclient.FoldersApi(gpyclient.ApiClient(configuration))
limit = 1000 # int | Limit the maximum number of folders to return (optional) (default to 1000)
page = 1 # int | Page index for starting fetching folders (optional) (default to 1)

try:
    # Get all folders.
    api_response = api_instance.get_folders(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->get_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the maximum number of folders to return | [optional] [default to 1000]
 **page** | **int**| Page index for starting fetching folders | [optional] [default to 1]

### Return type

[**list[FolderSearchHitModel]**](FolderSearchHitModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder**
> FolderModel update_folder(folder_uid, body)

Update folder.

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
api_instance = gpyclient.FoldersApi(gpyclient.ApiClient(configuration))
folder_uid = 'folder_uid_example' # str | 
body = gpyclient.UpdateFolderCommandModel() # UpdateFolderCommandModel | To change the unique identifier (uid), provide another one. To overwrite an existing folder with newer version, set `overwrite` to `true`. Provide the current version to safelly update the folder: if the provided version differs from the stored one the request will fail, unless `overwrite` is `true`.

try:
    # Update folder.
    api_response = api_instance.update_folder(folder_uid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->update_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_uid** | **str**|  | 
 **body** | [**UpdateFolderCommandModel**](UpdateFolderCommandModel.md)| To change the unique identifier (uid), provide another one. To overwrite an existing folder with newer version, set &#x60;overwrite&#x60; to &#x60;true&#x60;. Provide the current version to safelly update the folder: if the provided version differs from the stored one the request will fail, unless &#x60;overwrite&#x60; is &#x60;true&#x60;. | 

### Return type

[**FolderModel**](FolderModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

