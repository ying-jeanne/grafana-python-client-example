# pythonclient.RecordingRulesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recording_rule**](RecordingRulesApi.md#create_recording_rule) | **POST** /recording-rules | Create a new recording rule.
[**create_recording_rule_write_target**](RecordingRulesApi.md#create_recording_rule_write_target) | **POST** /recording-rules/writer | Create a new write target.
[**delete_recording_rule**](RecordingRulesApi.md#delete_recording_rule) | **DELETE** /recording-rules/{recordingRuleID} | Delete a recording rule.
[**delete_recording_rule_write_target**](RecordingRulesApi.md#delete_recording_rule_write_target) | **DELETE** /recording-rules/writer | Delete the write target.
[**get_recording_rule_write_target**](RecordingRulesApi.md#get_recording_rule_write_target) | **GET** /recording-rules/writer | Get the write target.
[**list_recording_rules**](RecordingRulesApi.md#list_recording_rules) | **GET** /recording-rules | Get all recording rules.
[**test_create_recording_rule**](RecordingRulesApi.md#test_create_recording_rule) | **POST** /recording-rules/test | Test a recording rule.
[**update_recording_rule**](RecordingRulesApi.md#update_recording_rule) | **PUT** /recording-rules | Update a recording rule.


# **create_recording_rule**
> RecordingRuleJSONModel create_recording_rule(body)

Create a new recording rule.

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
api_instance = pythonclient.RecordingRulesApi(pythonclient.ApiClient(configuration))
body = pythonclient.RecordingRuleJSONModel() # RecordingRuleJSONModel | 

try:
    # Create a new recording rule.
    api_response = api_instance.create_recording_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingRulesApi->create_recording_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordingRuleJSONModel**](RecordingRuleJSONModel.md)|  | 

### Return type

[**RecordingRuleJSONModel**](RecordingRuleJSONModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recording_rule_write_target**
> PrometheusRemoteWriteTargetJSONModel create_recording_rule_write_target(body)

Create a new write target.

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
api_instance = pythonclient.RecordingRulesApi(pythonclient.ApiClient(configuration))
body = pythonclient.PrometheusRemoteWriteTargetJSONModel() # PrometheusRemoteWriteTargetJSONModel | 

try:
    # Create a new write target.
    api_response = api_instance.create_recording_rule_write_target(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingRulesApi->create_recording_rule_write_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrometheusRemoteWriteTargetJSONModel**](PrometheusRemoteWriteTargetJSONModel.md)|  | 

### Return type

[**PrometheusRemoteWriteTargetJSONModel**](PrometheusRemoteWriteTargetJSONModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording_rule**
> SuccessResponseBodyModel delete_recording_rule(recording_rule_id)

Delete a recording rule.

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
api_instance = pythonclient.RecordingRulesApi(pythonclient.ApiClient(configuration))
recording_rule_id = 789 # int | 

try:
    # Delete a recording rule.
    api_response = api_instance.delete_recording_rule(recording_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingRulesApi->delete_recording_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_rule_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording_rule_write_target**
> SuccessResponseBodyModel delete_recording_rule_write_target()

Delete the write target.

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
api_instance = pythonclient.RecordingRulesApi(pythonclient.ApiClient(configuration))

try:
    # Delete the write target.
    api_response = api_instance.delete_recording_rule_write_target()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingRulesApi->delete_recording_rule_write_target: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_rule_write_target**
> PrometheusRemoteWriteTargetJSONModel get_recording_rule_write_target()

Get the write target.

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
api_instance = pythonclient.RecordingRulesApi(pythonclient.ApiClient(configuration))

try:
    # Get the write target.
    api_response = api_instance.get_recording_rule_write_target()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingRulesApi->get_recording_rule_write_target: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PrometheusRemoteWriteTargetJSONModel**](PrometheusRemoteWriteTargetJSONModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recording_rules**
> list[RecordingRuleJSONModel] list_recording_rules()

Get all recording rules.

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
api_instance = pythonclient.RecordingRulesApi(pythonclient.ApiClient(configuration))

try:
    # Get all recording rules.
    api_response = api_instance.list_recording_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingRulesApi->list_recording_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RecordingRuleJSONModel]**](RecordingRuleJSONModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_create_recording_rule**
> SuccessResponseBodyModel test_create_recording_rule(body)

Test a recording rule.

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
api_instance = pythonclient.RecordingRulesApi(pythonclient.ApiClient(configuration))
body = pythonclient.RecordingRuleJSONModel() # RecordingRuleJSONModel | 

try:
    # Test a recording rule.
    api_response = api_instance.test_create_recording_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingRulesApi->test_create_recording_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordingRuleJSONModel**](RecordingRuleJSONModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recording_rule**
> RecordingRuleJSONModel update_recording_rule(body)

Update a recording rule.

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
api_instance = pythonclient.RecordingRulesApi(pythonclient.ApiClient(configuration))
body = pythonclient.RecordingRuleJSONModel() # RecordingRuleJSONModel | 

try:
    # Update a recording rule.
    api_response = api_instance.update_recording_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingRulesApi->update_recording_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordingRuleJSONModel**](RecordingRuleJSONModel.md)|  | 

### Return type

[**RecordingRuleJSONModel**](RecordingRuleJSONModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

