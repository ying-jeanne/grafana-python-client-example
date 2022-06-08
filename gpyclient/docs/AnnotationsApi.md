# gpyclient.AnnotationsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_annotation**](AnnotationsApi.md#create_annotation) | **POST** /annotations | Create Annotation.
[**create_graphite_annotation**](AnnotationsApi.md#create_graphite_annotation) | **POST** /annotations/graphite | Create Annotation in Graphite format.
[**delete_annotation**](AnnotationsApi.md#delete_annotation) | **DELETE** /annotations/{annotation_id} | Delete Annotation By ID.
[**get_annotation**](AnnotationsApi.md#get_annotation) | **GET** /annotations/{annotation_id} | Get Annotation by Id.
[**get_annotation_tags**](AnnotationsApi.md#get_annotation_tags) | **GET** /annotations/tags | Find Annotations Tags.
[**get_annotations**](AnnotationsApi.md#get_annotations) | **GET** /annotations | Find Annotations.
[**mass_delete_annotations**](AnnotationsApi.md#mass_delete_annotations) | **POST** /annotations/mass-delete | Delete multiple annotations.
[**patch_annotation**](AnnotationsApi.md#patch_annotation) | **PATCH** /annotations/{annotation_id} | Patch Annotation
[**update_annotation**](AnnotationsApi.md#update_annotation) | **PUT** /annotations/{annotation_id} | Update Annotation.


# **create_annotation**
> InlineResponse2003Model create_annotation(body)

Create Annotation.

Creates an annotation in the Grafana database. The dashboardId and panelId fields are optional. If they are not specified then an organization annotation is created and can be queried in any dashboard that adds the Grafana annotations data source. When creating a region annotation include the timeEnd property. The format for `time` and `timeEnd` should be epoch numbers in millisecond resolution. The response for this HTTP request is slightly different in versions prior to v6.4. In prior versions you would also get an endId if you where creating a region. But in 6.4 regions are represented using a single event with time and timeEnd properties.

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
api_instance = gpyclient.AnnotationsApi(gpyclient.ApiClient(configuration))
body = gpyclient.PostAnnotationsCmdModel() # PostAnnotationsCmdModel | 

try:
    # Create Annotation.
    api_response = api_instance.create_annotation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->create_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAnnotationsCmdModel**](PostAnnotationsCmdModel.md)|  | 

### Return type

[**InlineResponse2003Model**](InlineResponse2003Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_graphite_annotation**
> InlineResponse2003Model create_graphite_annotation(body)

Create Annotation in Graphite format.

Creates an annotation by using Graphite-compatible event format. The `when` and `data` fields are optional. If `when` is not specified then the current time will be used as annotation’s timestamp. The `tags` field can also be in prior to Graphite `0.10.0` format (string with multiple tags being separated by a space).

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
api_instance = gpyclient.AnnotationsApi(gpyclient.ApiClient(configuration))
body = gpyclient.PostGraphiteAnnotationsCmdModel() # PostGraphiteAnnotationsCmdModel | 

try:
    # Create Annotation in Graphite format.
    api_response = api_instance.create_graphite_annotation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->create_graphite_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostGraphiteAnnotationsCmdModel**](PostGraphiteAnnotationsCmdModel.md)|  | 

### Return type

[**InlineResponse2003Model**](InlineResponse2003Model.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_annotation**
> SuccessResponseBodyModel delete_annotation(annotation_id)

Delete Annotation By ID.

Deletes the annotation that matches the specified ID.

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
api_instance = gpyclient.AnnotationsApi(gpyclient.ApiClient(configuration))
annotation_id = 'annotation_id_example' # str | 

try:
    # Delete Annotation By ID.
    api_response = api_instance.delete_annotation(annotation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->delete_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | **str**|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_annotation**
> ItemDTOModel get_annotation()

Get Annotation by Id.

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
api_instance = gpyclient.AnnotationsApi(gpyclient.ApiClient(configuration))

try:
    # Get Annotation by Id.
    api_response = api_instance.get_annotation()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->get_annotation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ItemDTOModel**](ItemDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_annotation_tags**
> GetAnnotationTagsResponseModel get_annotation_tags(tag=tag, limit=limit)

Find Annotations Tags.

Find all the event tags created in the annotations.

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
api_instance = gpyclient.AnnotationsApi(gpyclient.ApiClient(configuration))
tag = 'tag_example' # str | Tag is a string that you can use to filter tags. (optional)
limit = '100' # str | Max limit for results returned. (optional) (default to 100)

try:
    # Find Annotations Tags.
    api_response = api_instance.get_annotation_tags(tag=tag, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->get_annotation_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Tag is a string that you can use to filter tags. | [optional] 
 **limit** | **str**| Max limit for results returned. | [optional] [default to 100]

### Return type

[**GetAnnotationTagsResponseModel**](GetAnnotationTagsResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_annotations**
> list[ItemDTOModel] get_annotations(_from=_from, to=to, user_id=user_id, alert_id=alert_id, dashboard_id=dashboard_id, panel_id=panel_id, limit=limit, tags=tags, type=type, match_any=match_any)

Find Annotations.

Starting in Grafana v6.4 regions annotations are now returned in one entity that now includes the timeEnd property.

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
api_instance = gpyclient.AnnotationsApi(gpyclient.ApiClient(configuration))
_from = 789 # int | Find annotations created after specific epoch datetime in milliseconds. (optional)
to = 789 # int | Find annotations created before specific epoch datetime in milliseconds. (optional)
user_id = 789 # int | Limit response to annotations created by specific user. (optional)
alert_id = 789 # int | Find annotations for a specified alert. (optional)
dashboard_id = 789 # int | Find annotations that are scoped to a specific dashboard (optional)
panel_id = 789 # int | Find annotations that are scoped to a specific panel (optional)
limit = 789 # int | Max limit for results returned. (optional)
tags = ['tags_example'] # list[str] | Use this to filter organization annotations. Organization annotations are annotations from an annotation data source that are not connected specifically to a dashboard or panel. You can filter by multiple tags. (optional)
type = 'type_example' # str | Return alerts or user created annotations (optional)
match_any = true # bool | Match any or all tags (optional)

try:
    # Find Annotations.
    api_response = api_instance.get_annotations(_from=_from, to=to, user_id=user_id, alert_id=alert_id, dashboard_id=dashboard_id, panel_id=panel_id, limit=limit, tags=tags, type=type, match_any=match_any)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->get_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Find annotations created after specific epoch datetime in milliseconds. | [optional] 
 **to** | **int**| Find annotations created before specific epoch datetime in milliseconds. | [optional] 
 **user_id** | **int**| Limit response to annotations created by specific user. | [optional] 
 **alert_id** | **int**| Find annotations for a specified alert. | [optional] 
 **dashboard_id** | **int**| Find annotations that are scoped to a specific dashboard | [optional] 
 **panel_id** | **int**| Find annotations that are scoped to a specific panel | [optional] 
 **limit** | **int**| Max limit for results returned. | [optional] 
 **tags** | [**list[str]**](str.md)| Use this to filter organization annotations. Organization annotations are annotations from an annotation data source that are not connected specifically to a dashboard or panel. You can filter by multiple tags. | [optional] 
 **type** | **str**| Return alerts or user created annotations | [optional] 
 **match_any** | **bool**| Match any or all tags | [optional] 

### Return type

[**list[ItemDTOModel]**](ItemDTOModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mass_delete_annotations**
> SuccessResponseBodyModel mass_delete_annotations(body)

Delete multiple annotations.

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
api_instance = gpyclient.AnnotationsApi(gpyclient.ApiClient(configuration))
body = gpyclient.MassDeleteAnnotationsCmdModel() # MassDeleteAnnotationsCmdModel | 

try:
    # Delete multiple annotations.
    api_response = api_instance.mass_delete_annotations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->mass_delete_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MassDeleteAnnotationsCmdModel**](MassDeleteAnnotationsCmdModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_annotation**
> SuccessResponseBodyModel patch_annotation(annotation_id, body)

Patch Annotation

Updates one or more properties of an annotation that matches the specified ID. This operation currently supports updating of the `text`, `tags`, `time` and `timeEnd` properties. This is available in Grafana 6.0.0-beta2 and above.

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
api_instance = gpyclient.AnnotationsApi(gpyclient.ApiClient(configuration))
annotation_id = 'annotation_id_example' # str | 
body = gpyclient.PatchAnnotationsCmdModel() # PatchAnnotationsCmdModel | 

try:
    # Patch Annotation
    api_response = api_instance.patch_annotation(annotation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->patch_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | **str**|  | 
 **body** | [**PatchAnnotationsCmdModel**](PatchAnnotationsCmdModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_annotation**
> SuccessResponseBodyModel update_annotation(annotation_id, body)

Update Annotation.

Updates all properties of an annotation that matches the specified id. To only update certain property, consider using the Patch Annotation operation.

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
api_instance = gpyclient.AnnotationsApi(gpyclient.ApiClient(configuration))
annotation_id = 'annotation_id_example' # str | 
body = gpyclient.UpdateAnnotationsCmdModel() # UpdateAnnotationsCmdModel | 

try:
    # Update Annotation.
    api_response = api_instance.update_annotation(annotation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->update_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | **str**|  | 
 **body** | [**UpdateAnnotationsCmdModel**](UpdateAnnotationsCmdModel.md)|  | 

### Return type

[**SuccessResponseBodyModel**](SuccessResponseBodyModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

