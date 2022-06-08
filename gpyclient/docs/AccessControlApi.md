# gpyclient.AccessControlApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_builtin_role**](AccessControlApi.md#add_builtin_role) | **POST** /access-control/builtin-roles | Create a built-in role assignment.
[**add_team_role**](AccessControlApi.md#add_team_role) | **POST** /access-control/teams/{teamId}/roles | Add team role.
[**add_user_role**](AccessControlApi.md#add_user_role) | **POST** /access-control/users/{user_id}/roles | Add a user role assignment.
[**create_role_with_permissions**](AccessControlApi.md#create_role_with_permissions) | **POST** /access-control/roles | Create a new custom role.
[**delete_custom_role**](AccessControlApi.md#delete_custom_role) | **DELETE** /access-control/roles/{roleUID} | Delete a custom role.
[**get_access_control_status**](AccessControlApi.md#get_access_control_status) | **GET** /access-control/status | Get status.
[**get_all_roles**](AccessControlApi.md#get_all_roles) | **GET** /access-control/roles | Get all roles.
[**get_role**](AccessControlApi.md#get_role) | **GET** /access-control/roles/{roleUID} | Get a role.
[**list_builtin_roles**](AccessControlApi.md#list_builtin_roles) | **GET** /access-control/builtin-roles | Get all built-in role assignments.
[**list_team_roles**](AccessControlApi.md#list_team_roles) | **GET** /access-control/teams/{teamId}/roles | Get team roles.
[**list_user_roles**](AccessControlApi.md#list_user_roles) | **GET** /access-control/users/{user_id}/roles | List roles assigned to a user.
[**remove_builtin_role**](AccessControlApi.md#remove_builtin_role) | **DELETE** /access-control/builtin-roles/{builtinRole}/roles/{roleUID} | Remove a built-in role assignment.
[**remove_team_role**](AccessControlApi.md#remove_team_role) | **DELETE** /access-control/teams/{teamId}/roles/{roleUID} | Remove team role.
[**remove_user_role**](AccessControlApi.md#remove_user_role) | **DELETE** /access-control/users/{user_id}/roles/{roleUID} | Remove a user role assignment.
[**set_team_roles**](AccessControlApi.md#set_team_roles) | **PUT** /access-control/teams/{teamId}/roles | Update team role.
[**set_user_roles**](AccessControlApi.md#set_user_roles) | **PUT** /access-control/users/{user_id}/roles | Set user role assignments.
[**update_role_with_permissions**](AccessControlApi.md#update_role_with_permissions) | **PUT** /access-control/roles/{roleUID} | Update a custom role.


# **add_builtin_role**
> SuccessResponseBodyModel add_builtin_role(body)

Create a built-in role assignment.

You need to have a permission with action `roles.builtin:add` and scope `permissions:type:delegate`. `permissions:type:delegate` scope ensures that users can only create built-in role assignments with the roles which have same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to create a built-in role assignment which will allow to do that. This is done to prevent escalation of privileges.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
body = gpyclient.AddBuiltInRoleCommandModel() # AddBuiltInRoleCommandModel | 

try:
    # Create a built-in role assignment.
    api_response = api_instance.add_builtin_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->add_builtin_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddBuiltInRoleCommandModel**](AddBuiltInRoleCommandModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_team_role**
> SuccessResponseBodyModel add_team_role(team_id, body)

Add team role.

You need to have a permission with action `teams.roles:add` and scope `permissions:type:delegate`.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
team_id = 789 # int | 
body = gpyclient.AddTeamRoleCommandModel() # AddTeamRoleCommandModel | 

try:
    # Add team role.
    api_response = api_instance.add_team_role(team_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->add_team_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | 
 **body** | [**AddTeamRoleCommandModel**](AddTeamRoleCommandModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_role**
> SuccessResponseBodyModel add_user_role(user_id, body)

Add a user role assignment.

Assign a role to a specific user. For bulk updates consider Set user role assignments.  You need to have a permission with action `users.roles:add` and scope `permissions:type:delegate`. `permissions:type:delegate` scope ensures that users can only assign roles which have same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to assign a role which will allow to do that. This is done to prevent escalation of privileges.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 
body = gpyclient.AddUserRoleCommandModel() # AddUserRoleCommandModel | 

try:
    # Add a user role assignment.
    api_response = api_instance.add_user_role(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->add_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **body** | [**AddUserRoleCommandModel**](AddUserRoleCommandModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role_with_permissions**
> RoleDTOModel create_role_with_permissions(body)

Create a new custom role.

Creates a new custom role and maps given permissions to that role. Note that roles with the same prefix as Fixed Roles can’t be created.  You need to have a permission with action `roles:write` and scope `permissions:type:delegate`. `permissions:type:delegate`` scope ensures that users can only create custom roles with the same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to create a custom role which allows to do that. This is done to prevent escalation of privileges.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
body = gpyclient.SetUserRolesCommandModel() # SetUserRolesCommandModel | 

try:
    # Create a new custom role.
    api_response = api_instance.create_role_with_permissions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->create_role_with_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetUserRolesCommandModel**](SetUserRolesCommandModel.md)|  | 

### Return type

[**RoleDTOModel**](RoleDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_role**
> SuccessResponseBodyModel delete_custom_role(role_uid)

Delete a custom role.

Delete a role with the given UID, and it’s permissions. If the role is assigned to a built-in role, the deletion operation will fail, unless force query param is set to true, and in that case all assignments will also be deleted.  You need to have a permission with action `roles:delete` and scope `permissions:type:delegate`. `permissions:type:delegate` scope ensures that users can only delete a custom role with the same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to delete a custom role which allows to do that.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
role_uid = 'role_uid_example' # str | 

try:
    # Delete a custom role.
    api_response = api_instance.delete_custom_role(role_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->delete_custom_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_control_status**
> StatusModel get_access_control_status()

Get status.

Returns an indicator to check if fine-grained access control is enabled or not.  You need to have a permission with action `status:accesscontrol` and scope `services:accesscontrol`.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))

try:
    # Get status.
    api_response = api_instance.get_access_control_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->get_access_control_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusModel**](StatusModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles**
> list[RoleDTOModel] get_all_roles()

Get all roles.

Gets all existing roles. The response contains all global and organization local roles, for the organization which user is signed in.  You need to have a permission with action `roles:list` and scope `roles:*`.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))

try:
    # Get all roles.
    api_response = api_instance.get_all_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->get_all_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RoleDTOModel]**](RoleDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleDTOModel get_role(role_uid)

Get a role.

Get a role for the given UID.  You need to have a permission with action `roles:read` and scope `roles:*`.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
role_uid = 'role_uid_example' # str | 

try:
    # Get a role.
    api_response = api_instance.get_role(role_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 

### Return type

[**RoleDTOModel**](RoleDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_builtin_roles**
> dict(str, list[RoleDTOModel]) list_builtin_roles()

Get all built-in role assignments.

You need to have a permission with action `roles.builtin:list` with scope `roles:*`.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))

try:
    # Get all built-in role assignments.
    api_response = api_instance.list_builtin_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->list_builtin_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, list[RoleDTOModel])**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_roles**
> SuccessResponseBodyModel list_team_roles(team_id)

Get team roles.

You need to have a permission with action `teams.roles:list` and scope `teams:id:<team ID>`.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
team_id = 789 # int | 

try:
    # Get team roles.
    api_response = api_instance.list_team_roles(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->list_team_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_roles**
> list[RoleDTOModel] list_user_roles(user_id)

List roles assigned to a user.

Lists the roles that have been directly assigned to a given user. The list does not include built-in roles (Viewer, Editor, Admin or Grafana Admin), and it does not include roles that have been inherited from a team.  You need to have a permission with action `users.roles:list` and scope `users:id:<user ID>`.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # List roles assigned to a user.
    api_response = api_instance.list_user_roles(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->list_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**list[RoleDTOModel]**](RoleDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_builtin_role**
> SuccessResponseBodyModel remove_builtin_role(role_uid, builtin_role, _global=_global)

Remove a built-in role assignment.

Deletes a built-in role assignment (for one of Viewer, Editor, Admin, or Grafana Admin) to the role with the provided UID.  You need to have a permission with action `roles.builtin:remove` and scope `permissions:type:delegate`. `permissions:type:delegate` scope ensures that users can only remove built-in role assignments with the roles which have same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to remove a built-in role assignment which allows to do that.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
role_uid = 'role_uid_example' # str | 
builtin_role = 'builtin_role_example' # str | 
_global = true # bool | A flag indicating if the assignment is global or not. If set to false, the default org ID of the authenticated user will be used from the request to remove assignment. (optional)

try:
    # Remove a built-in role assignment.
    api_response = api_instance.remove_builtin_role(role_uid, builtin_role, _global=_global)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->remove_builtin_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 
 **builtin_role** | **str**|  | 
 **_global** | **bool**| A flag indicating if the assignment is global or not. If set to false, the default org ID of the authenticated user will be used from the request to remove assignment. | [optional] 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_team_role**
> SuccessResponseBodyModel remove_team_role(role_uid, team_id)

Remove team role.

You need to have a permission with action `teams.roles:remove` and scope `permissions:type:delegate`.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
role_uid = 'role_uid_example' # str | 
team_id = 789 # int | 

try:
    # Remove team role.
    api_response = api_instance.remove_team_role(role_uid, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->remove_team_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 
 **team_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_role**
> SuccessResponseBodyModel remove_user_role(user_id, role_uid, _global=_global)

Remove a user role assignment.

Revoke a role from a user. For bulk updates consider Set user role assignments.  You need to have a permission with action `users.roles:remove` and scope `permissions:type:delegate`. `permissions:type:delegate` scope ensures that users can only unassign roles which have same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to unassign a role which will allow to do that. This is done to prevent escalation of privileges.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 
role_uid = 'role_uid_example' # str | 
_global = true # bool | A flag indicating if the assignment is global or not. If set to false, the default org ID of the authenticated user will be used from the request to remove assignment. (optional)

try:
    # Remove a user role assignment.
    api_response = api_instance.remove_user_role(user_id, role_uid, _global=_global)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->remove_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **role_uid** | **str**|  | 
 **_global** | **bool**| A flag indicating if the assignment is global or not. If set to false, the default org ID of the authenticated user will be used from the request to remove assignment. | [optional] 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_team_roles**
> SuccessResponseBodyModel set_team_roles(team_id)

Update team role.

You need to have a permission with action `teams.roles:add` and `teams.roles:remove` and scope `permissions:type:delegate` for each.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
team_id = 789 # int | 

try:
    # Update team role.
    api_response = api_instance.set_team_roles(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->set_team_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_roles**
> SuccessResponseBodyModel set_user_roles(user_id)

Set user role assignments.

Update the user’s role assignments to match the provided set of UIDs. This will remove any assigned roles that aren’t in the request and add roles that are in the set but are not already assigned to the user. If you want to add or remove a single role, consider using Add a user role assignment or Remove a user role assignment instead.  You need to have a permission with action `users.roles:add` and `users.roles:remove` and scope `permissions:type:delegate` for each. `permissions:type:delegate`  scope ensures that users can only assign or unassign roles which have same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to assign or unassign a role which will allow to do that. This is done to prevent escalation of privileges.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Set user role assignments.
    api_response = api_instance.set_user_roles(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->set_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_with_permissions**
> RoleDTOModel update_role_with_permissions(role_uid, body)

Update a custom role.

You need to have a permission with action `roles:write` and scope `permissions:type:delegate`. `permissions:type:delegate`` scope ensures that users can only create custom roles with the same, or a subset of permissions which the user has.

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
api_instance = gpyclient.AccessControlApi(gpyclient.ApiClient(configuration))
role_uid = 'role_uid_example' # str | 
body = gpyclient.UpdateRoleCommandModel() # UpdateRoleCommandModel | 

try:
    # Update a custom role.
    api_response = api_instance.update_role_with_permissions(role_uid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->update_role_with_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 
 **body** | [**UpdateRoleCommandModel**](UpdateRoleCommandModel.md)|  | 

### Return type

[**RoleDTOModel**](RoleDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

