# gpyclient.AdminProvisioningApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reload_provisioned_access_control**](AdminProvisioningApi.md#reload_provisioned_access_control) | **POST** /admin/provisioning/accesscontrol/reload | Reload access control provisioning configurations.
[**reload_provisioned_alert_notifiers**](AdminProvisioningApi.md#reload_provisioned_alert_notifiers) | **POST** /admin/provisioning/notifications/reload | Reload legacy alert notifier provisioning configurations.
[**reload_provisioned_dashboards**](AdminProvisioningApi.md#reload_provisioned_dashboards) | **POST** /admin/provisioning/dashboards/reload | Reload dashboard provisioning configurations.
[**reload_provisioned_datasources**](AdminProvisioningApi.md#reload_provisioned_datasources) | **POST** /admin/provisioning/datasources/reload | Reload datasource provisioning configurations.
[**reload_provisioned_plugins**](AdminProvisioningApi.md#reload_provisioned_plugins) | **POST** /admin/provisioning/plugins/reload | Reload plugin provisioning configurations.


# **reload_provisioned_access_control**
> SuccessResponseBodyModel reload_provisioned_access_control()

Reload access control provisioning configurations.

Reloads the provisioning config files for access control again. It won’t return until the new provisioned entities are already stored in the database. In case of dashboards, it will stop polling for changes in dashboard files and then restart it with new configurations after returning. If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `provisioning:reload` and scope `provisioners:accesscontrol`.

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
api_instance = gpyclient.AdminProvisioningApi(gpyclient.ApiClient(configuration))

try:
    # Reload access control provisioning configurations.
    api_response = api_instance.reload_provisioned_access_control()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminProvisioningApi->reload_provisioned_access_control: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_provisioned_alert_notifiers**
> SuccessResponseBodyModel reload_provisioned_alert_notifiers()

Reload legacy alert notifier provisioning configurations.

Reloads the provisioning config files for legacy alert notifiers again. It won’t return until the new provisioned entities are already stored in the database. In case of dashboards, it will stop polling for changes in dashboard files and then restart it with new configurations after returning. If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `provisioning:reload` and scope `provisioners:notifications`.

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
api_instance = gpyclient.AdminProvisioningApi(gpyclient.ApiClient(configuration))

try:
    # Reload legacy alert notifier provisioning configurations.
    api_response = api_instance.reload_provisioned_alert_notifiers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminProvisioningApi->reload_provisioned_alert_notifiers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_provisioned_dashboards**
> SuccessResponseBodyModel reload_provisioned_dashboards()

Reload dashboard provisioning configurations.

Reloads the provisioning config files for dashboards again. It won’t return until the new provisioned entities are already stored in the database. In case of dashboards, it will stop polling for changes in dashboard files and then restart it with new configurations after returning. If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `provisioning:reload` and scope `provisioners:dashboards`.

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
api_instance = gpyclient.AdminProvisioningApi(gpyclient.ApiClient(configuration))

try:
    # Reload dashboard provisioning configurations.
    api_response = api_instance.reload_provisioned_dashboards()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminProvisioningApi->reload_provisioned_dashboards: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_provisioned_datasources**
> SuccessResponseBodyModel reload_provisioned_datasources()

Reload datasource provisioning configurations.

Reloads the provisioning config files for datasources again. It won’t return until the new provisioned entities are already stored in the database. In case of dashboards, it will stop polling for changes in dashboard files and then restart it with new configurations after returning. If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `provisioning:reload` and scope `provisioners:datasources`.

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
api_instance = gpyclient.AdminProvisioningApi(gpyclient.ApiClient(configuration))

try:
    # Reload datasource provisioning configurations.
    api_response = api_instance.reload_provisioned_datasources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminProvisioningApi->reload_provisioned_datasources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_provisioned_plugins**
> SuccessResponseBodyModel reload_provisioned_plugins()

Reload plugin provisioning configurations.

Reloads the provisioning config files for plugins again. It won’t return until the new provisioned entities are already stored in the database. In case of dashboards, it will stop polling for changes in dashboard files and then restart it with new configurations after returning. If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `provisioning:reload` and scope `provisioners:plugin`.

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
api_instance = gpyclient.AdminProvisioningApi(gpyclient.ApiClient(configuration))

try:
    # Reload plugin provisioning configurations.
    api_response = api_instance.reload_provisioned_plugins()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminProvisioningApi->reload_provisioned_plugins: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

