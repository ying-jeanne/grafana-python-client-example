# gpyclient.SyncTeamGroupsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_group_api**](SyncTeamGroupsApi.md#add_team_group_api) | **POST** /teams/{teamId}/groups | Add External Group.
[**get_team_groups_api**](SyncTeamGroupsApi.md#get_team_groups_api) | **GET** /teams/{teamId}/groups | Get External Groups.
[**remove_team_group_api**](SyncTeamGroupsApi.md#remove_team_group_api) | **DELETE** /teams/{teamId}/groups/{groupId} | Remove External Group.


# **add_team_group_api**
> SuccessResponseBodyModel add_team_group_api(body, team_id)

Add External Group.

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
api_instance = gpyclient.SyncTeamGroupsApi(gpyclient.ApiClient(configuration))
body = gpyclient.TeamGroupMappingModel() # TeamGroupMappingModel | 
team_id = 789 # int | 

try:
    # Add External Group.
    api_response = api_instance.add_team_group_api(body, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncTeamGroupsApi->add_team_group_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamGroupMappingModel**](TeamGroupMappingModel.md)|  | 
 **team_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_groups_api**
> list[TeamGroupDTOModel] get_team_groups_api(team_id)

Get External Groups.

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
api_instance = gpyclient.SyncTeamGroupsApi(gpyclient.ApiClient(configuration))
team_id = 789 # int | 

try:
    # Get External Groups.
    api_response = api_instance.get_team_groups_api(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncTeamGroupsApi->get_team_groups_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | 

### Return type

[**list[TeamGroupDTOModel]**](TeamGroupDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_team_group_api**
> SuccessResponseBodyModel remove_team_group_api(group_id, team_id)

Remove External Group.

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
api_instance = gpyclient.SyncTeamGroupsApi(gpyclient.ApiClient(configuration))
group_id = 789 # int | 
team_id = 789 # int | 

try:
    # Remove External Group.
    api_response = api_instance.remove_team_group_api(group_id, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncTeamGroupsApi->remove_team_group_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **team_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

