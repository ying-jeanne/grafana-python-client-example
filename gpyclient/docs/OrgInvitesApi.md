# gpyclient.OrgInvitesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_invite**](OrgInvitesApi.md#add_invite) | **POST** /org/invites | Add invite.
[**get_invites**](OrgInvitesApi.md#get_invites) | **GET** /org/invites | Get pending invites.
[**revoke_invite**](OrgInvitesApi.md#revoke_invite) | **DELETE** /org/{invitation_code}/invites | Revoke invite.


# **add_invite**
> InlineResponse20010Model add_invite(body)

Add invite.

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
api_instance = gpyclient.OrgInvitesApi(gpyclient.ApiClient(configuration))
body = gpyclient.AddInviteFormModel() # AddInviteFormModel | 

try:
    # Add invite.
    api_response = api_instance.add_invite(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgInvitesApi->add_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddInviteFormModel**](AddInviteFormModel.md)|  | 

### Return type

[**InlineResponse20010Model**](InlineResponse20010Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invites**
> list[TempUserDTOModel] get_invites()

Get pending invites.

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
api_instance = gpyclient.OrgInvitesApi(gpyclient.ApiClient(configuration))

try:
    # Get pending invites.
    api_response = api_instance.get_invites()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgInvitesApi->get_invites: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TempUserDTOModel]**](TempUserDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_invite**
> SuccessResponseBodyModel revoke_invite(invitation_code)

Revoke invite.

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
api_instance = gpyclient.OrgInvitesApi(gpyclient.ApiClient(configuration))
invitation_code = 'invitation_code_example' # str | 

try:
    # Revoke invite.
    api_response = api_instance.revoke_invite(invitation_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgInvitesApi->revoke_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_code** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

