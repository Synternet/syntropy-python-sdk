# syntropy_sdk.ServicesApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_agent_service_destroy**](ServicesApi.md#platform_agent_service_destroy) | **POST** /api/platform/agent-services-delete | Delete services
[**platform_agent_service_index**](ServicesApi.md#platform_agent_service_index) | **GET** /api/platform/agent-services | Get services
[**platform_agent_service_subnet_update**](ServicesApi.md#platform_agent_service_subnet_update) | **POST** /api/platform/agent-services-subnets | Update service status
[**platform_connection_service_show**](ServicesApi.md#platform_connection_service_show) | **GET** /api/platform/connections/services | Get services
[**platform_connection_service_update**](ServicesApi.md#platform_connection_service_update) | **POST** /api/platform/connections/services | Create services
[**platform_connection_subnet_destroy**](ServicesApi.md#platform_connection_subnet_destroy) | **POST** /api/platform/connections/services/remove | Delete services

# **platform_agent_service_destroy**
> platform_agent_service_destroy(body)

Delete services

Delete agent services.

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
api_instance = syntropy_sdk.ServicesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.AgentServicesDeletionObject() # AgentServicesDeletionObject | 

try:
    # Delete services
    api_instance.platform_agent_service_destroy(body)
except ApiException as e:
    print("Exception when calling ServicesApi->platform_agent_service_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentServicesDeletionObject**](AgentServicesDeletionObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_service_index**
> PlatformResponseAgentServiceGetServicesByAgentIdUserIdObjectArray_ platform_agent_service_index(agent_ids)

Get services

Get agent services.

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
api_instance = syntropy_sdk.ServicesApi(syntropy_sdk.ApiClient(configuration))
agent_ids = [3.4] # list[float] | 

try:
    # Get services
    api_response = api_instance.platform_agent_service_index(agent_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->platform_agent_service_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_ids** | [**list[float]**](float.md)|  | 

### Return type

[**PlatformResponseAgentServiceGetServicesByAgentIdUserIdObjectArray_**](PlatformResponseAgentServiceGetServicesByAgentIdUserIdObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_service_subnet_update**
> platform_agent_service_subnet_update(body)

Update service status

Update agent services status.

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
api_instance = syntropy_sdk.ServicesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.UpdateStatusBody() # UpdateStatusBody | 

try:
    # Update service status
    api_instance.platform_agent_service_subnet_update(body)
except ApiException as e:
    print("Exception when calling ServicesApi->platform_agent_service_subnet_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateStatusBody**](UpdateStatusBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_service_show**
> PlatformResponseAgentConnGroupWithServicesObjectArray_ platform_connection_service_show(connection_group_ids)

Get services

Retrieves connection services

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
api_instance = syntropy_sdk.ServicesApi(syntropy_sdk.ApiClient(configuration))
connection_group_ids = [3.4] # list[float] | 

try:
    # Get services
    api_response = api_instance.platform_connection_service_show(connection_group_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->platform_connection_service_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_group_ids** | [**list[float]**](float.md)|  | 

### Return type

[**PlatformResponseAgentConnGroupWithServicesObjectArray_**](PlatformResponseAgentConnGroupWithServicesObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_service_update**
> platform_connection_service_update(body)

Create services

Updates agent connection services ips

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
api_instance = syntropy_sdk.ServicesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.ConnectionGroupServicesUpdateObject() # ConnectionGroupServicesUpdateObject | 

try:
    # Create services
    api_instance.platform_connection_service_update(body)
except ApiException as e:
    print("Exception when calling ServicesApi->platform_connection_service_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionGroupServicesUpdateObject**](ConnectionGroupServicesUpdateObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_subnet_destroy**
> platform_connection_subnet_destroy(body)

Delete services

Deletes agent connection services/subnets.

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
api_instance = syntropy_sdk.ServicesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.AgentConnectionSubnetsDeletionObject() # AgentConnectionSubnetsDeletionObject | 

try:
    # Delete services
    api_instance.platform_connection_subnet_destroy(body)
except ApiException as e:
    print("Exception when calling ServicesApi->platform_connection_subnet_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentConnectionSubnetsDeletionObject**](AgentConnectionSubnetsDeletionObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

