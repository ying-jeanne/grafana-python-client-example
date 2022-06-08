# gpyclient.AdminApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings**](AdminApi.md#get_settings) | **GET** /admin/settings | Fetch settings.
[**get_stats**](AdminApi.md#get_stats) | **GET** /admin/stats | Fetch Grafana Stats.
[**pause_all_alerts**](AdminApi.md#pause_all_alerts) | **POST** /admin/pause-all-alerts | Pause/unpause all (legacy) alerts.


# **get_settings**
> SettingsBagModel get_settings()

Fetch settings.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `settings:read` and scopes: `settings:*`, `settings:auth.saml:` and `settings:auth.saml:enabled` (property level).

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
api_instance = gpyclient.AdminApi(gpyclient.ApiClient(configuration))

try:
    # Fetch settings.
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsBagModel**](SettingsBagModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> AdminStatsModel get_stats()

Fetch Grafana Stats.

Only works with Basic Authentication (username and password). See introduction for an explanation. If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `server:stats:read`.

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
api_instance = gpyclient.AdminApi(gpyclient.ApiClient(configuration))

try:
    # Fetch Grafana Stats.
    api_response = api_instance.get_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminStatsModel**](AdminStatsModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_all_alerts**
> InlineResponse200Model pause_all_alerts(body)

Pause/unpause all (legacy) alerts.

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
api_instance = gpyclient.AdminApi(gpyclient.ApiClient(configuration))
body = gpyclient.PauseAllAlertsCommandModel() # PauseAllAlertsCommandModel | 

try:
    # Pause/unpause all (legacy) alerts.
    api_response = api_instance.pause_all_alerts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->pause_all_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PauseAllAlertsCommandModel**](PauseAllAlertsCommandModel.md)|  | 

### Return type

[**InlineResponse200Model**](InlineResponse200Model.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

