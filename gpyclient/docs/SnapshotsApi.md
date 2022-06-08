# gpyclient.SnapshotsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snapshot**](SnapshotsApi.md#create_snapshot) | **POST** /snapshots | When creating a snapshot using the API, you have to provide the full dashboard payload including the snapshot data. This endpoint is designed for the Grafana UI.
[**delete_snapshot_by_delete_key**](SnapshotsApi.md#delete_snapshot_by_delete_key) | **GET** /snapshots-delete/{deleteKey} | Delete Snapshot by deleteKey.
[**delete_snapshot_by_key**](SnapshotsApi.md#delete_snapshot_by_key) | **DELETE** /snapshots/{key} | Delete Snapshot by Key.
[**get_snapshot_by_key**](SnapshotsApi.md#get_snapshot_by_key) | **GET** /snapshots/{key} | Get Snapshot by Key.
[**get_snapshot_sharing_options**](SnapshotsApi.md#get_snapshot_sharing_options) | **GET** /snapshot/shared-options | Get snapshot sharing settings.
[**get_snapshots**](SnapshotsApi.md#get_snapshots) | **GET** /dashboard/snapshots | List snapshots.


# **create_snapshot**
> InlineResponse20014Model create_snapshot(body)

When creating a snapshot using the API, you have to provide the full dashboard payload including the snapshot data. This endpoint is designed for the Grafana UI.

Snapshot public mode should be enabled or authentication is required.

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
api_instance = gpyclient.SnapshotsApi(gpyclient.ApiClient(configuration))
body = gpyclient.CreateDashboardSnapshotCommandModel() # CreateDashboardSnapshotCommandModel | 

try:
    # When creating a snapshot using the API, you have to provide the full dashboard payload including the snapshot data. This endpoint is designed for the Grafana UI.
    api_response = api_instance.create_snapshot(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->create_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDashboardSnapshotCommandModel**](CreateDashboardSnapshotCommandModel.md)|  | 

### Return type

[**InlineResponse20014Model**](InlineResponse20014Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_by_delete_key**
> SuccessResponseBodyModel delete_snapshot_by_delete_key(delete_key)

Delete Snapshot by deleteKey.

Snapshot public mode should be enabled or authentication is required.

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
api_instance = gpyclient.SnapshotsApi(gpyclient.ApiClient(configuration))
delete_key = 'delete_key_example' # str | 

try:
    # Delete Snapshot by deleteKey.
    api_response = api_instance.delete_snapshot_by_delete_key(delete_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->delete_snapshot_by_delete_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_key** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_by_key**
> SuccessResponseBodyModel delete_snapshot_by_key(key)

Delete Snapshot by Key.

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
api_instance = gpyclient.SnapshotsApi(gpyclient.ApiClient(configuration))
key = 'key_example' # str | 

try:
    # Delete Snapshot by Key.
    api_response = api_instance.delete_snapshot_by_key(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->delete_snapshot_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_by_key**
> get_snapshot_by_key(key)

Get Snapshot by Key.

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
api_instance = gpyclient.SnapshotsApi(gpyclient.ApiClient(configuration))
key = 'key_example' # str | 

try:
    # Get Snapshot by Key.
    api_instance.get_snapshot_by_key(key)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_snapshot_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_sharing_options**
> InlineResponse20013Model get_snapshot_sharing_options()

Get snapshot sharing settings.

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
api_instance = gpyclient.SnapshotsApi(gpyclient.ApiClient(configuration))

try:
    # Get snapshot sharing settings.
    api_response = api_instance.get_snapshot_sharing_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_snapshot_sharing_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20013Model**](InlineResponse20013Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshots**
> list[DashboardSnapshotDTOModel] get_snapshots(query=query, limit=limit)

List snapshots.

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
api_instance = gpyclient.SnapshotsApi(gpyclient.ApiClient(configuration))
query = 'query_example' # str | Search Query (optional)
limit = 1000 # int | Limit the number of returned results (optional) (default to 1000)

try:
    # List snapshots.
    api_response = api_instance.get_snapshots(query=query, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search Query | [optional] 
 **limit** | **int**| Limit the number of returned results | [optional] [default to 1000]

### Return type

[**list[DashboardSnapshotDTOModel]**](DashboardSnapshotDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

