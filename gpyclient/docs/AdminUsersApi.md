# gpyclient.AdminUsersApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](AdminUsersApi.md#create_user) | **POST** /admin/users | Create new user.
[**delete_user**](AdminUsersApi.md#delete_user) | **DELETE** /admin/users/{user_id} | Delete global User.
[**disable_user**](AdminUsersApi.md#disable_user) | **POST** /admin/users/{user_id}/disable | Disable user.
[**enable_user**](AdminUsersApi.md#enable_user) | **POST** /admin/users/{user_id}/enable | Enable user.
[**get_auth_tokens**](AdminUsersApi.md#get_auth_tokens) | **GET** /admin/users/{user_id}/auth-tokens | Return a list of all auth tokens (devices) that the user currently have logged in from.
[**get_user_quota**](AdminUsersApi.md#get_user_quota) | **GET** /admin/users/{user_id}/quotas | Fetch user quota.
[**logout_user**](AdminUsersApi.md#logout_user) | **POST** /admin/users/{user_id}/logout | Logout user revokes all auth tokens (devices) for the user. User of issued auth tokens (devices) will no longer be logged in and will be required to authenticate again upon next activity.
[**revoke_auth_token**](AdminUsersApi.md#revoke_auth_token) | **POST** /admin/users/{user_id}/revoke-auth-token | Revoke auth token for user.
[**set_password**](AdminUsersApi.md#set_password) | **PUT** /admin/users/{user_id}/password | Set password for user.
[**set_permissions**](AdminUsersApi.md#set_permissions) | **PUT** /admin/users/{user_id}/permissions | Set permissions for user.
[**update_user_quota**](AdminUsersApi.md#update_user_quota) | **PUT** /admin/users/{user_id}/quotas/{quota_target} | Update user quota.


# **create_user**
> UserIdDTOModel create_user(body)

Create new user.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users:create`. Note that OrgId is an optional parameter that can be used to assign a new user to a different organization when `auto_assign_org` is set to `true`.

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.AdminUsersApi(gpyclient.ApiClient(configuration))
body = gpyclient.AdminCreateUserFormModel() # AdminCreateUserFormModel | 

try:
    # Create new user.
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminCreateUserFormModel**](AdminCreateUserFormModel.md)|  | 

### Return type

[**UserIdDTOModel**](UserIdDTOModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> SuccessResponseBodyModel delete_user(user_id)

Delete global User.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users:delete` and scope `global.users:*`.

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.AdminUsersApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Delete global User.
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_user**
> SuccessResponseBodyModel disable_user(user_id)

Disable user.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users:disable` and scope `global.users:1` (userIDScope).

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.AdminUsersApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Disable user.
    api_response = api_instance.disable_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->disable_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_user**
> SuccessResponseBodyModel enable_user(user_id)

Enable user.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users:enable` and scope `global.users:1` (userIDScope).

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.AdminUsersApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Enable user.
    api_response = api_instance.enable_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->enable_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_tokens**
> list[UserTokenModel] get_auth_tokens(user_id)

Return a list of all auth tokens (devices) that the user currently have logged in from.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.authtoken:list` and scope `global.users:*`.

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.AdminUsersApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Return a list of all auth tokens (devices) that the user currently have logged in from.
    api_response = api_instance.get_auth_tokens(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->get_auth_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**list[UserTokenModel]**](UserTokenModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_quota**
> list[UserQuotaDTOModel] get_user_quota(user_id)

Fetch user quota.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.quotas:list` and scope `global.users:1` (userIDScope).

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.AdminUsersApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Fetch user quota.
    api_response = api_instance.get_user_quota(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->get_user_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**list[UserQuotaDTOModel]**](UserQuotaDTOModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_user**
> SuccessResponseBodyModel logout_user(user_id)

Logout user revokes all auth tokens (devices) for the user. User of issued auth tokens (devices) will no longer be logged in and will be required to authenticate again upon next activity.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.logout` and scope `global.users:*`.

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.AdminUsersApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Logout user revokes all auth tokens (devices) for the user. User of issued auth tokens (devices) will no longer be logged in and will be required to authenticate again upon next activity.
    api_response = api_instance.logout_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->logout_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_auth_token**
> SuccessResponseBodyModel revoke_auth_token(body, user_id)

Revoke auth token for user.

Revokes the given auth token (device) for the user. User of issued auth token (device) will no longer be logged in and will be required to authenticate again upon next activity. If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.authtoken:update` and scope `global.users:*`.

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.AdminUsersApi(gpyclient.ApiClient(configuration))
body = gpyclient.RevokeAuthTokenCmdModel() # RevokeAuthTokenCmdModel | 
user_id = 789 # int | 

try:
    # Revoke auth token for user.
    api_response = api_instance.revoke_auth_token(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->revoke_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RevokeAuthTokenCmdModel**](RevokeAuthTokenCmdModel.md)|  | 
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_password**
> SuccessResponseBodyModel set_password(body, user_id)

Set password for user.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.password:update` and scope `global.users:*`.

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.AdminUsersApi(gpyclient.ApiClient(configuration))
body = gpyclient.AdminUpdateUserPasswordFormModel() # AdminUpdateUserPasswordFormModel | 
user_id = 789 # int | 

try:
    # Set password for user.
    api_response = api_instance.set_password(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->set_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminUpdateUserPasswordFormModel**](AdminUpdateUserPasswordFormModel.md)|  | 
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_permissions**
> SuccessResponseBodyModel set_permissions(body, user_id)

Set permissions for user.

Only works with Basic Authentication (username and password). See introduction for an explanation. If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.permissions:update` and scope `global.users:*`.

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
api_instance = gpyclient.AdminUsersApi(gpyclient.ApiClient(configuration))
body = gpyclient.AdminUpdateUserPermissionsFormModel() # AdminUpdateUserPermissionsFormModel | 
user_id = 789 # int | 

try:
    # Set permissions for user.
    api_response = api_instance.set_permissions(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->set_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminUpdateUserPermissionsFormModel**](AdminUpdateUserPermissionsFormModel.md)|  | 
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_quota**
> SuccessResponseBodyModel update_user_quota(quota_target, body, user_id)

Update user quota.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.quotas:update` and scope `global.users:1` (userIDScope).

### Example
```python
from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = gpyclient.AdminUsersApi(gpyclient.ApiClient(configuration))
quota_target = 'quota_target_example' # str | 
body = gpyclient.UpdateUserQuotaCmdModel() # UpdateUserQuotaCmdModel | 
user_id = 789 # int | 

try:
    # Update user quota.
    api_response = api_instance.update_user_quota(quota_target, body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->update_user_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_target** | **str**|  | 
 **body** | [**UpdateUserQuotaCmdModel**](UpdateUserQuotaCmdModel.md)|  | 
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

