# pythonclient.LicensingApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_license_token**](LicensingApi.md#delete_license_token) | **DELETE** /licensing/token | Remove license from database.
[**get_custom_permissions_csv**](LicensingApi.md#get_custom_permissions_csv) | **GET** /licensing/custom-permissions-csv | Get custom permissions report in CSV format.
[**get_custom_permissions_report**](LicensingApi.md#get_custom_permissions_report) | **GET** /licensing/custom-permissions | Get custom permissions report.
[**get_license_status**](LicensingApi.md#get_license_status) | **GET** /licensing/check | Check license availability.
[**get_license_token**](LicensingApi.md#get_license_token) | **GET** /licensing/token | Get license token.
[**post_license_token**](LicensingApi.md#post_license_token) | **POST** /licensing/token | Create license token.
[**post_renew_license_token**](LicensingApi.md#post_renew_license_token) | **POST** /licensing/token/renew | Manually force license refresh.
[**refresh_license_stats**](LicensingApi.md#refresh_license_stats) | **GET** /licensing/refresh-stats | Refresh license stats.


# **delete_license_token**
> ErrorResponseBodyModel delete_license_token(body)

Remove license from database.

Removes the license stored in the Grafana database. Available in Grafana Enterprise v7.4+.  You need to have a permission with action `licensing:delete`.

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
api_instance = pythonclient.LicensingApi(pythonclient.ApiClient(configuration))
body = pythonclient.DeleteTokenCommandModel() # DeleteTokenCommandModel | 

try:
    # Remove license from database.
    api_response = api_instance.delete_license_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->delete_license_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteTokenCommandModel**](DeleteTokenCommandModel.md)|  | 

### Return type

[**ErrorResponseBodyModel**](ErrorResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_permissions_csv**
> list[CustomPermissionsRecordDTOModel] get_custom_permissions_csv()

Get custom permissions report in CSV format.

You need to have a permission with action `licensing.reports:read`.

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
api_instance = pythonclient.LicensingApi(pythonclient.ApiClient(configuration))

try:
    # Get custom permissions report in CSV format.
    api_response = api_instance.get_custom_permissions_csv()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->get_custom_permissions_csv: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomPermissionsRecordDTOModel]**](CustomPermissionsRecordDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_permissions_report**
> list[CustomPermissionsRecordDTOModel] get_custom_permissions_report()

Get custom permissions report.

You need to have a permission with action `licensing.reports:read`.

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
api_instance = pythonclient.LicensingApi(pythonclient.ApiClient(configuration))

try:
    # Get custom permissions report.
    api_response = api_instance.get_custom_permissions_report()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->get_custom_permissions_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomPermissionsRecordDTOModel]**](CustomPermissionsRecordDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_status**
> get_license_status()

Check license availability.

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
api_instance = pythonclient.LicensingApi(pythonclient.ApiClient(configuration))

try:
    # Check license availability.
    api_instance.get_license_status()
except ApiException as e:
    print("Exception when calling LicensingApi->get_license_status: %s\n" % e)
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

# **get_license_token**
> TokenModel get_license_token()

Get license token.

You need to have a permission with action `licensing:read`.

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
api_instance = pythonclient.LicensingApi(pythonclient.ApiClient(configuration))

try:
    # Get license token.
    api_response = api_instance.get_license_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->get_license_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenModel**](TokenModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_license_token**
> TokenModel post_license_token(body)

Create license token.

You need to have a permission with action `licensing:update`.

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
api_instance = pythonclient.LicensingApi(pythonclient.ApiClient(configuration))
body = pythonclient.DeleteTokenCommandModel() # DeleteTokenCommandModel | 

try:
    # Create license token.
    api_response = api_instance.post_license_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->post_license_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteTokenCommandModel**](DeleteTokenCommandModel.md)|  | 

### Return type

[**TokenModel**](TokenModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_renew_license_token**
> post_renew_license_token(body)

Manually force license refresh.

Manually ask license issuer for a new token. Available in Grafana Enterprise v7.4+.  You need to have a permission with action `licensing:update`.

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
api_instance = pythonclient.LicensingApi(pythonclient.ApiClient(configuration))
body = NULL # object | 

try:
    # Manually force license refresh.
    api_instance.post_renew_license_token(body)
except ApiException as e:
    print("Exception when calling LicensingApi->post_renew_license_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_license_stats**
> ActiveUserStatsModel refresh_license_stats()

Refresh license stats.

You need to have a permission with action `licensing:read`.

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
api_instance = pythonclient.LicensingApi(pythonclient.ApiClient(configuration))

try:
    # Refresh license stats.
    api_response = api_instance.refresh_license_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->refresh_license_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ActiveUserStatsModel**](ActiveUserStatsModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

