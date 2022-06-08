# gpyclient.AdminLdapApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ldap_status**](AdminLdapApi.md#get_ldap_status) | **GET** /admin/ldap/status | Attempts to connect to all the configured LDAP servers and returns information on whenever they&#39;re available or not.
[**get_ldap_user**](AdminLdapApi.md#get_ldap_user) | **GET** /admin/ldap/{user_name} | Finds an user based on a username in LDAP. This helps illustrate how would the particular user be mapped in Grafana when synced.
[**reload_ldap**](AdminLdapApi.md#reload_ldap) | **POST** /admin/ldap/reload | Reloads the LDAP configuration.
[**sync_ldap_user**](AdminLdapApi.md#sync_ldap_user) | **POST** /admin/ldap/sync/{user_id} | Enables a single Grafana user to be synchronized against LDAP.


# **get_ldap_status**
> SuccessResponseBodyModel get_ldap_status()

Attempts to connect to all the configured LDAP servers and returns information on whenever they're available or not.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `ldap.status:read`.

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
api_instance = gpyclient.AdminLdapApi(gpyclient.ApiClient(configuration))

try:
    # Attempts to connect to all the configured LDAP servers and returns information on whenever they're available or not.
    api_response = api_instance.get_ldap_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminLdapApi->get_ldap_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ldap_user**
> SuccessResponseBodyModel get_ldap_user(user_name)

Finds an user based on a username in LDAP. This helps illustrate how would the particular user be mapped in Grafana when synced.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `ldap.user:read`.

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
api_instance = gpyclient.AdminLdapApi(gpyclient.ApiClient(configuration))
user_name = 'user_name_example' # str | 

try:
    # Finds an user based on a username in LDAP. This helps illustrate how would the particular user be mapped in Grafana when synced.
    api_response = api_instance.get_ldap_user(user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminLdapApi->get_ldap_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_ldap**
> SuccessResponseBodyModel reload_ldap()

Reloads the LDAP configuration.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `ldap.config:reload`.

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
api_instance = gpyclient.AdminLdapApi(gpyclient.ApiClient(configuration))

try:
    # Reloads the LDAP configuration.
    api_response = api_instance.reload_ldap()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminLdapApi->reload_ldap: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_ldap_user**
> SuccessResponseBodyModel sync_ldap_user(user_id)

Enables a single Grafana user to be synchronized against LDAP.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `ldap.user:sync`.

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
api_instance = gpyclient.AdminLdapApi(gpyclient.ApiClient(configuration))
user_id = 789 # int | 

try:
    # Enables a single Grafana user to be synchronized against LDAP.
    api_response = api_instance.sync_ldap_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminLdapApi->sync_ldap_user: %s\n" % e)
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

