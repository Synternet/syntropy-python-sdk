# syntropy_sdk.PlatformApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_admin_agent_config**](PlatformApi.md#platform_admin_agent_config) | **GET** /api/platform/admin/agent/{agent_id}/config | 
[**platform_agent_config**](PlatformApi.md#platform_agent_config) | **GET** /api/platform/agent/{agent_id}/config | 
[**platform_agent_coordinates**](PlatformApi.md#platform_agent_coordinates) | **POST** /api/platform/agents/coordinates | 
[**platform_agent_create**](PlatformApi.md#platform_agent_create) | **POST** /api/platform/agents | 
[**platform_agent_destroy**](PlatformApi.md#platform_agent_destroy) | **DELETE** /api/platform/agents/{agent_id} | 
[**platform_agent_id_name_pairs**](PlatformApi.md#platform_agent_id_name_pairs) | **GET** /api/platform/agents/filters | 
[**platform_agent_index**](PlatformApi.md#platform_agent_index) | **GET** /api/platform/agents | 
[**platform_agent_provider_index**](PlatformApi.md#platform_agent_provider_index) | **GET** /api/platform/agent-providers | 
[**platform_agent_provider_show**](PlatformApi.md#platform_agent_provider_show) | **GET** /api/platform/agent-providers/{id} | 
[**platform_agent_service_destroy**](PlatformApi.md#platform_agent_service_destroy) | **POST** /api/platform/agent-services-delete | 
[**platform_agent_service_index**](PlatformApi.md#platform_agent_service_index) | **GET** /api/platform/agent-services | 
[**platform_agent_service_subnet_update**](PlatformApi.md#platform_agent_service_subnet_update) | **POST** /api/platform/agent-services-subnets | 
[**platform_agent_tag_index**](PlatformApi.md#platform_agent_tag_index) | **GET** /api/platform/agent-tags | 
[**platform_agent_update**](PlatformApi.md#platform_agent_update) | **PATCH** /api/platform/agents/{agent_id} | 
[**platform_agents_destroy**](PlatformApi.md#platform_agents_destroy) | **POST** /api/platform/agents/remove | 
[**platform_api_key_create**](PlatformApi.md#platform_api_key_create) | **POST** /api/platform/api-keys | 
[**platform_api_key_destroy**](PlatformApi.md#platform_api_key_destroy) | **DELETE** /api/platform/api-keys/{api_key_id} | 
[**platform_api_key_index**](PlatformApi.md#platform_api_key_index) | **GET** /api/platform/api-keys | 
[**platform_config**](PlatformApi.md#platform_config) | **GET** /api/platform/agent/{agent_id}/wg-config | 
[**platform_connection_agent_destroy**](PlatformApi.md#platform_connection_agent_destroy) | **DELETE** /api/platform/connections/agents/{agent_id} | 
[**platform_connection_agents_destroy**](PlatformApi.md#platform_connection_agents_destroy) | **POST** /api/platform/connections/agents/remove | 
[**platform_connection_create**](PlatformApi.md#platform_connection_create) | **POST** /api/platform/connections | 
[**platform_connection_create_mesh**](PlatformApi.md#platform_connection_create_mesh) | **POST** /api/platform/connections/mesh | 
[**platform_connection_create_p2_t**](PlatformApi.md#platform_connection_create_p2_t) | **POST** /api/platform/connections/point-to-tag | 
[**platform_connection_create_p2p**](PlatformApi.md#platform_connection_create_p2p) | **POST** /api/platform/connections/point-to-point | 
[**platform_connection_destroy**](PlatformApi.md#platform_connection_destroy) | **POST** /api/platform/connections/remove | 
[**platform_connection_destroy_deprecated**](PlatformApi.md#platform_connection_destroy_deprecated) | **DELETE** /api/platform/connections/{connection_id} | 
[**platform_connection_index**](PlatformApi.md#platform_connection_index) | **GET** /api/platform/connections | 
[**platform_connection_service_show**](PlatformApi.md#platform_connection_service_show) | **GET** /api/platform/connection-services | 
[**platform_connection_service_update**](PlatformApi.md#platform_connection_service_update) | **POST** /api/platform/connection-services | 
[**platform_connection_subnet_destroy**](PlatformApi.md#platform_connection_subnet_destroy) | **POST** /api/platform/connection-services-delete | 
[**platform_logs_read_timestamp**](PlatformApi.md#platform_logs_read_timestamp) | **POST** /api/platform/logs-reads-timestamp | 
[**platform_network_info**](PlatformApi.md#platform_network_info) | **GET** /api/platform/network/info | 

# **platform_admin_agent_config**
> PlatformResponseAdminAgentConfig_ platform_admin_agent_config(agent_id)



Returns agent configuration details (admin).

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
agent_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    api_response = api_instance.platform_admin_agent_config(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_admin_agent_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**IdNumber**](.md)|  | 

### Return type

[**PlatformResponseAdminAgentConfig_**](PlatformResponseAdminAgentConfig_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_config**
> PlatformResponseAdminAgentConfig_ platform_agent_config(agent_id)



Returns agent configuration details.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
agent_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    api_response = api_instance.platform_agent_config(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**IdNumber**](.md)|  | 

### Return type

[**PlatformResponseAdminAgentConfig_**](PlatformResponseAdminAgentConfig_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_coordinates**
> PlatformResponseAgentCoordinatesObjectArray_ platform_agent_coordinates(body)



Retrieves Platform agent location coordinates

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.Body1() # Body1 | 

try:
    api_response = api_instance.platform_agent_coordinates(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_coordinates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | 

### Return type

[**PlatformResponseAgentCoordinatesObjectArray_**](PlatformResponseAgentCoordinatesObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_create**
> PlatformResponseAgentCreateAgentObject_ platform_agent_create(body)



Creates new `platform agent`.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.platform_agent_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**PlatformResponseAgentCreateAgentObject_**](PlatformResponseAgentCreateAgentObject_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_destroy**
> platform_agent_destroy(agent_id)



Deletes `platform agent` ands its `connections`.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
agent_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    api_instance.platform_agent_destroy(agent_id)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_id_name_pairs**
> PlatformResponseAgentFiltersObject_ platform_agent_id_name_pairs(filter=filter)



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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
filter = syntropy_sdk.WhereString() # WhereString | ids[]: array of agent ids, example: \"1;2;3\", id|name: agent id or agent name, example: \"name1\" or \"132\", name: exact agent name, example: \"name1\", statuses[]: one of: connected, connected_with_errors, disconnected, example: \"connected;connected_with_errors\", providers[]: array of providers ids, example: \"1;2;3\", tags[]: array of tags ids, example: \"1;2;3\", tags_names[]: array of tags name, example: \"name1;name2;name3\", connected[]: boolean to check if agent belongs to connection, example: \"true\", (optional)

try:
    api_response = api_instance.platform_agent_id_name_pairs(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_id_name_pairs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**WhereString**](.md)| ids[]: array of agent ids, example: \&quot;1;2;3\&quot;, id|name: agent id or agent name, example: \&quot;name1\&quot; or \&quot;132\&quot;, name: exact agent name, example: \&quot;name1\&quot;, statuses[]: one of: connected, connected_with_errors, disconnected, example: \&quot;connected;connected_with_errors\&quot;, providers[]: array of providers ids, example: \&quot;1;2;3\&quot;, tags[]: array of tags ids, example: \&quot;1;2;3\&quot;, tags_names[]: array of tags name, example: \&quot;name1;name2;name3\&quot;, connected[]: boolean to check if agent belongs to connection, example: \&quot;true\&quot;, | [optional] 

### Return type

[**PlatformResponseAgentFiltersObject_**](PlatformResponseAgentFiltersObject_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_index**
> PlatformResponseAgentFoundAndCountObjectArray_ platform_agent_index(skip=skip, take=take, order=order, filter=filter, show_logs_state=show_logs_state)



Retrieves agents.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
skip = syntropy_sdk.SkipNumber() # SkipNumber |  (optional)
take = syntropy_sdk.TakeNumber() # TakeNumber |  (optional)
order = syntropy_sdk.OrderString() # OrderString | string: \"ASC\" | \"DESC\" (optional)
filter = syntropy_sdk.WhereString() # WhereString | ids[]: array of agent ids, example: \"1;2;3\", id|name: agent id or agent name or ip, example: \"name1\" or \"132\" or \"192.168.0.1\", name: exact agent name, example: \"name1\", types[]: array of agent types, example: Windows;macOS;Linux;Virtual, statuses[]: one of: connected, connected_with_errors, disconnected, example: \"connected;connected_with_errors\", providers[]: array of providers ids, example: \"0;1;2;3\", tags[]: array of tags ids, example: \"0;1;2;3\", tags_names[]: array of tags name, example: \"name1;name2;name3\", agent_modified_at_from: date from which agent was last modified agent_modified_at_to: date to which agent was last modified agent_versions[]: array of agent versions, example: \"0.0.75;0.0.74\" locations[]: array of locations, example: \"ES;US\" (optional)
show_logs_state = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.platform_agent_index(skip=skip, take=take, order=order, filter=filter, show_logs_state=show_logs_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | [**SkipNumber**](.md)|  | [optional] 
 **take** | [**TakeNumber**](.md)|  | [optional] 
 **order** | [**OrderString**](.md)| string: \&quot;ASC\&quot; | \&quot;DESC\&quot; | [optional] 
 **filter** | [**WhereString**](.md)| ids[]: array of agent ids, example: \&quot;1;2;3\&quot;, id|name: agent id or agent name or ip, example: \&quot;name1\&quot; or \&quot;132\&quot; or \&quot;192.168.0.1\&quot;, name: exact agent name, example: \&quot;name1\&quot;, types[]: array of agent types, example: Windows;macOS;Linux;Virtual, statuses[]: one of: connected, connected_with_errors, disconnected, example: \&quot;connected;connected_with_errors\&quot;, providers[]: array of providers ids, example: \&quot;0;1;2;3\&quot;, tags[]: array of tags ids, example: \&quot;0;1;2;3\&quot;, tags_names[]: array of tags name, example: \&quot;name1;name2;name3\&quot;, agent_modified_at_from: date from which agent was last modified agent_modified_at_to: date to which agent was last modified agent_versions[]: array of agent versions, example: \&quot;0.0.75;0.0.74\&quot; locations[]: array of locations, example: \&quot;ES;US\&quot; | [optional] 
 **show_logs_state** | **bool**|  | [optional] [default to false]

### Return type

[**PlatformResponseAgentFoundAndCountObjectArray_**](PlatformResponseAgentFoundAndCountObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_provider_index**
> PlatformResponseAgentProviderArray_ platform_agent_provider_index(skip=skip, take=take, order=order)



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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
skip = syntropy_sdk.SkipNumber() # SkipNumber |  (optional)
take = syntropy_sdk.TakeNumber() # TakeNumber |  (optional)
order = syntropy_sdk.AgentProviderOrderString() # AgentProviderOrderString |  (optional)

try:
    api_response = api_instance.platform_agent_provider_index(skip=skip, take=take, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_provider_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | [**SkipNumber**](.md)|  | [optional] 
 **take** | [**TakeNumber**](.md)|  | [optional] 
 **order** | [**AgentProviderOrderString**](.md)|  | [optional] 

### Return type

[**PlatformResponseAgentProviderArray_**](PlatformResponseAgentProviderArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_provider_show**
> PlatformResponseAgentProvider_ platform_agent_provider_show(id)



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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    api_response = api_instance.platform_agent_provider_show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_provider_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**IdNumber**](.md)|  | 

### Return type

[**PlatformResponseAgentProvider_**](PlatformResponseAgentProvider_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_service_destroy**
> platform_agent_service_destroy(body)



Deletes agent Services

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = NULL # dict(str, object) | 

try:
    api_instance.platform_agent_service_destroy(body)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_service_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

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



Retrieves agent services.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
agent_ids = [3.4] # list[float] | 

try:
    api_response = api_instance.platform_agent_service_index(agent_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_service_index: %s\n" % e)
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



Updates agent services status

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = NULL # dict(str, object) | 

try:
    api_instance.platform_agent_service_subnet_update(body)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_service_subnet_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_tag_index**
> PlatformResponseAgentTagModelObjectArray_ platform_agent_tag_index()



Get user agent tags.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))

try:
    api_response = api_instance.platform_agent_tag_index()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_tag_index: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PlatformResponseAgentTagModelObjectArray_**](PlatformResponseAgentTagModelObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_update**
> PlatformResponseSuccessBoolean_ platform_agent_update(body, agent_id)



Patches agent.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = NULL # dict(str, object) | 
agent_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    api_response = api_instance.platform_agent_update(body, agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **agent_id** | [**IdNumber**](.md)|  | 

### Return type

[**PlatformResponseSuccessBoolean_**](PlatformResponseSuccessBoolean_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agents_destroy**
> platform_agents_destroy(body)



Deletes `platform agent` ands its `connections`.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.AgentsObject()] # list[AgentsObject] | 

try:
    api_instance.platform_agents_destroy(body)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agents_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AgentsObject]**](AgentsObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_api_key_create**
> PlatformResponseApiKeyObject_ platform_api_key_create(body)



Creates API key.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.platform_api_key_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_api_key_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**PlatformResponseApiKeyObject_**](PlatformResponseApiKeyObject_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_api_key_destroy**
> platform_api_key_destroy(api_key_id)



Deletes API key.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
api_key_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    api_instance.platform_api_key_destroy(api_key_id)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_api_key_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_api_key_index**
> PlatformResponseApiKeyObjectArray_ platform_api_key_index(skip=skip, take=take, order=order, filter=filter)



Get API keys.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
skip = syntropy_sdk.SkipNumber() # SkipNumber |  (optional)
take = syntropy_sdk.TakeNumber() # TakeNumber |  (optional)
order = 'order_example' # str | string: \"ASC\" | \"DESC\" (optional)
filter = 'filter_example' # str | api_key_id: string, api_key_name: string (optional)

try:
    api_response = api_instance.platform_api_key_index(skip=skip, take=take, order=order, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_api_key_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | [**SkipNumber**](.md)|  | [optional] 
 **take** | [**TakeNumber**](.md)|  | [optional] 
 **order** | **str**| string: \&quot;ASC\&quot; | \&quot;DESC\&quot; | [optional] 
 **filter** | **str**| api_key_id: string, api_key_name: string | [optional] 

### Return type

[**PlatformResponseApiKeyObjectArray_**](PlatformResponseApiKeyObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_config**
> PlatformResponseAgentWgConfig_ platform_config(agent_id)



Returns `platform agent` `WireGuard` configuration.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
agent_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    api_response = api_instance.platform_config(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**IdNumber**](.md)|  | 

### Return type

[**PlatformResponseAgentWgConfig_**](PlatformResponseAgentWgConfig_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_agent_destroy**
> platform_connection_agent_destroy(agent_id)



Deletes agent `connections`. Does not remove `platform agent` from `networks`.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
agent_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    api_instance.platform_connection_agent_destroy(agent_id)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_agent_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_agents_destroy**
> platform_connection_agents_destroy(body)



Deletes agent `connections`. Does not remove `platform agent` from `networks`.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.AgentsObject()] # list[AgentsObject] | 

try:
    api_instance.platform_connection_agents_destroy(body)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_agents_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AgentsObject]**](AgentsObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_create**
> PlatformResponseAgentConnectionObjectArray_ platform_connection_create(body, paths=paths)



Creates agents connections. If connection type is POINT_TO_POINT, then agent_ids should contain pairs of ids, i.e.: [[1,2], [2,3], ...]. In other types of networks a flat array of ids should be passed, i.e.: [1, 2, 3, ...].

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = {
  "value" : {
    "agent_ids" : [ 1, 2 ]
  }
} # dict(str, object) | 
paths = ['paths_example'] # list[str] | Comma separated servers ids list for SDN path. (optional)

try:
    api_response = api_instance.platform_connection_create(body, paths=paths)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **paths** | [**list[str]**](str.md)| Comma separated servers ids list for SDN path. | [optional] 

### Return type

[**PlatformResponseAgentConnectionObjectArray_**](PlatformResponseAgentConnectionObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_create_mesh**
> PlatformResponseAgentConnectionObjectArray_ platform_connection_create_mesh(body, paths=paths)



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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = NULL # dict(str, object) | 
paths = ['paths_example'] # list[str] | Comma separated servers ids list for SDN path. (optional)

try:
    api_response = api_instance.platform_connection_create_mesh(body, paths=paths)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_create_mesh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **paths** | [**list[str]**](str.md)| Comma separated servers ids list for SDN path. | [optional] 

### Return type

[**PlatformResponseAgentConnectionObjectArray_**](PlatformResponseAgentConnectionObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_create_p2_t**
> PlatformResponseAgentConnectionObjectArray_ platform_connection_create_p2_t(body, paths=paths)



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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = NULL # dict(str, object) | 
paths = ['paths_example'] # list[str] | Comma separated servers ids list for SDN path. (optional)

try:
    api_response = api_instance.platform_connection_create_p2_t(body, paths=paths)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_create_p2_t: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **paths** | [**list[str]**](str.md)| Comma separated servers ids list for SDN path. | [optional] 

### Return type

[**PlatformResponseAgentConnectionObjectArray_**](PlatformResponseAgentConnectionObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_create_p2p**
> PlatformResponseAgentConnectionObjectArray_ platform_connection_create_p2p(body, paths=paths)



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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = NULL # dict(str, object) | 
paths = ['paths_example'] # list[str] | Comma separated servers ids list for SDN path. (optional)

try:
    api_response = api_instance.platform_connection_create_p2p(body, paths=paths)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_create_p2p: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **paths** | [**list[str]**](str.md)| Comma separated servers ids list for SDN path. | [optional] 

### Return type

[**PlatformResponseAgentConnectionObjectArray_**](PlatformResponseAgentConnectionObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_destroy**
> platform_connection_destroy(body)



Deletes `connections` by supplied pairs of `platform agents`.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.AgentsPairObject()] # list[AgentsPairObject] | 

try:
    api_instance.platform_connection_destroy(body)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AgentsPairObject]**](AgentsPairObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_destroy_deprecated**
> platform_connection_destroy_deprecated(connection_id)



Removes agent pair (agent1, agent2) connections (PUBLIC, SDN{1,2,3}).

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
connection_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    api_instance.platform_connection_destroy_deprecated(connection_id)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_destroy_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_index**
> PlatformResponseAgentConnectionFindAndCountObjectArray_ platform_connection_index(skip=skip, take=take, order=order, filter=filter, show_sdn_connections=show_sdn_connections, load_relations=load_relations)



Retrieves connections.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
skip = syntropy_sdk.SkipNumber() # SkipNumber |  (optional)
take = syntropy_sdk.TakeNumber() # TakeNumber |  (optional)
order = syntropy_sdk.OrderString() # OrderString | string: \"ASC\" | \"DESC\" (optional)
filter = syntropy_sdk.WhereString() # WhereString | id|name: string, example: \"1\" or \"name\", connectionId: string, example: \"1\", name: exact agent name, example: \"name1\", agent_ids[]: array of agent ids, example: \"1;2;3\", statuses[]: array of statuses, one of PENDING, WARNING, ERROR, CONNECTED, OFFLINE, example: \"OFFLINE;ERROR;WARNING\", providers[]: array of providers ids, example: \"1;2;3\", agent_connection_updated_at_from: date from which connection was last modified, agent_connection_updated_at_to: date to which connection was last modified (optional)
show_sdn_connections = syntropy_sdk.ShowSdnConnections() # ShowSdnConnections |  (optional)
load_relations = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.platform_connection_index(skip=skip, take=take, order=order, filter=filter, show_sdn_connections=show_sdn_connections, load_relations=load_relations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | [**SkipNumber**](.md)|  | [optional] 
 **take** | [**TakeNumber**](.md)|  | [optional] 
 **order** | [**OrderString**](.md)| string: \&quot;ASC\&quot; | \&quot;DESC\&quot; | [optional] 
 **filter** | [**WhereString**](.md)| id|name: string, example: \&quot;1\&quot; or \&quot;name\&quot;, connectionId: string, example: \&quot;1\&quot;, name: exact agent name, example: \&quot;name1\&quot;, agent_ids[]: array of agent ids, example: \&quot;1;2;3\&quot;, statuses[]: array of statuses, one of PENDING, WARNING, ERROR, CONNECTED, OFFLINE, example: \&quot;OFFLINE;ERROR;WARNING\&quot;, providers[]: array of providers ids, example: \&quot;1;2;3\&quot;, agent_connection_updated_at_from: date from which connection was last modified, agent_connection_updated_at_to: date to which connection was last modified | [optional] 
 **show_sdn_connections** | [**ShowSdnConnections**](.md)|  | [optional] 
 **load_relations** | **bool**|  | [optional] [default to true]

### Return type

[**PlatformResponseAgentConnectionFindAndCountObjectArray_**](PlatformResponseAgentConnectionFindAndCountObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_service_show**
> PlatformResponseAgentConnectionWithServicesObjectArray_ platform_connection_service_show(connection_ids)



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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
connection_ids = [3.4] # list[float] | 

try:
    api_response = api_instance.platform_connection_service_show(connection_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_service_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_ids** | [**list[float]**](float.md)|  | 

### Return type

[**PlatformResponseAgentConnectionWithServicesObjectArray_**](PlatformResponseAgentConnectionWithServicesObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_service_update**
> platform_connection_service_update(body)



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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = NULL # dict(str, object) | 

try:
    api_instance.platform_connection_service_update(body)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_service_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = NULL # dict(str, object) | 

try:
    api_instance.platform_connection_subnet_destroy(body)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_subnet_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_logs_read_timestamp**
> platform_logs_read_timestamp(body)



Save last logs read timestamp.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.LogsReadTimestampObject()] # list[LogsReadTimestampObject] | 

try:
    api_instance.platform_logs_read_timestamp(body)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_logs_read_timestamp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[LogsReadTimestampObject]**](LogsReadTimestampObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_info**
> PlatformResponseNetworkInfoObject_ platform_network_info()



Get network info.

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
api_instance = syntropy_sdk.PlatformApi(syntropy_sdk.ApiClient(configuration))

try:
    api_response = api_instance.platform_network_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PlatformResponseNetworkInfoObject_**](PlatformResponseNetworkInfoObject_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

