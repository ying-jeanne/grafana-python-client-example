# gpyclient.SamlApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_saml_login**](SamlApi.md#get_saml_login) | **GET** /login/saml | It initiates the login flow by redirecting the user to the IdP.
[**get_saml_logout**](SamlApi.md#get_saml_logout) | **GET** /logout/saml | GetLogout initiates single logout process.
[**get_saml_metadata**](SamlApi.md#get_saml_metadata) | **GET** /saml/metadata | It exposes the SP (Grafana&#39;s) metadata for the IdP&#39;s consumption.
[**post_acs**](SamlApi.md#post_acs) | **POST** /saml/acs | It performs assertion Consumer Service (ACS).
[**post_slo**](SamlApi.md#post_slo) | **POST** /saml/slo | It performs Single Logout (SLO) callback.


# **get_saml_login**
> get_saml_login()

It initiates the login flow by redirecting the user to the IdP.

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
api_instance = gpyclient.SamlApi(gpyclient.ApiClient(configuration))

try:
    # It initiates the login flow by redirecting the user to the IdP.
    api_instance.get_saml_login()
except ApiException as e:
    print("Exception when calling SamlApi->get_saml_login: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_logout**
> get_saml_logout()

GetLogout initiates single logout process.

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
api_instance = gpyclient.SamlApi(gpyclient.ApiClient(configuration))

try:
    # GetLogout initiates single logout process.
    api_instance.get_saml_logout()
except ApiException as e:
    print("Exception when calling SamlApi->get_saml_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_metadata**
> list[int] get_saml_metadata()

It exposes the SP (Grafana's) metadata for the IdP's consumption.

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
api_instance = gpyclient.SamlApi(gpyclient.ApiClient(configuration))

try:
    # It exposes the SP (Grafana's) metadata for the IdP's consumption.
    api_response = api_instance.get_saml_metadata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamlApi->get_saml_metadata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[int]**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/xml;application/samlmetadata+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_acs**
> post_acs(relay_state=relay_state)

It performs assertion Consumer Service (ACS).

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
api_instance = gpyclient.SamlApi(gpyclient.ApiClient(configuration))
relay_state = 'relay_state_example' # str |  (optional)

try:
    # It performs assertion Consumer Service (ACS).
    api_instance.post_acs(relay_state=relay_state)
except ApiException as e:
    print("Exception when calling SamlApi->post_acs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_state** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_slo**
> post_slo(saml_request=saml_request, saml_response=saml_response)

It performs Single Logout (SLO) callback.

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
api_instance = gpyclient.SamlApi(gpyclient.ApiClient(configuration))
saml_request = 'saml_request_example' # str |  (optional)
saml_response = 'saml_response_example' # str |  (optional)

try:
    # It performs Single Logout (SLO) callback.
    api_instance.post_slo(saml_request=saml_request, saml_response=saml_response)
except ApiException as e:
    print("Exception when calling SamlApi->post_slo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_request** | **str**|  | [optional] 
 **saml_response** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

