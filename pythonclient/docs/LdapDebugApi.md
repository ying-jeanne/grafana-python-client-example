# pythonclient.LdapDebugApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ldap_sync_status**](LdapDebugApi.md#get_ldap_sync_status) | **GET** /admin/ldap-sync-status | Available to grafana admins.


# **get_ldap_sync_status**
> ActiveSyncStatusDTOModel get_ldap_sync_status()

Available to grafana admins.

You need to have a permission with action `ldap.status:read`.

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
api_instance = pythonclient.LdapDebugApi(pythonclient.ApiClient(configuration))

try:
    # Available to grafana admins.
    api_response = api_instance.get_ldap_sync_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LdapDebugApi->get_ldap_sync_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ActiveSyncStatusDTOModel**](ActiveSyncStatusDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

