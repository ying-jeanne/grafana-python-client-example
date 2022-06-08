# pythonclient.UsersApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{user_id} | Get user by id.
[**get_user_by_login_or_email**](UsersApi.md#get_user_by_login_or_email) | **GET** /users/lookup | Get user by login or email.
[**get_user_org_list**](UsersApi.md#get_user_org_list) | **GET** /users/{user_id}/orgs | Get organizations for user.
[**get_user_teams**](UsersApi.md#get_user_teams) | **GET** /users/{user_id}/teams | Get teams for user.
[**search_users**](UsersApi.md#search_users) | **GET** /users | Get users.
[**search_users_with_paging**](UsersApi.md#search_users_with_paging) | **GET** /users/search | Get users with paging.
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{user_id} | Update user.


# **get_user_by_id**
> UserProfileDTOModel get_user_by_id(user_id)

Get user by id.

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
api_instance = pythonclient.UsersApi(pythonclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Get user by id.
    api_response = api_instance.get_user_by_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**UserProfileDTOModel**](UserProfileDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_login_or_email**
> UserProfileDTOModel get_user_by_login_or_email(login_or_email)

Get user by login or email.

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
api_instance = pythonclient.UsersApi(pythonclient.ApiClient(configuration))
login_or_email = 'login_or_email_example' # str | loginOrEmail of the user

try:
    # Get user by login or email.
    api_response = api_instance.get_user_by_login_or_email(login_or_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_by_login_or_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_or_email** | **str**| loginOrEmail of the user | 

### Return type

[**UserProfileDTOModel**](UserProfileDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_org_list**
> list[UserOrgDTOModel] get_user_org_list(user_id)

Get organizations for user.

Get organizations for user identified by id.

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
api_instance = pythonclient.UsersApi(pythonclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Get organizations for user.
    api_response = api_instance.get_user_org_list(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_org_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**list[UserOrgDTOModel]**](UserOrgDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_teams**
> list[TeamDTOModel] get_user_teams(user_id)

Get teams for user.

Get teams for user identified by id.

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
api_instance = pythonclient.UsersApi(pythonclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Get teams for user.
    api_response = api_instance.get_user_teams(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**list[TeamDTOModel]**](TeamDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> SearchUserQueryResultModel search_users(perpage=perpage, page=page)

Get users.

Returns all users that the authenticated user has permission to view, admin permission required.

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
api_instance = pythonclient.UsersApi(pythonclient.ApiClient(configuration))
perpage = 1000 # int | Limit the maximum number of users to return per page (optional) (default to 1000)
page = 1 # int | Page index for starting fetching users (optional) (default to 1)

try:
    # Get users.
    api_response = api_instance.search_users(perpage=perpage, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perpage** | **int**| Limit the maximum number of users to return per page | [optional] [default to 1000]
 **page** | **int**| Page index for starting fetching users | [optional] [default to 1]

### Return type

[**SearchUserQueryResultModel**](SearchUserQueryResultModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_with_paging**
> SearchUserQueryResultModel search_users_with_paging()

Get users with paging.

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
api_instance = pythonclient.UsersApi(pythonclient.ApiClient(configuration))

try:
    # Get users with paging.
    api_response = api_instance.search_users_with_paging()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->search_users_with_paging: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SearchUserQueryResultModel**](SearchUserQueryResultModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserProfileDTOModel update_user(user_id, body)

Update user.

Update the user identified by id.

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
api_instance = pythonclient.UsersApi(pythonclient.ApiClient(configuration))
user_id = 789 # int | 
body = pythonclient.UpdateUserCommandModel() # UpdateUserCommandModel | To change the email, name, login, theme, provide another one.

try:
    # Update user.
    api_response = api_instance.update_user(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **body** | [**UpdateUserCommandModel**](UpdateUserCommandModel.md)| To change the email, name, login, theme, provide another one. | 

### Return type

[**UserProfileDTOModel**](UserProfileDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

