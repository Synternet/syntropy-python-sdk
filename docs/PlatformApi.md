# syntropy_sdk.PlatformApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_admin_config**](PlatformApi.md#platform_admin_config) | **GET** /api/platform/admin/agent/{agent_id}/config | 
[**platform_agent_coordinates**](PlatformApi.md#platform_agent_coordinates) | **GET** /api/platform/agents/coordinates | 
[**platform_agent_create**](PlatformApi.md#platform_agent_create) | **POST** /api/platform/agents | 
[**platform_agent_destroy**](PlatformApi.md#platform_agent_destroy) | **DELETE** /api/platform/agents/{agent_id} | 
[**platform_agent_group_destroy**](PlatformApi.md#platform_agent_group_destroy) | **DELETE** /api/platform/network/agent-groups/{group_id} | 
[**platform_agent_group_update**](PlatformApi.md#platform_agent_group_update) | **PUT** /api/platform/network/agent-groups/{group_id} | 
[**platform_agent_id_name_pairs**](PlatformApi.md#platform_agent_id_name_pairs) | **GET** /api/platform/agents/filters | 
[**platform_agent_index**](PlatformApi.md#platform_agent_index) | **GET** /api/platform/agents | 
[**platform_agent_provider_index**](PlatformApi.md#platform_agent_provider_index) | **GET** /api/platform/agent-providers | 
[**platform_agent_provider_show**](PlatformApi.md#platform_agent_provider_show) | **GET** /api/platform/agent-providers/{id} | 
[**platform_agent_service_destroy**](PlatformApi.md#platform_agent_service_destroy) | **POST** /api/platform/agent-services-delete | 
[**platform_agent_service_index**](PlatformApi.md#platform_agent_service_index) | **GET** /api/platform/agent-services | 
[**platform_agent_service_subnet_update**](PlatformApi.md#platform_agent_service_subnet_update) | **POST** /api/platform/agent-services-subnets | 
[**platform_agent_tag_index**](PlatformApi.md#platform_agent_tag_index) | **GET** /api/platform/agent-tags | 
[**platform_agent_update**](PlatformApi.md#platform_agent_update) | **PATCH** /api/platform/agents/{agent_id} | 
[**platform_api_key_create**](PlatformApi.md#platform_api_key_create) | **POST** /api/platform/api-keys | 
[**platform_api_key_destroy**](PlatformApi.md#platform_api_key_destroy) | **DELETE** /api/platform/api-keys/{api_key_id} | 
[**platform_api_key_index**](PlatformApi.md#platform_api_key_index) | **GET** /api/platform/api-keys | 
[**platform_api_key_update**](PlatformApi.md#platform_api_key_update) | **PATCH** /api/platform/api-keys/{api_key_id} | 
[**platform_config**](PlatformApi.md#platform_config) | **GET** /api/platform/agent/{agent_id}/wg-config | 
[**platform_connection_agent_destroy**](PlatformApi.md#platform_connection_agent_destroy) | **DELETE** /api/platform/connections/agents/{agent_id} | 
[**platform_connection_create**](PlatformApi.md#platform_connection_create) | **POST** /api/platform/connections | 
[**platform_connection_create_mesh**](PlatformApi.md#platform_connection_create_mesh) | **POST** /api/platform/connections/mesh | 
[**platform_connection_create_p2p**](PlatformApi.md#platform_connection_create_p2p) | **POST** /api/platform/connections/point-to-point | 
[**platform_connection_destroy**](PlatformApi.md#platform_connection_destroy) | **POST** /api/platform/connections/remove | 
[**platform_connection_destroy_deprecated**](PlatformApi.md#platform_connection_destroy_deprecated) | **DELETE** /api/platform/connections/{connection_id} | 
[**platform_connection_index**](PlatformApi.md#platform_connection_index) | **GET** /api/platform/connections | 
[**platform_connection_service_show**](PlatformApi.md#platform_connection_service_show) | **GET** /api/platform/connection-services | 
[**platform_connection_service_update**](PlatformApi.md#platform_connection_service_update) | **POST** /api/platform/connection-services | 
[**platform_connection_subnet_destroy**](PlatformApi.md#platform_connection_subnet_destroy) | **POST** /api/platform/connection-services-delete | 
[**platform_logs_read_timestamp**](PlatformApi.md#platform_logs_read_timestamp) | **POST** /api/platform/logs-reads-timestamp | 
[**platform_network_agent_create**](PlatformApi.md#platform_network_agent_create) | **POST** /api/platform/network/{network_id}/agents/add | 
[**platform_network_agent_create_deprecated**](PlatformApi.md#platform_network_agent_create_deprecated) | **POST** /api/platform/network/{network_id}/agents | 
[**platform_network_agent_destroy**](PlatformApi.md#platform_network_agent_destroy) | **DELETE** /api/platform/networks/{network_id}/agents/{agent_id} | 
[**platform_network_agent_group_create**](PlatformApi.md#platform_network_agent_group_create) | **POST** /api/platform/network/{network_id}/agent-groups/{group_name} | 
[**platform_network_agent_remove**](PlatformApi.md#platform_network_agent_remove) | **POST** /api/platform/networks/{network_id}/agents/remove | 
[**platform_network_agent_remove_deprecated**](PlatformApi.md#platform_network_agent_remove_deprecated) | **DELETE** /api/platform/networks/{network_id}/agents | 
[**platform_network_create**](PlatformApi.md#platform_network_create) | **POST** /api/platform/networks | 
[**platform_network_destroy**](PlatformApi.md#platform_network_destroy) | **DELETE** /api/platform/networks/{network_id} | 
[**platform_network_index**](PlatformApi.md#platform_network_index) | **GET** /api/platform/networks | 
[**platform_network_info**](PlatformApi.md#platform_network_info) | **GET** /api/platform/network/{network_id}/info | 
[**platform_network_network_agent_destroy_deprecated**](PlatformApi.md#platform_network_network_agent_destroy_deprecated) | **POST** /api/platform/network/{network_id}/agents/delete | 
[**platform_network_topology**](PlatformApi.md#platform_network_topology) | **GET** /api/platform/networks/topology | 

# **platform_admin_config**
> PlatformResponseAdminAgentConfig_ platform_admin_config(agent_id)



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
agent_id = 1.2 # float | 

try:
    api_response = api_instance.platform_admin_config(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_admin_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **float**|  | 

### Return type

[**PlatformResponseAdminAgentConfig_**](PlatformResponseAdminAgentConfig_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_coordinates**
> PlatformResponseAgentCoordinatesObjectArray_ platform_agent_coordinates(agent_ids)



Get Platform agent location coordinates

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
    api_response = api_instance.platform_agent_coordinates(agent_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_coordinates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_ids** | [**list[float]**](float.md)|  | 

### Return type

[**PlatformResponseAgentCoordinatesObjectArray_**](PlatformResponseAgentCoordinatesObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_create**
> PlatformResponseAgentObject_ platform_agent_create(body)



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

[**PlatformResponseAgentObject_**](PlatformResponseAgentObject_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_destroy**
> InlineResponse204 platform_agent_destroy(agent_id)



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
agent_id = 1.2 # float | 

try:
    api_response = api_instance.platform_agent_destroy(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_group_destroy**
> InlineResponse204 platform_agent_group_destroy(group_id)



Remove agent group.

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
group_id = 1.2 # float | 

try:
    api_response = api_instance.platform_agent_group_destroy(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_group_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_group_update**
> InlineResponse204 platform_agent_group_update(body, group_id)



Update network agents group.

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
body = [3.4] # list[float] | 
group_id = 1.2 # float | 

try:
    api_response = api_instance.platform_agent_group_update(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_group_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[float]**](float.md)|  | 
 **group_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

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
filter = 'filter_example' # str | ids[]: array of agent ids, example: \"1;2;3\", id|name: agent id or agent name, example: \"name1\" or \"132\", name: exact agent name, example: \"name1\", statuses[]: one of: connected, connected_with_errors, disconnected, example: \"connected;connected_with_errors\", networks[]: array of network ids, example: \"1;2;3\", providers[]: array of providers ids, example: \"1;2;3\", tags[]: array of tags ids, example: \"1;2;3\", tags_names[]: array of tags name, example: \"name1;name2;name3\", networks_names[]: array of networks names, example: \"name1;name2;name3\", connected[]: boolean to check if agent belongs to connection, example: \"true\", (optional)

try:
    api_response = api_instance.platform_agent_id_name_pairs(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_id_name_pairs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| ids[]: array of agent ids, example: \&quot;1;2;3\&quot;, id|name: agent id or agent name, example: \&quot;name1\&quot; or \&quot;132\&quot;, name: exact agent name, example: \&quot;name1\&quot;, statuses[]: one of: connected, connected_with_errors, disconnected, example: \&quot;connected;connected_with_errors\&quot;, networks[]: array of network ids, example: \&quot;1;2;3\&quot;, providers[]: array of providers ids, example: \&quot;1;2;3\&quot;, tags[]: array of tags ids, example: \&quot;1;2;3\&quot;, tags_names[]: array of tags name, example: \&quot;name1;name2;name3\&quot;, networks_names[]: array of networks names, example: \&quot;name1;name2;name3\&quot;, connected[]: boolean to check if agent belongs to connection, example: \&quot;true\&quot;, | [optional] 

### Return type

[**PlatformResponseAgentFiltersObject_**](PlatformResponseAgentFiltersObject_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_index**
> PlatformResponseAgentObjectArray_ platform_agent_index(skip=skip, take=take, order=order, filter=filter, load_relations=load_relations, show_logs_state=show_logs_state)



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
skip = 1.2 # float |  (optional)
take = 1.2 # float |  (optional)
order = 'order_example' # str | string: \"ASC\" | \"DESC\" (optional)
filter = 'filter_example' # str | ids[]: array of agent ids, example: \"1;2;3\", id|name: agent id or agent name, example: \"name1\" or \"132\", name: exact agent name, example: \"name1\", statuses[]: one of: connected, connected_with_errors, disconnected, example: \"connected;connected_with_errors\", networks[]: array of network ids, example: \"0;1;2;3\", providers[]: array of providers ids, example: \"0;1;2;3\", tags[]: array of tags ids, example: \"0;1;2;3\", tags_names[]: array of tags name, example: \"name1;name2;name3\", networks_names[]: array of networks names, example: \"name1;name2;name3\", agent_modified_at_from: date from which agent was last modified agent_modified_at_to: date to which agent was last modified agent_versions[]: array of agent versions, example: \"0.0.75;0.0.74\" locations[]: array of locations, example: \"ES;US\" (optional)
load_relations = true # bool |  (optional) (default to true)
show_logs_state = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.platform_agent_index(skip=skip, take=take, order=order, filter=filter, load_relations=load_relations, show_logs_state=show_logs_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**|  | [optional] 
 **take** | **float**|  | [optional] 
 **order** | **str**| string: \&quot;ASC\&quot; | \&quot;DESC\&quot; | [optional] 
 **filter** | **str**| ids[]: array of agent ids, example: \&quot;1;2;3\&quot;, id|name: agent id or agent name, example: \&quot;name1\&quot; or \&quot;132\&quot;, name: exact agent name, example: \&quot;name1\&quot;, statuses[]: one of: connected, connected_with_errors, disconnected, example: \&quot;connected;connected_with_errors\&quot;, networks[]: array of network ids, example: \&quot;0;1;2;3\&quot;, providers[]: array of providers ids, example: \&quot;0;1;2;3\&quot;, tags[]: array of tags ids, example: \&quot;0;1;2;3\&quot;, tags_names[]: array of tags name, example: \&quot;name1;name2;name3\&quot;, networks_names[]: array of networks names, example: \&quot;name1;name2;name3\&quot;, agent_modified_at_from: date from which agent was last modified agent_modified_at_to: date to which agent was last modified agent_versions[]: array of agent versions, example: \&quot;0.0.75;0.0.74\&quot; locations[]: array of locations, example: \&quot;ES;US\&quot; | [optional] 
 **load_relations** | **bool**|  | [optional] [default to true]
 **show_logs_state** | **bool**|  | [optional] [default to false]

### Return type

[**PlatformResponseAgentObjectArray_**](PlatformResponseAgentObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_provider_index**
> PlatformResponseAgentProviderObjectArray_ platform_agent_provider_index(skip=skip, take=take, order=order, filter=filter)



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
skip = 1.2 # float |  (optional)
take = 1.2 # float |  (optional)
order = 'order_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)

try:
    api_response = api_instance.platform_agent_provider_index(skip=skip, take=take, order=order, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_provider_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**|  | [optional] 
 **take** | **float**|  | [optional] 
 **order** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**PlatformResponseAgentProviderObjectArray_**](PlatformResponseAgentProviderObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_provider_show**
> PlatformResponseAgentProviderObject_ platform_agent_provider_show(id)



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
id = 1.2 # float | 

try:
    api_response = api_instance.platform_agent_provider_show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_agent_provider_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**PlatformResponseAgentProviderObject_**](PlatformResponseAgentProviderObject_.md)

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
> PlatformResponseAgentServiceObjectArray_ platform_agent_service_index(agent_ids)



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

[**PlatformResponseAgentServiceObjectArray_**](PlatformResponseAgentServiceObjectArray_.md)

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
> PlatformResponseAgentTagObjectArray_ platform_agent_tag_index()



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

[**PlatformResponseAgentTagObjectArray_**](PlatformResponseAgentTagObjectArray_.md)

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
agent_id = 1.2 # float | 

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
 **agent_id** | **float**|  | 

### Return type

[**PlatformResponseSuccessBoolean_**](PlatformResponseSuccessBoolean_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

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
> InlineResponse204 platform_api_key_destroy(api_key_id)



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
api_key_id = 1.2 # float | 

try:
    api_response = api_instance.platform_api_key_destroy(api_key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_api_key_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
skip = 1.2 # float |  (optional)
take = 1.2 # float |  (optional)
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
 **skip** | **float**|  | [optional] 
 **take** | **float**|  | [optional] 
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

# **platform_api_key_update**
> InlineResponse204 platform_api_key_update(body, api_key_id)



Updates API key.

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
api_key_id = 1.2 # float | 

try:
    api_response = api_instance.platform_api_key_update(body, api_key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_api_key_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **api_key_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_config**
> PlatformResponse5BLinkTagPublic5D3F3Astring5BLinkTagSdn15D3F3Astring5BLinkTagSdn25D3F3Astring5BLinkTagSdn35D3F3Astring_ platform_config(agent_id)



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
agent_id = 1.2 # float | 

try:
    api_response = api_instance.platform_config(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **float**|  | 

### Return type

[**PlatformResponse5BLinkTagPublic5D3F3Astring5BLinkTagSdn15D3F3Astring5BLinkTagSdn25D3F3Astring5BLinkTagSdn35D3F3Astring_**](PlatformResponse5BLinkTagPublic5D3F3Astring5BLinkTagSdn15D3F3Astring5BLinkTagSdn25D3F3Astring5BLinkTagSdn35D3F3Astring_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_agent_destroy**
> InlineResponse204 platform_connection_agent_destroy(agent_id)



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
agent_id = 1.2 # float | 

try:
    api_response = api_instance.platform_connection_agent_destroy(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_agent_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
    "agent_ids" : [ 1, 2 ],
    "network_id" : 1
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
> InlineResponse204 platform_connection_destroy(body, network_updated_by=network_updated_by)



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
network_updated_by = syntropy_sdk.NetworkGenesisType() # NetworkGenesisType |  (optional)

try:
    api_response = api_instance.platform_connection_destroy(body, network_updated_by=network_updated_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AgentsPairObject]**](AgentsPairObject.md)|  | 
 **network_updated_by** | [**NetworkGenesisType**](.md)|  | [optional] 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_destroy_deprecated**
> InlineResponse204 platform_connection_destroy_deprecated(connection_id, network_updated_by=network_updated_by)



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
connection_id = 1.2 # float | 
network_updated_by = syntropy_sdk.NetworkGenesisType() # NetworkGenesisType |  (optional)

try:
    api_response = api_instance.platform_connection_destroy_deprecated(connection_id, network_updated_by=network_updated_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_connection_destroy_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **float**|  | 
 **network_updated_by** | [**NetworkGenesisType**](.md)|  | [optional] 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_index**
> PlatformResponseAgentConnectionObjectArray_ platform_connection_index(skip=skip, take=take, order=order, filter=filter, show_sdn_connections=show_sdn_connections, load_relations=load_relations)



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
skip = 1.2 # float |  (optional)
take = 1.2 # float |  (optional)
order = 'order_example' # str | string: \"ASC\" | \"DESC\" (optional)
filter = 'filter_example' # str | id|name: string, example: \"1\" or \"name\", name: exact agent name, example: \"name1\", agent_ids[]: array of agent ids, example: \"1;2;3\", statuses[]: array of statuses, one of PENDING, WARNING, ERROR, CONNECTED, OFFLINE, example: \"OFFLINE;ERROR;WARNING\", networks[]: array of networks ids, example: \"1;2;3\", providers[]: array of providers ids, example: \"1;2;3\", agent_connection_updated_at_from: date from which connection was last modified, agent_connection_updated_at_to: date to which connection was last modified (optional)
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
 **skip** | **float**|  | [optional] 
 **take** | **float**|  | [optional] 
 **order** | **str**| string: \&quot;ASC\&quot; | \&quot;DESC\&quot; | [optional] 
 **filter** | **str**| id|name: string, example: \&quot;1\&quot; or \&quot;name\&quot;, name: exact agent name, example: \&quot;name1\&quot;, agent_ids[]: array of agent ids, example: \&quot;1;2;3\&quot;, statuses[]: array of statuses, one of PENDING, WARNING, ERROR, CONNECTED, OFFLINE, example: \&quot;OFFLINE;ERROR;WARNING\&quot;, networks[]: array of networks ids, example: \&quot;1;2;3\&quot;, providers[]: array of providers ids, example: \&quot;1;2;3\&quot;, agent_connection_updated_at_from: date from which connection was last modified, agent_connection_updated_at_to: date to which connection was last modified | [optional] 
 **show_sdn_connections** | [**ShowSdnConnections**](.md)|  | [optional] 
 **load_relations** | **bool**|  | [optional] [default to true]

### Return type

[**PlatformResponseAgentConnectionObjectArray_**](PlatformResponseAgentConnectionObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_service_show**
> PlatformResponseAgentConnectionObjectArray_ platform_connection_service_show(connection_ids)



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

[**PlatformResponseAgentConnectionObjectArray_**](PlatformResponseAgentConnectionObjectArray_.md)

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



Deletes agent connection services/subnets

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
> InlineResponse204 platform_logs_read_timestamp(body)



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
    api_response = api_instance.platform_logs_read_timestamp(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_logs_read_timestamp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[LogsReadTimestampObject]**](LogsReadTimestampObject.md)|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_agent_create**
> InlineResponse204 platform_network_agent_create(body, network_id)



Adds agents to network without modifying connections.

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
body = [syntropy_sdk.NetworkAgentPayload()] # list[NetworkAgentPayload] | 
network_id = 1.2 # float | 

try:
    api_response = api_instance.platform_network_agent_create(body, network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_agent_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[NetworkAgentPayload]**](NetworkAgentPayload.md)|  | 
 **network_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_agent_create_deprecated**
> InlineResponse204 platform_network_agent_create_deprecated(body, network_id)



Adds `platform agents` to `network` view. Does not modify `connections`.

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
body = [syntropy_sdk.NetworkAgentPayload()] # list[NetworkAgentPayload] | 
network_id = 1.2 # float | 

try:
    api_response = api_instance.platform_network_agent_create_deprecated(body, network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_agent_create_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[NetworkAgentPayload]**](NetworkAgentPayload.md)|  | 
 **network_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_agent_destroy**
> InlineResponse204 platform_network_agent_destroy(network_id, agent_id)



Removes agent from network view and connections associated with it.

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
network_id = 1.2 # float | 
agent_id = 1.2 # float | 

try:
    api_response = api_instance.platform_network_agent_destroy(network_id, agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_agent_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **float**|  | 
 **agent_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_agent_group_create**
> InlineResponse204 platform_network_agent_group_create(network_id, group_name, body=body)



Creates agent group relation.

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
network_id = 1.2 # float | 
group_name = 'group_name_example' # str | 
body = [3.4] # list[float] |  (optional)

try:
    api_response = api_instance.platform_network_agent_group_create(network_id, group_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_agent_group_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **float**|  | 
 **group_name** | **str**|  | 
 **body** | [**list[float]**](float.md)|  | [optional] 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_agent_remove**
> InlineResponse204 platform_network_agent_remove(body, network_id)



Remove agents from network view without unconfiguring connections.

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
body = [3.4] # list[float] | 
network_id = 1.2 # float | 

try:
    api_response = api_instance.platform_network_agent_remove(body, network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_agent_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[float]**](float.md)|  | 
 **network_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_agent_remove_deprecated**
> InlineResponse204 platform_network_agent_remove_deprecated(body, network_id)



Remove `platform agents` from `network` view. Does not modify `connections`.

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
body = [3.4] # list[float] | 
network_id = 1.2 # float | 

try:
    api_response = api_instance.platform_network_agent_remove_deprecated(body, network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_agent_remove_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[float]**](float.md)|  | 
 **network_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_create**
> PlatformResponseNetworkObject_ platform_network_create(body)



Creates network.

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
    api_response = api_instance.platform_network_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**PlatformResponseNetworkObject_**](PlatformResponseNetworkObject_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_destroy**
> InlineResponse204 platform_network_destroy(network_id)



Deletes `network`. Does not modify `connections`.

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
network_id = 1.2 # float | 

try:
    api_response = api_instance.platform_network_destroy(network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_index**
> PlatformResponseNetworkObjectArray_ platform_network_index(skip=skip, take=take, order=order, filter=filter)



Retrieves networks.

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
skip = 1.2 # float |  (optional)
take = 1.2 # float |  (optional)
order = 'order_example' # str | string: \"ASC\" | \"DESC\" (optional)
filter = 'filter_example' # str | id|name: string, name: string, (optional)

try:
    api_response = api_instance.platform_network_index(skip=skip, take=take, order=order, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**|  | [optional] 
 **take** | **float**|  | [optional] 
 **order** | **str**| string: \&quot;ASC\&quot; | \&quot;DESC\&quot; | [optional] 
 **filter** | **str**| id|name: string, name: string, | [optional] 

### Return type

[**PlatformResponseNetworkObjectArray_**](PlatformResponseNetworkObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_info**
> PlatformResponseNetworkInfoObject_ platform_network_info(network_id)



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
network_id = 1.2 # float | 

try:
    api_response = api_instance.platform_network_info(network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **float**|  | 

### Return type

[**PlatformResponseNetworkInfoObject_**](PlatformResponseNetworkInfoObject_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_network_agent_destroy_deprecated**
> InlineResponse204 platform_network_network_agent_destroy_deprecated(body, network_id)



Removes network agents.

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
body = [3.4] # list[float] | 
network_id = 1.2 # float | 

try:
    api_response = api_instance.platform_network_network_agent_destroy_deprecated(body, network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_network_agent_destroy_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[float]**](float.md)|  | 
 **network_id** | **float**|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_network_topology**
> PlatformResponseNetworkTopologyObjectArray_ platform_network_topology(network_id=network_id)



Retrieves networks topology.

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
network_id = 1.2 # float |  (optional)

try:
    api_response = api_instance.platform_network_topology(network_id=network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **float**|  | [optional] 

### Return type

[**PlatformResponseNetworkTopologyObjectArray_**](PlatformResponseNetworkTopologyObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

