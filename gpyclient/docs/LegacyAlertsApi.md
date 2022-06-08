# gpyclient.LegacyAlertsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_by_id**](LegacyAlertsApi.md#get_alert_by_id) | **GET** /alerts/{alert_id} | Get alert by ID.
[**get_alerts**](LegacyAlertsApi.md#get_alerts) | **GET** /alerts | Get legacy alerts.
[**get_dashboard_states**](LegacyAlertsApi.md#get_dashboard_states) | **GET** /alerts/states-for-dashboard | Get alert states for a dashboard.
[**pause_alert**](LegacyAlertsApi.md#pause_alert) | **POST** /alerts/{alert_id}/pause | Pause/unpause alert by id.
[**test_alert**](LegacyAlertsApi.md#test_alert) | **POST** /alerts/test | Test alert.


# **get_alert_by_id**
> list[AlertModel] get_alert_by_id(alert_id)

Get alert by ID.

“evalMatches” data in the response is cached in the db when and only when the state of the alert changes (e.g. transitioning from “ok” to “alerting” state). If data from one server triggers the alert first and, before that server is seen leaving alerting state, a second server also enters a state that would trigger the alert, the second server will not be visible in “evalMatches” data.

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
api_instance = gpyclient.LegacyAlertsApi(gpyclient.ApiClient(configuration))
alert_id = 'alert_id_example' # str | 

try:
    # Get alert by ID.
    api_response = api_instance.get_alert_by_id(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsApi->get_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 

### Return type

[**list[AlertModel]**](AlertModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> list[AlertListItemDTOModel] get_alerts(dashboard_id=dashboard_id, panel_id=panel_id, query=query, state=state, limit=limit, folder_id=folder_id, dashboard_query=dashboard_query, dashboard_tag=dashboard_tag)

Get legacy alerts.

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
api_instance = gpyclient.LegacyAlertsApi(gpyclient.ApiClient(configuration))
dashboard_id = ['dashboard_id_example'] # list[str] | Limit response to alerts in specified dashboard(s). You can specify multiple dashboards. (optional)
panel_id = 789 # int | Limit response to alert for a specified panel on a dashboard. (optional)
query = 'query_example' # str | Limit response to alerts having a name like this value. (optional)
state = 'state_example' # str | Return alerts with one or more of the following alert states (optional)
limit = 789 # int | Limit response to X number of alerts. (optional)
folder_id = ['folder_id_example'] # list[str] | Limit response to alerts of dashboards in specified folder(s). You can specify multiple folders (optional)
dashboard_query = 'dashboard_query_example' # str | Limit response to alerts having a dashboard name like this value./ Limit response to alerts having a dashboard name like this value. (optional)
dashboard_tag = ['dashboard_tag_example'] # list[str] | Limit response to alerts of dashboards with specified tags. To do an “AND” filtering with multiple tags, specify the tags parameter multiple times (optional)

try:
    # Get legacy alerts.
    api_response = api_instance.get_alerts(dashboard_id=dashboard_id, panel_id=panel_id, query=query, state=state, limit=limit, folder_id=folder_id, dashboard_query=dashboard_query, dashboard_tag=dashboard_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsApi->get_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | [**list[str]**](str.md)| Limit response to alerts in specified dashboard(s). You can specify multiple dashboards. | [optional] 
 **panel_id** | **int**| Limit response to alert for a specified panel on a dashboard. | [optional] 
 **query** | **str**| Limit response to alerts having a name like this value. | [optional] 
 **state** | **str**| Return alerts with one or more of the following alert states | [optional] 
 **limit** | **int**| Limit response to X number of alerts. | [optional] 
 **folder_id** | [**list[str]**](str.md)| Limit response to alerts of dashboards in specified folder(s). You can specify multiple folders | [optional] 
 **dashboard_query** | **str**| Limit response to alerts having a dashboard name like this value./ Limit response to alerts having a dashboard name like this value. | [optional] 
 **dashboard_tag** | [**list[str]**](str.md)| Limit response to alerts of dashboards with specified tags. To do an “AND” filtering with multiple tags, specify the tags parameter multiple times | [optional] 

### Return type

[**list[AlertListItemDTOModel]**](AlertListItemDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_states**
> list[AlertStateInfoDTOModel] get_dashboard_states(dashboard_id)

Get alert states for a dashboard.

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
api_instance = gpyclient.LegacyAlertsApi(gpyclient.ApiClient(configuration))
dashboard_id = 789 # int | 

try:
    # Get alert states for a dashboard.
    api_response = api_instance.get_dashboard_states(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsApi->get_dashboard_states: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 

### Return type

[**list[AlertStateInfoDTOModel]**](AlertStateInfoDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_alert**
> InlineResponse2002Model pause_alert(alert_id, body)

Pause/unpause alert by id.

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
api_instance = gpyclient.LegacyAlertsApi(gpyclient.ApiClient(configuration))
alert_id = 'alert_id_example' # str | 
body = gpyclient.PauseAlertCommandModel() # PauseAlertCommandModel | 

try:
    # Pause/unpause alert by id.
    api_response = api_instance.pause_alert(alert_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsApi->pause_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 
 **body** | [**PauseAlertCommandModel**](PauseAlertCommandModel.md)|  | 

### Return type

[**InlineResponse2002Model**](InlineResponse2002Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_alert**
> AlertTestResultModel test_alert(body=body)

Test alert.

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
api_instance = gpyclient.LegacyAlertsApi(gpyclient.ApiClient(configuration))
body = gpyclient.AlertTestCommandModel() # AlertTestCommandModel |  (optional)

try:
    # Test alert.
    api_response = api_instance.test_alert(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsApi->test_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertTestCommandModel**](AlertTestCommandModel.md)|  | [optional] 

### Return type

[**AlertTestResultModel**](AlertTestResultModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

