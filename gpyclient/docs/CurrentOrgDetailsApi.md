# gpyclient.CurrentOrgDetailsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_org_user**](CurrentOrgDetailsApi.md#add_org_user) | **POST** /org/users | Add a new user to the current organization
[**delete_org_user**](CurrentOrgDetailsApi.md#delete_org_user) | **DELETE** /org/users/{user_id} | Delete user in current organization
[**get_org**](CurrentOrgDetailsApi.md#get_org) | **GET** /org | 
[**get_org_users**](CurrentOrgDetailsApi.md#get_org_users) | **GET** /org/users | Get all users within the current organization.
[**lookup_org_users**](CurrentOrgDetailsApi.md#lookup_org_users) | **GET** /org/users/lookup | Get all users within the current organization (lookup)
[**update_org**](CurrentOrgDetailsApi.md#update_org) | **PUT** /org | Update current Organization.
[**update_org_address**](CurrentOrgDetailsApi.md#update_org_address) | **PUT** /org/address | Update current Organization&#39;s address.
[**update_org_user**](CurrentOrgDetailsApi.md#update_org_user) | **PATCH** /org/users/{user_id} | Updates the given user


# **add_org_user**
> SuccessResponseBodyModel add_org_user(body)

Add a new user to the current organization

Adds a global user to the current organization.  If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `org.users:add` with scope `users:*`.

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
api_instance = gpyclient.CurrentOrgDetailsApi(gpyclient.ApiClient(configuration))
body = gpyclient.AddOrgUserCommandModel() # AddOrgUserCommandModel | 

try:
    # Add a new user to the current organization
    api_response = api_instance.add_org_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentOrgDetailsApi->add_org_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddOrgUserCommandModel**](AddOrgUserCommandModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_org_user**
> SuccessResponseBodyModel delete_org_user(user_id)

Delete user in current organization

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `org.users:remove` with scope `users:*`.

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
api_instance = gpyclient.CurrentOrgDetailsApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Delete user in current organization
    api_response = api_instance.delete_org_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentOrgDetailsApi->delete_org_user: %s\n" % e)
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

# **get_org**
> OrgDetailsDTOModel get_org()



Get current Organization

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
api_instance = gpyclient.CurrentOrgDetailsApi(gpyclient.ApiClient(configuration))

try:
    api_response = api_instance.get_org()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentOrgDetailsApi->get_org: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgDetailsDTOModel**](OrgDetailsDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_users**
> list[OrgUserDTOModel] get_org_users()

Get all users within the current organization.

Returns all org users within the current organization. Accessible to users with org admin role. If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `org.users:read` with scope `users:*`.

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
api_instance = gpyclient.CurrentOrgDetailsApi(gpyclient.ApiClient(configuration))

try:
    # Get all users within the current organization.
    api_response = api_instance.get_org_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentOrgDetailsApi->get_org_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OrgUserDTOModel]**](OrgUserDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_org_users**
> list[UserLookupDTOModel] lookup_org_users(query=query, limit=limit)

Get all users within the current organization (lookup)

Returns all org users within the current organization, but with less detailed information. Accessible to users with org admin role, admin in any folder or admin of any team. Mainly used by Grafana UI for providing list of users when adding team members and when editing folder/dashboard permissions.

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
api_instance = gpyclient.CurrentOrgDetailsApi(gpyclient.ApiClient(configuration))
query = 'query_example' # str |  (optional)
limit = 789 # int |  (optional)

try:
    # Get all users within the current organization (lookup)
    api_response = api_instance.lookup_org_users(query=query, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentOrgDetailsApi->lookup_org_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**list[UserLookupDTOModel]**](UserLookupDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org**
> SuccessResponseBodyModel update_org(body)

Update current Organization.

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
api_instance = gpyclient.CurrentOrgDetailsApi(gpyclient.ApiClient(configuration))
body = gpyclient.UpdateOrgFormModel() # UpdateOrgFormModel | 

try:
    # Update current Organization.
    api_response = api_instance.update_org(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentOrgDetailsApi->update_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrgFormModel**](UpdateOrgFormModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_address**
> SuccessResponseBodyModel update_org_address(body)

Update current Organization's address.

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
api_instance = gpyclient.CurrentOrgDetailsApi(gpyclient.ApiClient(configuration))
body = gpyclient.UpdateOrgAddressFormModel() # UpdateOrgAddressFormModel | 

try:
    # Update current Organization's address.
    api_response = api_instance.update_org_address(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentOrgDetailsApi->update_org_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrgAddressFormModel**](UpdateOrgAddressFormModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_user**
> SuccessResponseBodyModel update_org_user(body, user_id)

Updates the given user

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `org.users.role:update` with scope `users:*`.

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
api_instance = gpyclient.CurrentOrgDetailsApi(gpyclient.ApiClient(configuration))
body = gpyclient.UpdateOrgUserCommandModel() # UpdateOrgUserCommandModel | 
user_id = 789 # int | 

try:
    # Updates the given user
    api_response = api_instance.update_org_user(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentOrgDetailsApi->update_org_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrgUserCommandModel**](UpdateOrgUserCommandModel.md)|  | 
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

