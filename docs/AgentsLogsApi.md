# syntropy_sdk.AgentsLogsApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_platform_agent**](AgentsLogsApi.md#search_platform_agent) | **POST** /api/search/platform-agents | Get agents log
[**search_platform_agent_error**](AgentsLogsApi.md#search_platform_agent_error) | **POST** /api/search/platform-agents-errors | Get agents errors log

# **search_platform_agent**
> Object search_platform_agent(body)

Get agents log

Search platform agents index.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
configuration = syntropy_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AgentsLogsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.PlatformAgentsBodyObject() # PlatformAgentsBodyObject | 

try:
    # Get agents log
    api_response = api_instance.search_platform_agent(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsLogsApi->search_platform_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlatformAgentsBodyObject**](PlatformAgentsBodyObject.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_platform_agent_error**
> PlatformAgentsErrorResponse search_platform_agent_error(body)

Get agents errors log

Search platform agents index for errors.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
configuration = syntropy_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AgentsLogsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.PlatformAgentsErrorBody() # PlatformAgentsErrorBody | 

try:
    # Get agents errors log
    api_response = api_instance.search_platform_agent_error(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsLogsApi->search_platform_agent_error: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlatformAgentsErrorBody**](PlatformAgentsErrorBody.md)|  | 

### Return type

[**PlatformAgentsErrorResponse**](PlatformAgentsErrorResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

