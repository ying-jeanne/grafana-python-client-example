# pythonclient.AccessControlProvisioningApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_provisioning_reload_access_control**](AccessControlProvisioningApi.md#admin_provisioning_reload_access_control) | **POST** /admin/provisioning/access-control/reload | You need to have a permission with action &#x60;provisioning:reload&#x60; with scope &#x60;provisioners:accesscontrol&#x60;.


# **admin_provisioning_reload_access_control**
> ErrorResponseBodyModel admin_provisioning_reload_access_control()

You need to have a permission with action `provisioning:reload` with scope `provisioners:accesscontrol`.

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
api_instance = pythonclient.AccessControlProvisioningApi(pythonclient.ApiClient(configuration))

try:
    # You need to have a permission with action `provisioning:reload` with scope `provisioners:accesscontrol`.
    api_response = api_instance.admin_provisioning_reload_access_control()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlProvisioningApi->admin_provisioning_reload_access_control: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorResponseBodyModel**](ErrorResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

