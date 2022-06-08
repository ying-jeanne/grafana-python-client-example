# gpyclient.TeamsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_member**](TeamsApi.md#add_team_member) | **POST** /teams/{team_id}/members | Add Team Member.
[**create_team**](TeamsApi.md#create_team) | **POST** /teams | Add Team.
[**delete_team_by_id**](TeamsApi.md#delete_team_by_id) | **DELETE** /teams/{team_id} | Delete Team By ID.
[**get_team**](TeamsApi.md#get_team) | **GET** /teams/{team_id} | Get Team By ID.
[**get_team_members**](TeamsApi.md#get_team_members) | **GET** /teams/{team_id}/members | Get Team Members.
[**get_team_preferences**](TeamsApi.md#get_team_preferences) | **GET** /teams/{team_id}/preferences | Get Team Preferences.
[**remove_team_member**](TeamsApi.md#remove_team_member) | **DELETE** /teams/{team_id}/members/{user_id} | Remove Member From Team.
[**search_teams**](TeamsApi.md#search_teams) | **GET** /teams/search | Team Search With Paging.
[**update_team**](TeamsApi.md#update_team) | **PUT** /teams/{team_id} | Update Team.
[**update_team_member**](TeamsApi.md#update_team_member) | **PUT** /teams/{team_id}/members/{user_id} | Update Team Member.
[**update_team_preferences**](TeamsApi.md#update_team_preferences) | **PUT** /teams/{team_id}/preferences | Update Team Preferences.


# **add_team_member**
> SuccessResponseBodyModel add_team_member(team_id)

Add Team Member.

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
api_instance = gpyclient.TeamsApi(gpyclient.ApiClient(configuration))
team_id = 'team_id_example' # str | 

try:
    # Add Team Member.
    api_response = api_instance.add_team_member(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->add_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team**
> InlineResponse20015Model create_team(body)

Add Team.

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
api_instance = gpyclient.TeamsApi(gpyclient.ApiClient(configuration))
body = gpyclient.CreateTeamCommandModel() # CreateTeamCommandModel | 

try:
    # Add Team.
    api_response = api_instance.create_team(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTeamCommandModel**](CreateTeamCommandModel.md)|  | 

### Return type

[**InlineResponse20015Model**](InlineResponse20015Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_by_id**
> SuccessResponseBodyModel delete_team_by_id(team_id)

Delete Team By ID.

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
api_instance = gpyclient.TeamsApi(gpyclient.ApiClient(configuration))
team_id = 'team_id_example' # str | 

try:
    # Delete Team By ID.
    api_response = api_instance.delete_team_by_id(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_team_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> TeamDTOModel get_team(team_id)

Get Team By ID.

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
api_instance = gpyclient.TeamsApi(gpyclient.ApiClient(configuration))
team_id = 'team_id_example' # str | 

try:
    # Get Team By ID.
    api_response = api_instance.get_team(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**TeamDTOModel**](TeamDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_members**
> SuccessResponseBodyModel get_team_members(team_id)

Get Team Members.

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
api_instance = gpyclient.TeamsApi(gpyclient.ApiClient(configuration))
team_id = 'team_id_example' # str | 

try:
    # Get Team Members.
    api_response = api_instance.get_team_members(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_preferences**
> PrefsModel get_team_preferences(team_id)

Get Team Preferences.

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
api_instance = gpyclient.TeamsApi(gpyclient.ApiClient(configuration))
team_id = 'team_id_example' # str | 

try:
    # Get Team Preferences.
    api_response = api_instance.get_team_preferences(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**PrefsModel**](PrefsModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_team_member**
> SuccessResponseBodyModel remove_team_member(team_id, user_id)

Remove Member From Team.

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
api_instance = gpyclient.TeamsApi(gpyclient.ApiClient(configuration))
team_id = 'team_id_example' # str | 
user_id = 789 # int | 

try:
    # Remove Member From Team.
    api_response = api_instance.remove_team_member(team_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->remove_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_teams**
> SearchTeamQueryResultModel search_teams(page=page, perpage=perpage, name=name, query=query)

Team Search With Paging.

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
api_instance = gpyclient.TeamsApi(gpyclient.ApiClient(configuration))
page = 1 # int |  (optional) (default to 1)
perpage = 1000 # int | Number of items per page The totalCount field in the response can be used for pagination list E.g. if totalCount is equal to 100 teams and the perpage parameter is set to 10 then there are 10 pages of teams. (optional) (default to 1000)
name = 'name_example' # str |  (optional)
query = 'query_example' # str | If set it will return results where the query value is contained in the name field. Query values with spaces need to be URL encoded. (optional)

try:
    # Team Search With Paging.
    api_response = api_instance.search_teams(page=page, perpage=perpage, name=name, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->search_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **perpage** | **int**| Number of items per page The totalCount field in the response can be used for pagination list E.g. if totalCount is equal to 100 teams and the perpage parameter is set to 10 then there are 10 pages of teams. | [optional] [default to 1000]
 **name** | **str**|  | [optional] 
 **query** | **str**| If set it will return results where the query value is contained in the name field. Query values with spaces need to be URL encoded. | [optional] 

### Return type

[**SearchTeamQueryResultModel**](SearchTeamQueryResultModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> SuccessResponseBodyModel update_team(team_id, body)

Update Team.

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
api_instance = gpyclient.TeamsApi(gpyclient.ApiClient(configuration))
team_id = 'team_id_example' # str | 
body = gpyclient.UpdateTeamCommandModel() # UpdateTeamCommandModel | 

try:
    # Update Team.
    api_response = api_instance.update_team(team_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **body** | [**UpdateTeamCommandModel**](UpdateTeamCommandModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team_member**
> SuccessResponseBodyModel update_team_member(team_id, body, user_id)

Update Team Member.

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
api_instance = gpyclient.TeamsApi(gpyclient.ApiClient(configuration))
team_id = 'team_id_example' # str | 
body = gpyclient.UpdateTeamMemberCommandModel() # UpdateTeamMemberCommandModel | 
user_id = 789 # int | 

try:
    # Update Team Member.
    api_response = api_instance.update_team_member(team_id, body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **body** | [**UpdateTeamMemberCommandModel**](UpdateTeamMemberCommandModel.md)|  | 
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team_preferences**
> SuccessResponseBodyModel update_team_preferences(team_id, body)

Update Team Preferences.

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
api_instance = gpyclient.TeamsApi(gpyclient.ApiClient(configuration))
team_id = 'team_id_example' # str | 
body = gpyclient.UpdatePrefsCmdModel() # UpdatePrefsCmdModel | 

try:
    # Update Team Preferences.
    api_response = api_instance.update_team_preferences(team_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **body** | [**UpdatePrefsCmdModel**](UpdatePrefsCmdModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

