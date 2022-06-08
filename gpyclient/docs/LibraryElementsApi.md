# gpyclient.LibraryElementsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_library_element**](LibraryElementsApi.md#create_library_element) | **POST** /library-elements | Create library element.
[**delete_library_element_by_uid**](LibraryElementsApi.md#delete_library_element_by_uid) | **DELETE** /library-elements/{library_element_uid} | Delete library element.
[**get_library_element_by_name**](LibraryElementsApi.md#get_library_element_by_name) | **GET** /library-elements/name/{library_element_name} | Get library element by name.
[**get_library_element_by_uid**](LibraryElementsApi.md#get_library_element_by_uid) | **GET** /library-elements/{library_element_uid} | Get library element by UID.
[**get_library_element_connections**](LibraryElementsApi.md#get_library_element_connections) | **GET** /library-elements/{library_element_uid}/connections/ | Get library element connections.
[**get_library_elements**](LibraryElementsApi.md#get_library_elements) | **GET** /library-elements | Get all library elements.
[**update_library_element**](LibraryElementsApi.md#update_library_element) | **PATCH** /library-elements/{library_element_uid} | Update library element.


# **create_library_element**
> LibraryElementResponseModel create_library_element(body)

Create library element.

Creates a new library element.

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
api_instance = gpyclient.LibraryElementsApi(gpyclient.ApiClient(configuration))
body = gpyclient.CreateLibraryElementCommandModel() # CreateLibraryElementCommandModel | 

try:
    # Create library element.
    api_response = api_instance.create_library_element(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryElementsApi->create_library_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLibraryElementCommandModel**](CreateLibraryElementCommandModel.md)|  | 

### Return type

[**LibraryElementResponseModel**](LibraryElementResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_element_by_uid**
> SuccessResponseBodyModel delete_library_element_by_uid(library_element_uid)

Delete library element.

Deletes an existing library element as specified by the UID. This operation cannot be reverted. You cannot delete a library element that is connected. This operation cannot be reverted.

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
api_instance = gpyclient.LibraryElementsApi(gpyclient.ApiClient(configuration))
library_element_uid = 'library_element_uid_example' # str | 

try:
    # Delete library element.
    api_response = api_instance.delete_library_element_by_uid(library_element_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryElementsApi->delete_library_element_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_element_uid** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_element_by_name**
> LibraryElementResponseModel get_library_element_by_name(library_element_name)

Get library element by name.

Returns a library element with the given name.

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
api_instance = gpyclient.LibraryElementsApi(gpyclient.ApiClient(configuration))
library_element_name = 'library_element_name_example' # str | 

try:
    # Get library element by name.
    api_response = api_instance.get_library_element_by_name(library_element_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryElementsApi->get_library_element_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_element_name** | **str**|  | 

### Return type

[**LibraryElementResponseModel**](LibraryElementResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_element_by_uid**
> LibraryElementResponseModel get_library_element_by_uid(library_element_uid)

Get library element by UID.

Returns a library element with the given UID.

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
api_instance = gpyclient.LibraryElementsApi(gpyclient.ApiClient(configuration))
library_element_uid = 'library_element_uid_example' # str | 

try:
    # Get library element by UID.
    api_response = api_instance.get_library_element_by_uid(library_element_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryElementsApi->get_library_element_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_element_uid** | **str**|  | 

### Return type

[**LibraryElementResponseModel**](LibraryElementResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_element_connections**
> LibraryElementConnectionsResponseModel get_library_element_connections(library_element_uid)

Get library element connections.

Returns a list of connections for a library element based on the UID specified.

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
api_instance = gpyclient.LibraryElementsApi(gpyclient.ApiClient(configuration))
library_element_uid = 'library_element_uid_example' # str | 

try:
    # Get library element connections.
    api_response = api_instance.get_library_element_connections(library_element_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryElementsApi->get_library_element_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_element_uid** | **str**|  | 

### Return type

[**LibraryElementConnectionsResponseModel**](LibraryElementConnectionsResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_elements**
> LibraryElementSearchResponseModel get_library_elements(search_string=search_string, kind=kind, sort_direction=sort_direction, type_filter=type_filter, exclude_uid=exclude_uid, folder_filter=folder_filter, per_page=per_page, page=page)

Get all library elements.

Returns a list of all library elements the authenticated user has permission to view. Use the `perPage` query parameter to control the maximum number of library elements returned; the default limit is `100`. You can also use the `page` query parameter to fetch library elements from any page other than the first one.

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
api_instance = gpyclient.LibraryElementsApi(gpyclient.ApiClient(configuration))
search_string = 'search_string_example' # str | Part of the name or description searched for. (optional)
kind = 789 # int | Kind of element to search for. (optional)
sort_direction = 'sort_direction_example' # str | Sort order of elements. (optional)
type_filter = 'type_filter_example' # str | A comma separated list of types to filter the elements by (optional)
exclude_uid = 'exclude_uid_example' # str | Element UID to exclude from search results. (optional)
folder_filter = 'folder_filter_example' # str | A comma separated list of folder ID(s) to filter the elements by. (optional)
per_page = 100 # int | The number of results per page. (optional) (default to 100)
page = 1 # int | The page for a set of records, given that only perPage records are returned at a time. Numbering starts at 1. (optional) (default to 1)

try:
    # Get all library elements.
    api_response = api_instance.get_library_elements(search_string=search_string, kind=kind, sort_direction=sort_direction, type_filter=type_filter, exclude_uid=exclude_uid, folder_filter=folder_filter, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryElementsApi->get_library_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| Part of the name or description searched for. | [optional] 
 **kind** | **int**| Kind of element to search for. | [optional] 
 **sort_direction** | **str**| Sort order of elements. | [optional] 
 **type_filter** | **str**| A comma separated list of types to filter the elements by | [optional] 
 **exclude_uid** | **str**| Element UID to exclude from search results. | [optional] 
 **folder_filter** | **str**| A comma separated list of folder ID(s) to filter the elements by. | [optional] 
 **per_page** | **int**| The number of results per page. | [optional] [default to 100]
 **page** | **int**| The page for a set of records, given that only perPage records are returned at a time. Numbering starts at 1. | [optional] [default to 1]

### Return type

[**LibraryElementSearchResponseModel**](LibraryElementSearchResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_element**
> LibraryElementResponseModel update_library_element(library_element_uid, body)

Update library element.

Updates an existing library element identified by uid.

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
api_instance = gpyclient.LibraryElementsApi(gpyclient.ApiClient(configuration))
library_element_uid = 'library_element_uid_example' # str | 
body = gpyclient.PatchLibraryElementCommandModel() # PatchLibraryElementCommandModel | 

try:
    # Update library element.
    api_response = api_instance.update_library_element(library_element_uid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryElementsApi->update_library_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_element_uid** | **str**|  | 
 **body** | [**PatchLibraryElementCommandModel**](PatchLibraryElementCommandModel.md)|  | 

### Return type

[**LibraryElementResponseModel**](LibraryElementResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

