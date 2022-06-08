# gpyclient.OrgsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_add_org_user**](OrgsApi.md#admin_add_org_user) | **POST** /orgs/{org_id}/users | Add a new user to the current organization
[**admin_delete_org**](OrgsApi.md#admin_delete_org) | **DELETE** /orgs/{org_id} | Delete Organization.
[**admin_delete_org_user**](OrgsApi.md#admin_delete_org_user) | **DELETE** /orgs/{org_id}/users/{user_id} | Delete user in current organization
[**admin_get_org_users**](OrgsApi.md#admin_get_org_users) | **GET** /orgs/{org_id}/users | Get Users in Organization.
[**admin_update_org**](OrgsApi.md#admin_update_org) | **PUT** /orgs/{org_id} | Update Organization.
[**admin_update_org_address**](OrgsApi.md#admin_update_org_address) | **PUT** /orgs/{org_id}/address | Update Organization&#39;s address.
[**admin_update_org_user**](OrgsApi.md#admin_update_org_user) | **PATCH** /orgs/{org_id}/users/{user_id} | Update Users in Organization.
[**create_org**](OrgsApi.md#create_org) | **POST** /orgs | Create Organization.
[**get_org_by_id**](OrgsApi.md#get_org_by_id) | **GET** /orgs/{org_id} | Get Organization by ID.
[**get_org_by_name**](OrgsApi.md#get_org_by_name) | **GET** /orgs/name/{org_name} | Get Organization by ID.
[**get_org_quota**](OrgsApi.md#get_org_quota) | **GET** /orgs/{org_id}/quotas | Fetch Organization quota.
[**search_org**](OrgsApi.md#search_org) | **GET** /orgs | 
[**update_org_quota**](OrgsApi.md#update_org_quota) | **PUT** /orgs/{org_id}/quotas/{quota_target} | Update user quota.


# **admin_add_org_user**
> SuccessResponseBodyModel admin_add_org_user(body, org_id)

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
body = gpyclient.AddOrgUserCommandModel() # AddOrgUserCommandModel | 
org_id = 789 # int | 

try:
    # Add a new user to the current organization
    api_response = api_instance.admin_add_org_user(body, org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->admin_add_org_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddOrgUserCommandModel**](AddOrgUserCommandModel.md)|  | 
 **org_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_org**
> SuccessResponseBodyModel admin_delete_org(org_id)

Delete Organization.

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
org_id = 789 # int | 

try:
    # Delete Organization.
    api_response = api_instance.admin_delete_org(org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->admin_delete_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_org_user**
> SuccessResponseBodyModel admin_delete_org_user(org_id, user_id)

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
org_id = 789 # int | 
user_id = 789 # int | 

try:
    # Delete user in current organization
    api_response = api_instance.admin_delete_org_user(org_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->admin_delete_org_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_org_users**
> list[OrgUserDTOModel] admin_get_org_users(org_id)

Get Users in Organization.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `org.users:read` with scope `users:*`.

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
org_id = 789 # int | 

try:
    # Get Users in Organization.
    api_response = api_instance.admin_get_org_users(org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->admin_get_org_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 

### Return type

[**list[OrgUserDTOModel]**](OrgUserDTOModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_org**
> SuccessResponseBodyModel admin_update_org(body, org_id)

Update Organization.

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
body = gpyclient.UpdateOrgFormModel() # UpdateOrgFormModel | 
org_id = 789 # int | 

try:
    # Update Organization.
    api_response = api_instance.admin_update_org(body, org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->admin_update_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrgFormModel**](UpdateOrgFormModel.md)|  | 
 **org_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_org_address**
> SuccessResponseBodyModel admin_update_org_address(body, org_id)

Update Organization's address.

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
body = gpyclient.UpdateOrgAddressFormModel() # UpdateOrgAddressFormModel | 
org_id = 789 # int | 

try:
    # Update Organization's address.
    api_response = api_instance.admin_update_org_address(body, org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->admin_update_org_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrgAddressFormModel**](UpdateOrgAddressFormModel.md)|  | 
 **org_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_org_user**
> SuccessResponseBodyModel admin_update_org_user(body, org_id, user_id)

Update Users in Organization.

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
body = gpyclient.UpdateOrgUserCommandModel() # UpdateOrgUserCommandModel | 
org_id = 789 # int | 
user_id = 789 # int | 

try:
    # Update Users in Organization.
    api_response = api_instance.admin_update_org_user(body, org_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->admin_update_org_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrgUserCommandModel**](UpdateOrgUserCommandModel.md)|  | 
 **org_id** | **int**|  | 
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_org**
> InlineResponse20011Model create_org(body)

Create Organization.

Only works if [users.allow_org_create](https://grafana.com/docs/grafana/latest/administration/configuration/#allow_org_create) is set.

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
body = gpyclient.CreateOrgCommandModel() # CreateOrgCommandModel | 

try:
    # Create Organization.
    api_response = api_instance.create_org(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->create_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrgCommandModel**](CreateOrgCommandModel.md)|  | 

### Return type

[**InlineResponse20011Model**](InlineResponse20011Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_by_id**
> OrgDetailsDTOModel get_org_by_id(org_id)

Get Organization by ID.

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
org_id = 789 # int | 

try:
    # Get Organization by ID.
    api_response = api_instance.get_org_by_id(org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->get_org_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 

### Return type

[**OrgDetailsDTOModel**](OrgDetailsDTOModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_by_name**
> OrgDetailsDTOModel get_org_by_name(org_name)

Get Organization by ID.

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
org_name = 'org_name_example' # str | 

try:
    # Get Organization by ID.
    api_response = api_instance.get_org_by_name(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->get_org_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**|  | 

### Return type

[**OrgDetailsDTOModel**](OrgDetailsDTOModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_quota**
> list[UserQuotaDTOModel] get_org_quota(org_id)

Fetch Organization quota.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `orgs.quotas:read` and scope `org:id:1` (orgIDScope). list

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
org_id = 789 # int | 

try:
    # Fetch Organization quota.
    api_response = api_instance.get_org_quota(org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->get_org_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 

### Return type

[**list[UserQuotaDTOModel]**](UserQuotaDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_org**
> list[OrgDTOModel] search_org(page=page, perpage=perpage, name=name, query=query)



Search all Organizations

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
page = 1 # int |  (optional) (default to 1)
perpage = 1000 # int | Number of items per page The totalCount field in the response can be used for pagination list E.g. if totalCount is equal to 100 teams and the perpage parameter is set to 10 then there are 10 pages of teams. (optional) (default to 1000)
name = 'name_example' # str |  (optional)
query = 'query_example' # str | If set it will return results where the query value is contained in the name field. Query values with spaces need to be URL encoded. (optional)

try:
    api_response = api_instance.search_org(page=page, perpage=perpage, name=name, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->search_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **perpage** | **int**| Number of items per page The totalCount field in the response can be used for pagination list E.g. if totalCount is equal to 100 teams and the perpage parameter is set to 10 then there are 10 pages of teams. | [optional] [default to 1000]
 **name** | **str**|  | [optional] 
 **query** | **str**| If set it will return results where the query value is contained in the name field. Query values with spaces need to be URL encoded. | [optional] 

### Return type

[**list[OrgDTOModel]**](OrgDTOModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_quota**
> SuccessResponseBodyModel update_org_quota(quota_target, org_id, body)

Update user quota.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `orgs.quotas:write` and scope `org:id:1` (orgIDScope).

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
api_instance = gpyclient.OrgsApi(gpyclient.ApiClient(configuration))
quota_target = 'quota_target_example' # str | 
org_id = 789 # int | 
body = gpyclient.UpdateOrgQuotaCmdModel() # UpdateOrgQuotaCmdModel | 

try:
    # Update user quota.
    api_response = api_instance.update_org_quota(quota_target, org_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->update_org_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_target** | **str**|  | 
 **org_id** | **int**|  | 
 **body** | [**UpdateOrgQuotaCmdModel**](UpdateOrgQuotaCmdModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

