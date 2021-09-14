# syntropy_sdk.AgentsApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_agent_config**](AgentsApi.md#platform_agent_config) | **GET** /api/platform/agent/{agent_id}/config | Get agent config
[**platform_agent_coordinates**](AgentsApi.md#platform_agent_coordinates) | **POST** /api/platform/agents/coordinates | Get coordinates
[**platform_agent_create**](AgentsApi.md#platform_agent_create) | **POST** /api/platform/agents | Create agent
[**platform_agent_id_name_pairs**](AgentsApi.md#platform_agent_id_name_pairs) | **GET** /api/platform/agents/filters | Get agents (id,name)
[**platform_agent_index**](AgentsApi.md#platform_agent_index) | **GET** /api/platform/agents | Get agents
[**platform_agent_provider_index**](AgentsApi.md#platform_agent_provider_index) | **GET** /api/platform/agent-providers | Get agent providers
[**platform_agent_provider_show**](AgentsApi.md#platform_agent_provider_show) | **GET** /api/platform/agent-providers/{id} | Get agent provider
[**platform_agent_tag_index**](AgentsApi.md#platform_agent_tag_index) | **GET** /api/platform/agent-tags | Get agent tags
[**platform_agent_update**](AgentsApi.md#platform_agent_update) | **PATCH** /api/platform/agents/{agent_id} | Update agent
[**platform_agents_destroy**](AgentsApi.md#platform_agents_destroy) | **POST** /api/platform/agents/remove | Delete agent
[**platform_config**](AgentsApi.md#platform_config) | **GET** /api/platform/agent/{agent_id}/wg-config | Get agent wg config
[**platform_logs_read_timestamp**](AgentsApi.md#platform_logs_read_timestamp) | **POST** /api/platform/logs-reads-timestamp | Get logs reads timestamps
[**v1_platform_delete_agents**](AgentsApi.md#v1_platform_delete_agents) | **POST** /api/platform/v1/agents/delete | Delete Agents
[**v1_platform_get_agents**](AgentsApi.md#v1_platform_get_agents) | **POST** /api/platform/v1/agents | Get Agents

# **platform_agent_config**
> PlatformResponseAdminAgentConfig_ platform_agent_config(agent_id)

Get agent config

Show agent configuration details.

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
agent_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Get agent config
    api_response = api_instance.platform_agent_config(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_agent_config: %s\n" % e)
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

Get coordinates

Retrieves agent location coordinates

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.AgentsCoordinatesBody() # AgentsCoordinatesBody | 

try:
    # Get coordinates
    api_response = api_instance.platform_agent_coordinates(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_agent_coordinates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentsCoordinatesBody**](AgentsCoordinatesBody.md)|  | 

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

Create agent

Create new agent. Only `VIRTUAL` agents creation is supported. Not `VIRTUAL` agents are automatically created when first WebSocket connection is established.

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.UserAgentCreateObject() # UserAgentCreateObject | 

try:
    # Create agent
    api_response = api_instance.platform_agent_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_agent_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAgentCreateObject**](UserAgentCreateObject.md)|  | 

### Return type

[**PlatformResponseAgentCreateAgentObject_**](PlatformResponseAgentCreateAgentObject_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_agent_id_name_pairs**
> PlatformResponseAgentFiltersObject_ platform_agent_id_name_pairs(filter=filter)

Get agents (id,name)

Get all agents names and ids.

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
filter = syntropy_sdk.WhereString() # WhereString | ids[]: array of agent ids, example: \"1;2;3\", id|name: agent id or agent name, example: \"name1\" or \"132\", name: exact agent name, example: \"name1\", statuses[]: one of: connected, connected_with_errors, disconnected, example: \"connected;connected_with_errors\", providers[]: array of providers ids, example: \"1;2;3\", tags[]: array of tags ids, example: \"1;2;3\", tags_names[]: array of tags name, example: \"name1;name2;name3\", connected[]: boolean to check if agent belongs to connection, example: \"true\", (optional)

try:
    # Get agents (id,name)
    api_response = api_instance.platform_agent_id_name_pairs(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_agent_id_name_pairs: %s\n" % e)
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

Get agents

Agents index.

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
skip = syntropy_sdk.SkipNumber() # SkipNumber |  (optional)
take = syntropy_sdk.TakeNumber() # TakeNumber |  (optional)
order = syntropy_sdk.OrderString() # OrderString | string: \"ASC\" | \"DESC\" (optional)
filter = syntropy_sdk.WhereString() # WhereString | ids[]: array of agent ids, example: \"1;2;3\", id|name: agent id or agent name or ip, example: \"name1\" or \"132\" or \"192.168.0.1\", name: exact agent name, example: \"name1\", types[]: array of agent types, example: Windows;macOS;Linux;Virtual, statuses[]: one of: connected, connected_with_errors, disconnected, example: \"connected;connected_with_errors\", providers[]: array of providers ids, example: \"0;1;2;3\", tags[]: array of tags ids, example: \"0;1;2;3\", tags_names[]: array of tags name, example: \"name1;name2;name3\", agent_modified_at_from: date from which agent was last modified agent_modified_at_to: date to which agent was last modified agent_versions[]: array of agent versions, example: \"0.0.75;0.0.74\" locations[]: array of locations, example: \"ES;US\" (optional)
show_logs_state = false # bool |  (optional) (default to false)

try:
    # Get agents
    api_response = api_instance.platform_agent_index(skip=skip, take=take, order=order, filter=filter, show_logs_state=show_logs_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_agent_index: %s\n" % e)
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

Get agent providers

Agent providers index.

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
skip = syntropy_sdk.SkipNumber() # SkipNumber |  (optional)
take = syntropy_sdk.TakeNumber() # TakeNumber |  (optional)
order = syntropy_sdk.AgentProviderOrderString() # AgentProviderOrderString |  (optional)

try:
    # Get agent providers
    api_response = api_instance.platform_agent_provider_index(skip=skip, take=take, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_agent_provider_index: %s\n" % e)
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

Get agent provider

Show agent provider by id.

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Get agent provider
    api_response = api_instance.platform_agent_provider_show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_agent_provider_show: %s\n" % e)
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

# **platform_agent_tag_index**
> PlatformResponseAgentTagModelObjectArray_ platform_agent_tag_index()

Get agent tags

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))

try:
    # Get agent tags
    api_response = api_instance.platform_agent_tag_index()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_agent_tag_index: %s\n" % e)
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

Update agent

Update agent.

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.UserAgentPatchObject() # UserAgentPatchObject | 
agent_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Update agent
    api_response = api_instance.platform_agent_update(body, agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_agent_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAgentPatchObject**](UserAgentPatchObject.md)|  | 
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

Delete agent

Delete agent and all connections made with this agent.

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.AgentsObject()] # list[AgentsObject] | 

try:
    # Delete agent
    api_instance.platform_agents_destroy(body)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_agents_destroy: %s\n" % e)
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

# **platform_config**
> PlatformResponseAgentWgConfig_ platform_config(agent_id)

Get agent wg config

Returns agent WireGuard configuration.

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
agent_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Get agent wg config
    api_response = api_instance.platform_config(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_config: %s\n" % e)
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

# **platform_logs_read_timestamp**
> platform_logs_read_timestamp(body)

Get logs reads timestamps

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.LogsReadTimestampObject()] # list[LogsReadTimestampObject] | 

try:
    # Get logs reads timestamps
    api_instance.platform_logs_read_timestamp(body)
except ApiException as e:
    print("Exception when calling AgentsApi->platform_logs_read_timestamp: %s\n" % e)
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

# **v1_platform_delete_agents**
> v1_platform_delete_agents(body)

Delete Agents

Delete agents. Connections with other platform agents will be destroyed. Learn more about platform agents [here](https://docs.syntropystack.com/docs/what-is-syntropy-agent).

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.DeleteAgentsRequestV1Inner()] # list[DeleteAgentsRequestV1Inner] | 

try:
    # Delete Agents
    api_instance.v1_platform_delete_agents(body)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_platform_delete_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DeleteAgentsRequestV1Inner]**](DeleteAgentsRequestV1Inner.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_platform_get_agents**
> PlatformResponseV1GetAgentsResponseV1_ v1_platform_get_agents(body)

Get Agents

Return a list of agents. Learn more about platform agents [here](https://docs.syntropystack.com/docs/what-is-syntropy-agent).

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
api_instance = syntropy_sdk.AgentsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.GetAgentsRequestV1() # GetAgentsRequestV1 | 

try:
    # Get Agents
    api_response = api_instance.v1_platform_get_agents(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_platform_get_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetAgentsRequestV1**](GetAgentsRequestV1.md)|  | 

### Return type

[**PlatformResponseV1GetAgentsResponseV1_**](PlatformResponseV1GetAgentsResponseV1_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

