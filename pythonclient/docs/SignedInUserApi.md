# pythonclient.SignedInUserApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_user_password**](SignedInUserApi.md#change_user_password) | **PUT** /user/password | Change Password.
[**clear_help_flags**](SignedInUserApi.md#clear_help_flags) | **GET** /user/helpflags/clear | Clear user help flag.
[**get_signed_in_user**](SignedInUserApi.md#get_signed_in_user) | **GET** /user | Get signed in User.
[**get_signed_in_user_auth_tokens**](SignedInUserApi.md#get_signed_in_user_auth_tokens) | **GET** /user/auth-tokens | Auth tokens of the actual User.
[**get_signed_in_user_org_list**](SignedInUserApi.md#get_signed_in_user_org_list) | **GET** /user/orgs | Organizations of the actual User.
[**get_signed_in_user_team_list**](SignedInUserApi.md#get_signed_in_user_team_list) | **GET** /user/teams | Teams that the actual User is member of.
[**get_user_quotas**](SignedInUserApi.md#get_user_quotas) | **GET** /user/quotas | Fetch user quota.
[**revoke_signed_in_auth_token_cmd**](SignedInUserApi.md#revoke_signed_in_auth_token_cmd) | **POST** /user/revoke-auth-token | Revoke an auth token of the actual User.
[**set_help_flag**](SignedInUserApi.md#set_help_flag) | **PUT** /user/helpflags/{flag_id} | Set user help flag.
[**star_dashboard**](SignedInUserApi.md#star_dashboard) | **POST** /user/stars/dashboard/{dashboard_id} | Star a dashboard.
[**unstar_dashboard**](SignedInUserApi.md#unstar_dashboard) | **DELETE** /user/stars/dashboard/{dashboard_id} | Unstar a dashboard.
[**update_signed_in_user**](SignedInUserApi.md#update_signed_in_user) | **PUT** /user | Update signed in User.
[**user_set_using_org**](SignedInUserApi.md#user_set_using_org) | **POST** /user/using/{org_id} | Switch user context for signed in user.


# **change_user_password**
> SuccessResponseBodyModel change_user_password(body)

Change Password.

Changes the password for the user.

### Example
```python
from __future__ import print_function
import time
import pythonclient
from pythonclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = pythonclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))
body = pythonclient.ChangeUserPasswordCommandModel() # ChangeUserPasswordCommandModel | To change the email, name, login, theme, provide another one.

try:
    # Change Password.
    api_response = api_instance.change_user_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->change_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeUserPasswordCommandModel**](ChangeUserPasswordCommandModel.md)| To change the email, name, login, theme, provide another one. | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_help_flags**
> InlineResponse20016Model clear_help_flags()

Clear user help flag.

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
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))

try:
    # Clear user help flag.
    api_response = api_instance.clear_help_flags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->clear_help_flags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20016Model**](InlineResponse20016Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signed_in_user**
> UserProfileDTOModel get_signed_in_user()

Get signed in User.

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
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))

try:
    # Get signed in User.
    api_response = api_instance.get_signed_in_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->get_signed_in_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProfileDTOModel**](UserProfileDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signed_in_user_auth_tokens**
> list[UserTokenModel] get_signed_in_user_auth_tokens()

Auth tokens of the actual User.

Return a list of all auth tokens (devices) that the actual user currently have logged in from.

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
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))

try:
    # Auth tokens of the actual User.
    api_response = api_instance.get_signed_in_user_auth_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->get_signed_in_user_auth_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserTokenModel]**](UserTokenModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signed_in_user_org_list**
> list[UserOrgDTOModel] get_signed_in_user_org_list()

Organizations of the actual User.

Return a list of all organizations of the current user.

### Example
```python
from __future__ import print_function
import time
import pythonclient
from pythonclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = pythonclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))

try:
    # Organizations of the actual User.
    api_response = api_instance.get_signed_in_user_org_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->get_signed_in_user_org_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserOrgDTOModel]**](UserOrgDTOModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signed_in_user_team_list**
> list[UserOrgDTOModel] get_signed_in_user_team_list()

Teams that the actual User is member of.

Return a list of all teams that the current user is member of.

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
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))

try:
    # Teams that the actual User is member of.
    api_response = api_instance.get_signed_in_user_team_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->get_signed_in_user_team_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserOrgDTOModel]**](UserOrgDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_quotas**
> list[UserQuotaDTOModel] get_user_quotas()

Fetch user quota.

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
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))

try:
    # Fetch user quota.
    api_response = api_instance.get_user_quotas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->get_user_quotas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserQuotaDTOModel]**](UserQuotaDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_signed_in_auth_token_cmd**
> SuccessResponseBodyModel revoke_signed_in_auth_token_cmd(body)

Revoke an auth token of the actual User.

Revokes the given auth token (device) for the actual user. User of issued auth token (device) will no longer be logged in and will be required to authenticate again upon next activity.

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
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))
body = pythonclient.RevokeAuthTokenCmdModel() # RevokeAuthTokenCmdModel | 

try:
    # Revoke an auth token of the actual User.
    api_response = api_instance.revoke_signed_in_auth_token_cmd(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->revoke_signed_in_auth_token_cmd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RevokeAuthTokenCmdModel**](RevokeAuthTokenCmdModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_help_flag**
> InlineResponse20016Model set_help_flag(flag_id)

Set user help flag.

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
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))
flag_id = 'flag_id_example' # str | 

try:
    # Set user help flag.
    api_response = api_instance.set_help_flag(flag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->set_help_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **str**|  | 

### Return type

[**InlineResponse20016Model**](InlineResponse20016Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **star_dashboard**
> SuccessResponseBodyModel star_dashboard(dashboard_id)

Star a dashboard.

Stars the given Dashboard for the actual user.

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
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | 

try:
    # Star a dashboard.
    api_response = api_instance.star_dashboard(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->star_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unstar_dashboard**
> SuccessResponseBodyModel unstar_dashboard(dashboard_id)

Unstar a dashboard.

Deletes the starring of the given Dashboard for the actual user.

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
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | 

try:
    # Unstar a dashboard.
    api_response = api_instance.unstar_dashboard(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->unstar_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_signed_in_user**
> UserProfileDTOModel update_signed_in_user(body)

Update signed in User.

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
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))
body = pythonclient.UpdateUserCommandModel() # UpdateUserCommandModel | To change the email, name, login, theme, provide another one.

try:
    # Update signed in User.
    api_response = api_instance.update_signed_in_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->update_signed_in_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserCommandModel**](UpdateUserCommandModel.md)| To change the email, name, login, theme, provide another one. | 

### Return type

[**UserProfileDTOModel**](UserProfileDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_set_using_org**
> SuccessResponseBodyModel user_set_using_org(org_id)

Switch user context for signed in user.

Switch user context to the given organization.

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
api_instance = pythonclient.SignedInUserApi(pythonclient.ApiClient(configuration))
org_id = 789 # int | 

try:
    # Switch user context for signed in user.
    api_response = api_instance.user_set_using_org(org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignedInUserApi->user_set_using_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

