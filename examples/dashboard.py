from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gpyclient.Configuration()
# configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = gpyclient.Configuration()
configuration.username = 'admin'
configuration.password = 'password'

# create an instance of the API class
api_instance = gpyclient.DashboardsApi(gpyclient.ApiClient(configuration))
body = gpyclient.SaveDashboardCommandModel() # SaveDashboardCommandModel | 

try:
    # Create / Update dashboard
    api_response = api_instance.post_dashboard(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->post_dashboard: %s\n" % e)