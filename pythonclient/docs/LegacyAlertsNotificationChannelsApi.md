# pythonclient.LegacyAlertsNotificationChannelsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_notification_channel**](LegacyAlertsNotificationChannelsApi.md#create_alert_notification_channel) | **POST** /alert-notifications | Create notification channel.
[**delete_alert_notification_channel**](LegacyAlertsNotificationChannelsApi.md#delete_alert_notification_channel) | **DELETE** /alert-notifications/{notification_channel_id} | Delete alert notification by ID.
[**delete_alert_notification_channel_by_uid**](LegacyAlertsNotificationChannelsApi.md#delete_alert_notification_channel_by_uid) | **DELETE** /alert-notifications/uid/{notification_channel_uid} | Delete alert notification by UID.
[**get_alert_notification_channel_by_id**](LegacyAlertsNotificationChannelsApi.md#get_alert_notification_channel_by_id) | **GET** /alert-notifications/{notification_channel_id} | Get notification channel by ID.
[**get_alert_notification_channel_by_uid**](LegacyAlertsNotificationChannelsApi.md#get_alert_notification_channel_by_uid) | **GET** /alert-notifications/uid/{notification_channel_uid} | Get notification channel by UID
[**get_alert_notification_channels**](LegacyAlertsNotificationChannelsApi.md#get_alert_notification_channels) | **GET** /alert-notifications | Get all notification channels.
[**lookup_alert_notification_channels**](LegacyAlertsNotificationChannelsApi.md#lookup_alert_notification_channels) | **GET** /alert-notifications/lookup | Get all notification channels (lookup)
[**notification_channel_test**](LegacyAlertsNotificationChannelsApi.md#notification_channel_test) | **POST** /alert-notifications/test | Test notification channel.
[**update_alert_notification_channel**](LegacyAlertsNotificationChannelsApi.md#update_alert_notification_channel) | **PUT** /alert-notifications/{notification_channel_id} | Update notification channel by ID.
[**update_alert_notification_channel_byuid**](LegacyAlertsNotificationChannelsApi.md#update_alert_notification_channel_byuid) | **PUT** /alert-notifications/uid/{notification_channel_uid} | Update notification channel by UID.


# **create_alert_notification_channel**
> AlertNotificationModel create_alert_notification_channel(body)

Create notification channel.

You can find the full list of [supported notifiers](https://grafana.com/docs/grafana/latest/alerting/old-alerting/notifications/#list-of-supported-notifiers) on the alert notifiers page.

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
api_instance = pythonclient.LegacyAlertsNotificationChannelsApi(pythonclient.ApiClient(configuration))
body = pythonclient.CreateAlertNotificationCommandModel() # CreateAlertNotificationCommandModel | 

try:
    # Create notification channel.
    api_response = api_instance.create_alert_notification_channel(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsNotificationChannelsApi->create_alert_notification_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAlertNotificationCommandModel**](CreateAlertNotificationCommandModel.md)|  | 

### Return type

[**AlertNotificationModel**](AlertNotificationModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_notification_channel**
> SuccessResponseBodyModel delete_alert_notification_channel(notification_channel_id)

Delete alert notification by ID.

Deletes an existing notification channel identified by ID.

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
api_instance = pythonclient.LegacyAlertsNotificationChannelsApi(pythonclient.ApiClient(configuration))
notification_channel_id = 789 # int | 

try:
    # Delete alert notification by ID.
    api_response = api_instance.delete_alert_notification_channel(notification_channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsNotificationChannelsApi->delete_alert_notification_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_id** | **int**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_notification_channel_by_uid**
> InlineResponse2001Model delete_alert_notification_channel_by_uid(notification_channel_uid)

Delete alert notification by UID.

Deletes an existing notification channel identified by UID.

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
api_instance = pythonclient.LegacyAlertsNotificationChannelsApi(pythonclient.ApiClient(configuration))
notification_channel_uid = 'notification_channel_uid_example' # str | 

try:
    # Delete alert notification by UID.
    api_response = api_instance.delete_alert_notification_channel_by_uid(notification_channel_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsNotificationChannelsApi->delete_alert_notification_channel_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_uid** | **str**|  | 

### Return type

[**InlineResponse2001Model**](InlineResponse2001Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_notification_channel_by_id**
> AlertNotificationModel get_alert_notification_channel_by_id(notification_channel_id)

Get notification channel by ID.

Returns the notification channel given the notification channel ID.

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
api_instance = pythonclient.LegacyAlertsNotificationChannelsApi(pythonclient.ApiClient(configuration))
notification_channel_id = 789 # int | 

try:
    # Get notification channel by ID.
    api_response = api_instance.get_alert_notification_channel_by_id(notification_channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsNotificationChannelsApi->get_alert_notification_channel_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_id** | **int**|  | 

### Return type

[**AlertNotificationModel**](AlertNotificationModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_notification_channel_by_uid**
> AlertNotificationModel get_alert_notification_channel_by_uid(notification_channel_uid)

Get notification channel by UID

Returns the notification channel given the notification channel UID.

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
api_instance = pythonclient.LegacyAlertsNotificationChannelsApi(pythonclient.ApiClient(configuration))
notification_channel_uid = 'notification_channel_uid_example' # str | 

try:
    # Get notification channel by UID
    api_response = api_instance.get_alert_notification_channel_by_uid(notification_channel_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsNotificationChannelsApi->get_alert_notification_channel_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_uid** | **str**|  | 

### Return type

[**AlertNotificationModel**](AlertNotificationModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_notification_channels**
> list[AlertNotificationModel] get_alert_notification_channels()

Get all notification channels.

Returns all notification channels that the authenticated user has permission to view.

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
api_instance = pythonclient.LegacyAlertsNotificationChannelsApi(pythonclient.ApiClient(configuration))

try:
    # Get all notification channels.
    api_response = api_instance.get_alert_notification_channels()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsNotificationChannelsApi->get_alert_notification_channels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AlertNotificationModel]**](AlertNotificationModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_alert_notification_channels**
> list[AlertNotificationLookupModel] lookup_alert_notification_channels()

Get all notification channels (lookup)

Returns all notification channels, but with less detailed information. Accessible by any authenticated user and is mainly used by providing alert notification channels in Grafana UI when configuring alert rule.

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
api_instance = pythonclient.LegacyAlertsNotificationChannelsApi(pythonclient.ApiClient(configuration))

try:
    # Get all notification channels (lookup)
    api_response = api_instance.lookup_alert_notification_channels()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsNotificationChannelsApi->lookup_alert_notification_channels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AlertNotificationLookupModel]**](AlertNotificationLookupModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_channel_test**
> SuccessResponseBodyModel notification_channel_test(body)

Test notification channel.

Sends a test notification to the channel.

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
api_instance = pythonclient.LegacyAlertsNotificationChannelsApi(pythonclient.ApiClient(configuration))
body = pythonclient.NotificationTestCommandModel() # NotificationTestCommandModel | 

try:
    # Test notification channel.
    api_response = api_instance.notification_channel_test(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsNotificationChannelsApi->notification_channel_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationTestCommandModel**](NotificationTestCommandModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_notification_channel**
> AlertNotificationModel update_alert_notification_channel(notification_channel_id, body)

Update notification channel by ID.

Updates an existing notification channel identified by ID.

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
api_instance = pythonclient.LegacyAlertsNotificationChannelsApi(pythonclient.ApiClient(configuration))
notification_channel_id = 789 # int | 
body = pythonclient.UpdateAlertNotificationCommandModel() # UpdateAlertNotificationCommandModel | 

try:
    # Update notification channel by ID.
    api_response = api_instance.update_alert_notification_channel(notification_channel_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsNotificationChannelsApi->update_alert_notification_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_id** | **int**|  | 
 **body** | [**UpdateAlertNotificationCommandModel**](UpdateAlertNotificationCommandModel.md)|  | 

### Return type

[**AlertNotificationModel**](AlertNotificationModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_notification_channel_byuid**
> AlertNotificationModel update_alert_notification_channel_byuid(notification_channel_uid, body)

Update notification channel by UID.

Updates an existing notification channel identified by uid.

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
api_instance = pythonclient.LegacyAlertsNotificationChannelsApi(pythonclient.ApiClient(configuration))
notification_channel_uid = 'notification_channel_uid_example' # str | 
body = pythonclient.UpdateAlertNotificationWithUidCommandModel() # UpdateAlertNotificationWithUidCommandModel | 

try:
    # Update notification channel by UID.
    api_response = api_instance.update_alert_notification_channel_byuid(notification_channel_uid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyAlertsNotificationChannelsApi->update_alert_notification_channel_byuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_uid** | **str**|  | 
 **body** | [**UpdateAlertNotificationWithUidCommandModel**](UpdateAlertNotificationWithUidCommandModel.md)|  | 

### Return type

[**AlertNotificationModel**](AlertNotificationModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

