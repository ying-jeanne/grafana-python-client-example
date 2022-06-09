from __future__ import print_function
import time
import gpyclient
from gpyclient.rest import ApiException
from pprint import pprint
from datetime import datetime

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
db = gpyclient.DashboardModel(
    annotations=None, 
    description="this is the description of a dashboard", 
    fiscal_year_start_month = 10, 
    graph_tooltip = 1, 
    title = 'dashisgood', 
    uid = 'aaaabbbb', 
    schema_version = 26,
    version = 3)
body = gpyclient.SaveDashboardCommandModel(dashboard = db, folder_id = 0) # SaveDashboardCommandModel | 

try:
    # Create / Update dashboard
    api_response = api_instance.post_dashboard(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->post_dashboard: %s\n" % e)