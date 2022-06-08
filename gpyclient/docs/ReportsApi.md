# gpyclient.ReportsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report**](ReportsApi.md#create_report) | **POST** /reports | Create a report.
[**delete_report**](ReportsApi.md#delete_report) | **DELETE** /reports/{reportID} | Delete a report.
[**get_report**](ReportsApi.md#get_report) | **GET** /reports/{reportID} | Get a report.
[**get_report_settings**](ReportsApi.md#get_report_settings) | **GET** /reports/settings | Get settings.
[**get_reports**](ReportsApi.md#get_reports) | **GET** /reports | List reports.
[**render_report_pd_fs**](ReportsApi.md#render_report_pd_fs) | **GET** /reports/render/pdfs | Render report for multiple dashboards.
[**render_report_pdf**](ReportsApi.md#render_report_pdf) | **GET** /reports/render/pdf/{DashboardID} | Render report for dashboard.
[**save_report_settings**](ReportsApi.md#save_report_settings) | **POST** /reports/settings | Save settings.
[**send_report**](ReportsApi.md#send_report) | **POST** /reports/email | Send a report.
[**send_test_email**](ReportsApi.md#send_test_email) | **POST** /reports/test-email | Send test report via email.
[**update_report**](ReportsApi.md#update_report) | **PUT** /reports/{reportID} | Update a report.


# **create_report**
> object create_report(body)

Create a report.

Available to org admins only and with a valid license.  You need to have a permission with action `reports.admin:create`.

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
api_instance = gpyclient.ReportsApi(gpyclient.ApiClient(configuration))
body = gpyclient.CreateOrUpdateConfigCmdModel() # CreateOrUpdateConfigCmdModel | 

try:
    # Create a report.
    api_response = api_instance.create_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->create_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateConfigCmdModel**](CreateOrUpdateConfigCmdModel.md)|  | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report**
> SuccessResponseBodyModel delete_report(report_id)

Delete a report.

Available to org admins only and with a valid or expired license  You need to have a permission with action `reports.delete` with scope `reports:id:<report ID>`.

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
api_instance = gpyclient.ReportsApi(gpyclient.ApiClient(configuration))
report_id = 789 # int | 

try:
    # Delete a report.
    api_response = api_instance.delete_report(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->delete_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> ConfigDTOModel get_report(report_id)

Get a report.

Available to org admins only and with a valid or expired license  You need to have a permission with action `reports:read` with scope `reports:id:<report ID>`.

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
api_instance = gpyclient.ReportsApi(gpyclient.ApiClient(configuration))
report_id = 789 # int | 

try:
    # Get a report.
    api_response = api_instance.get_report(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**|  | 

### Return type

[**ConfigDTOModel**](ConfigDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_settings**
> SettingsDTOModel get_report_settings()

Get settings.

Available to org admins only and with a valid or expired license  You need to have a permission with action `reports.settings:read`x.

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
api_instance = gpyclient.ReportsApi(gpyclient.ApiClient(configuration))

try:
    # Get settings.
    api_response = api_instance.get_report_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_report_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsDTOModel**](SettingsDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports**
> list[ConfigDTOModel] get_reports()

List reports.

Available to org admins only and with a valid or expired license  You need to have a permission with action `reports:read` with scope `reports:*`.

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
api_instance = gpyclient.ReportsApi(gpyclient.ApiClient(configuration))

try:
    # List reports.
    api_response = api_instance.get_reports()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_reports: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConfigDTOModel]**](ConfigDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_report_pd_fs**
> list[int] render_report_pd_fs()

Render report for multiple dashboards.

Available to all users and with a valid license.

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
api_instance = gpyclient.ReportsApi(gpyclient.ApiClient(configuration))

try:
    # Render report for multiple dashboards.
    api_response = api_instance.render_report_pd_fs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->render_report_pd_fs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[int]**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_report_pdf**
> list[int] render_report_pdf(dashboard_id)

Render report for dashboard.

Please refer to [reports enterprise](#/reports/renderReportPDFs) instead. This will be removed in Grafana 10.

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
api_instance = gpyclient.ReportsApi(gpyclient.ApiClient(configuration))
dashboard_id = 789 # int | 

try:
    # Render report for dashboard.
    api_response = api_instance.render_report_pdf(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->render_report_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 

### Return type

**list[int]**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_report_settings**
> SuccessResponseBodyModel save_report_settings(body)

Save settings.

Available to org admins only and with a valid or expired license  You need to have a permission with action `reports.settings:write`xx.

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
api_instance = gpyclient.ReportsApi(gpyclient.ApiClient(configuration))
body = gpyclient.SettingsDTOModel() # SettingsDTOModel | 

try:
    # Save settings.
    api_response = api_instance.save_report_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->save_report_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsDTOModel**](SettingsDTOModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_report**
> SuccessResponseBodyModel send_report(body)

Send a report.

Generate and send a report. This API waits for the report to be generated before returning. We recommend that you set the client’s timeout to at least 60 seconds. Available to org admins only and with a valid license.  Only available in Grafana Enterprise v7.0+. This API endpoint is experimental and may be deprecated in a future release. On deprecation, a migration strategy will be provided and the endpoint will remain functional until the next major release of Grafana.  You need to have a permission with action `reports:send`.

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
api_instance = gpyclient.ReportsApi(gpyclient.ApiClient(configuration))
body = gpyclient.ReportEmailDTOModel() # ReportEmailDTOModel | 

try:
    # Send a report.
    api_response = api_instance.send_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->send_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportEmailDTOModel**](ReportEmailDTOModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_test_email**
> SuccessResponseBodyModel send_test_email(body)

Send test report via email.

Available to org admins only and with a valid license.  You need to have a permission with action `reports:send`.

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
api_instance = gpyclient.ReportsApi(gpyclient.ApiClient(configuration))
body = gpyclient.CreateOrUpdateConfigCmdModel() # CreateOrUpdateConfigCmdModel | 

try:
    # Send test report via email.
    api_response = api_instance.send_test_email(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->send_test_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateConfigCmdModel**](CreateOrUpdateConfigCmdModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report**
> SuccessResponseBodyModel update_report(report_id, body)

Update a report.

Available to org admins only and with a valid or expired license  You need to have a permission with action `reports.admin:write` with scope `reports:id:<report ID>`.

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
api_instance = gpyclient.ReportsApi(gpyclient.ApiClient(configuration))
report_id = 789 # int | 
body = gpyclient.CreateOrUpdateConfigCmdModel() # CreateOrUpdateConfigCmdModel | 

try:
    # Update a report.
    api_response = api_instance.update_report(report_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->update_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**|  | 
 **body** | [**CreateOrUpdateConfigCmdModel**](CreateOrUpdateConfigCmdModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

