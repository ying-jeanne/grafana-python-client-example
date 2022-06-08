# gpyclient.SearchApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /search | 
[**search_sorting**](SearchApi.md#search_sorting) | **GET** /search/sorting | 


# **search**
> HitListModel search(query=query, tag=tag, type=type, dashboard_ids=dashboard_ids, folder_ids=folder_ids, starred=starred, limit=limit, page=page, permission=permission, sort=sort)



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
api_instance = gpyclient.SearchApi(gpyclient.ApiClient(configuration))
query = 'query_example' # str | Search Query (optional)
tag = ['tag_example'] # list[str] | List of tags to search for (optional)
type = 'type_example' # str | Type to search for, dash-folder or dash-db (optional)
dashboard_ids = [56] # list[int] | List of dashboard id’s to search for (optional)
folder_ids = [56] # list[int] | List of folder id’s to search in for dashboards (optional)
starred = true # bool | Flag indicating if only starred Dashboards should be returned (optional)
limit = 789 # int | Limit the number of returned results (max 5000) (optional)
page = 789 # int | Use this parameter to access hits beyond limit. Numbering starts at 1. limit param acts as page size. Only available in Grafana v6.2+. (optional)
permission = 'View' # str | Set to `Edit` to return dashboards/folders that the user can edit (optional) (default to View)
sort = 'alpha-asc' # str | Sort method; for listing all the possible sort methods use the search sorting endpoint. (optional) (default to alpha-asc)

try:
    api_response = api_instance.search(query=query, tag=tag, type=type, dashboard_ids=dashboard_ids, folder_ids=folder_ids, starred=starred, limit=limit, page=page, permission=permission, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search Query | [optional] 
 **tag** | [**list[str]**](str.md)| List of tags to search for | [optional] 
 **type** | **str**| Type to search for, dash-folder or dash-db | [optional] 
 **dashboard_ids** | [**list[int]**](int.md)| List of dashboard id’s to search for | [optional] 
 **folder_ids** | [**list[int]**](int.md)| List of folder id’s to search in for dashboards | [optional] 
 **starred** | **bool**| Flag indicating if only starred Dashboards should be returned | [optional] 
 **limit** | **int**| Limit the number of returned results (max 5000) | [optional] 
 **page** | **int**| Use this parameter to access hits beyond limit. Numbering starts at 1. limit param acts as page size. Only available in Grafana v6.2+. | [optional] 
 **permission** | **str**| Set to &#x60;Edit&#x60; to return dashboards/folders that the user can edit | [optional] [default to View]
 **sort** | **str**| Sort method; for listing all the possible sort methods use the search sorting endpoint. | [optional] [default to alpha-asc]

### Return type

[**HitListModel**](HitListModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sorting**
> InlineResponse20012Model search_sorting()



List search sorting options

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
api_instance = gpyclient.SearchApi(gpyclient.ApiClient(configuration))

try:
    api_response = api_instance.search_sorting()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_sorting: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20012Model**](InlineResponse20012Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

