# gpyclient.DsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_metrics_with_expressions**](DsApi.md#query_metrics_with_expressions) | **POST** /ds/query | Query metrics with expressions


# **query_metrics_with_expressions**
> QueryDataResponseModel query_metrics_with_expressions(body)

Query metrics with expressions

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:query`.

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
api_instance = gpyclient.DsApi(gpyclient.ApiClient(configuration))
body = gpyclient.MetricRequestModel() # MetricRequestModel | 

try:
    # Query metrics with expressions
    api_response = api_instance.query_metrics_with_expressions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DsApi->query_metrics_with_expressions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetricRequestModel**](MetricRequestModel.md)|  | 

### Return type

[**QueryDataResponseModel**](QueryDataResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

