# syntropy_sdk.PlatformApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config**](PlatformApi.md#config) | **GET** /api/platform/admin/agent/{agent_id}/config | 
[**create_agent_group**](PlatformApi.md#create_agent_group) | **POST** /api/platform/network/{network_id}/agent-groups/{group_name} | 
[**create_api_key**](PlatformApi.md#create_api_key) | **POST** /api/platform/api-keys | 
[**create_connections**](PlatformApi.md#create_connections) | **POST** /api/platform/connections | 
[**create_network**](PlatformApi.md#create_network) | **POST** /api/platform/networks | 
[**create_network_agents**](PlatformApi.md#create_network_agents) | **POST** /api/platform/network/{network_id}/agents | 
[**delete_agents**](PlatformApi.md#delete_agents) | **DELETE** /api/platform/agents/{agent_id} | 
[**delete_api_key**](PlatformApi.md#delete_api_key) | **DELETE** /api/platform/api-keys/{api_key_id} | 
[**delete_connection**](PlatformApi.md#delete_connection) | **DELETE** /api/platform/connections/{connection_id} | 
[**delete_networks**](PlatformApi.md#delete_networks) | **DELETE** /api/platform/networks/{network_id} | 
[**delete_networks_agent**](PlatformApi.md#delete_networks_agent) | **DELETE** /api/platform/networks/{network_id}/agents/{agent_id} | 
[**find_all_name_id_pairs_by_user_id**](PlatformApi.md#find_all_name_id_pairs_by_user_id) | **GET** /api/platform/agents/id-name-pairs | 
[**get_agent_services_with_subnets**](PlatformApi.md#get_agent_services_with_subnets) | **GET** /api/platform/agent-services | 
[**get_agent_tags**](PlatformApi.md#get_agent_tags) | **GET** /api/platform/agent-tags | 
[**get_connection_services**](PlatformApi.md#get_connection_services) | **GET** /api/platform/connection-services | 
[**get_network_info**](PlatformApi.md#get_network_info) | **GET** /api/platform/network/{network_id}/info | 
[**index_agents**](PlatformApi.md#index_agents) | **GET** /api/platform/agents | 
[**index_api_key**](PlatformApi.md#index_api_key) | **GET** /api/platform/api-keys | 
[**index_connections**](PlatformApi.md#index_connections) | **GET** /api/platform/connections | 
[**index_networks**](PlatformApi.md#index_networks) | **GET** /api/platform/networks | 
[**patch_agents**](PlatformApi.md#patch_agents) | **PATCH** /api/platform/agents/{agent_id} | 
[**remove_agent_group**](PlatformApi.md#remove_agent_group) | **DELETE** /api/platform/network/agent-groups/{group_id} | 
[**remove_network_agents**](PlatformApi.md#remove_network_agents) | **DELETE** /api/platform/network/{network_id}/agents | 
[**save_logs_read_timestamp**](PlatformApi.md#save_logs_read_timestamp) | **POST** /api/platform/logs-reads-timestamp | 
[**topology_networks**](PlatformApi.md#topology_networks) | **GET** /api/platform/networks/topology | 
[**update_agent_group**](PlatformApi.md#update_agent_group) | **PUT** /api/platform/network/agent-groups/{group_id} | 
[**update_agent_services_subnets_status**](PlatformApi.md#update_agent_services_subnets_status) | **POST** /api/platform/agent-services-subnets | 
[**update_api_key**](PlatformApi.md#update_api_key) | **PATCH** /api/platform/api-keys/{api_key_id} | 
[**update_connection_services**](PlatformApi.md#update_connection_services) | **POST** /api/platform/connection-services | 

# **config**
> PlatformResponseAdminAgentConfig_ config(agent_id)



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
    api_response = api_instance.config(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->config: %s\n" % e)
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

# **create_agent_group**
> InlineResponse204 create_agent_group(network_id, group_name, body=body)



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
    api_response = api_instance.create_agent_group(network_id, group_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->create_agent_group: %s\n" % e)
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

# **create_api_key**
> PlatformResponseApiKeyObject_ create_api_key(body)



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
    api_response = api_instance.create_api_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->create_api_key: %s\n" % e)
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

# **create_connections**
> PlatformResponseAgentConnectionObjectArray_ create_connections(body, show_sdn_connections=show_sdn_connections, update_type=update_type, paths=paths)



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
show_sdn_connections = syntropy_sdk.ShowSdnConnections() # ShowSdnConnections |  (optional)
update_type = syntropy_sdk.UpdateType() # UpdateType |  (optional)
paths = ['paths_example'] # list[str] | Comma separated servers ids list for SDN path. (optional)

try:
    api_response = api_instance.create_connections(body, show_sdn_connections=show_sdn_connections, update_type=update_type, paths=paths)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->create_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **show_sdn_connections** | [**ShowSdnConnections**](.md)|  | [optional] 
 **update_type** | [**UpdateType**](.md)|  | [optional] 
 **paths** | [**list[str]**](str.md)| Comma separated servers ids list for SDN path. | [optional] 

### Return type

[**PlatformResponseAgentConnectionObjectArray_**](PlatformResponseAgentConnectionObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network**
> PlatformResponseNetworkObject_ create_network(body)



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
    api_response = api_instance.create_network(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->create_network: %s\n" % e)
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

# **create_network_agents**
> InlineResponse204 create_network_agents(body, network_id)



Creates network agents.

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
    api_response = api_instance.create_network_agents(body, network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->create_network_agents: %s\n" % e)
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

# **delete_agents**
> InlineResponse204 delete_agents(agent_id)



Deletes agent.

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
    api_response = api_instance.delete_agents(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->delete_agents: %s\n" % e)
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

# **delete_api_key**
> InlineResponse204 delete_api_key(api_key_id)



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
    api_response = api_instance.delete_api_key(api_key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->delete_api_key: %s\n" % e)
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

# **delete_connection**
> InlineResponse204 delete_connection(connection_id, network_updated_by=network_updated_by)



Finds and deletes all tags (PUBLIC, SDN{1,2,3}) same pair connections (agent1, agent2) in network.

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
    api_response = api_instance.delete_connection(connection_id, network_updated_by=network_updated_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->delete_connection: %s\n" % e)
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

# **delete_networks**
> InlineResponse204 delete_networks(network_id)



Deletes network.

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
    api_response = api_instance.delete_networks(network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->delete_networks: %s\n" % e)
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

# **delete_networks_agent**
> InlineResponse204 delete_networks_agent(network_id, agent_id)



Deletes agent from network.

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
    api_response = api_instance.delete_networks_agent(network_id, agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->delete_networks_agent: %s\n" % e)
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

# **find_all_name_id_pairs_by_user_id**
> PlatformResponseAgentNameIdPairArray_ find_all_name_id_pairs_by_user_id()



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
    api_response = api_instance.find_all_name_id_pairs_by_user_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->find_all_name_id_pairs_by_user_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PlatformResponseAgentNameIdPairArray_**](PlatformResponseAgentNameIdPairArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_services_with_subnets**
> PlatformResponseAgentServiceObjectArray_ get_agent_services_with_subnets(agent_ids)



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
    api_response = api_instance.get_agent_services_with_subnets(agent_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->get_agent_services_with_subnets: %s\n" % e)
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

# **get_agent_tags**
> PlatformResponseAgentTagObjectArray_ get_agent_tags()



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
    api_response = api_instance.get_agent_tags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->get_agent_tags: %s\n" % e)
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

# **get_connection_services**
> PlatformResponseAgentConnectionObjectArray_ get_connection_services(connection_ids)



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
    api_response = api_instance.get_connection_services(connection_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->get_connection_services: %s\n" % e)
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

# **get_network_info**
> PlatformResponseNetworkInfoObject_ get_network_info(network_id)



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
    api_response = api_instance.get_network_info(network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->get_network_info: %s\n" % e)
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

# **index_agents**
> PlatformResponseAgentObjectArray_ index_agents(skip=skip, take=take, order=order, filter=filter, load_relations=load_relations, show_logs_state=show_logs_state)



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
filter = 'filter_example' # str | ids[]: array of agent ids, example: \"1;2;3\", id|name: agent id or agent name, example: \"name1\" or \"132\", name: exact agent name, example: \"name1\", statuses[]: one of: connected, connected_with_errors, disconnected, example: \"connected;connected_with_errors\", networks[]: array of network ids, example: \"1;2;3\", providers[]: array of providers ids, example: \"1;2;3\", tags[]: array of tags ids, example: \"1;2;3\", tags_names[]: array of tags name, example: \"name1;name2;name3\", networks_names[]: array of networks names, example: \"name1;name2;name3\", (optional)
load_relations = true # bool |  (optional) (default to true)
show_logs_state = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.index_agents(skip=skip, take=take, order=order, filter=filter, load_relations=load_relations, show_logs_state=show_logs_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->index_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**|  | [optional] 
 **take** | **float**|  | [optional] 
 **order** | **str**| string: \&quot;ASC\&quot; | \&quot;DESC\&quot; | [optional] 
 **filter** | **str**| ids[]: array of agent ids, example: \&quot;1;2;3\&quot;, id|name: agent id or agent name, example: \&quot;name1\&quot; or \&quot;132\&quot;, name: exact agent name, example: \&quot;name1\&quot;, statuses[]: one of: connected, connected_with_errors, disconnected, example: \&quot;connected;connected_with_errors\&quot;, networks[]: array of network ids, example: \&quot;1;2;3\&quot;, providers[]: array of providers ids, example: \&quot;1;2;3\&quot;, tags[]: array of tags ids, example: \&quot;1;2;3\&quot;, tags_names[]: array of tags name, example: \&quot;name1;name2;name3\&quot;, networks_names[]: array of networks names, example: \&quot;name1;name2;name3\&quot;, | [optional] 
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

# **index_api_key**
> PlatformResponseApiKeyObjectArray_ index_api_key(skip=skip, take=take, order=order, filter=filter)



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
    api_response = api_instance.index_api_key(skip=skip, take=take, order=order, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->index_api_key: %s\n" % e)
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

# **index_connections**
> PlatformResponseAgentConnectionObjectArray_ index_connections(skip=skip, take=take, order=order, filter=filter, show_sdn_connections=show_sdn_connections, load_relations=load_relations)



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
filter = 'filter_example' # str | id|name: string, example: \"1\" or \"name\", name: exact agent name, example: \"name1\", agent_ids[]: array of agent ids, example: \"1;2;3\", statuses[]: array of statuses, one of PENDING, WARNING, ERROR, CONNECTED, OFFLINE, example: \"OFFLINE;ERROR;WARNING\", networks[]: array of networks ids, example: \"1;2;3\", providers[]: array of providers ids, example: \"1;2;3\", (optional)
show_sdn_connections = syntropy_sdk.ShowSdnConnections() # ShowSdnConnections |  (optional)
load_relations = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.index_connections(skip=skip, take=take, order=order, filter=filter, show_sdn_connections=show_sdn_connections, load_relations=load_relations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->index_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**|  | [optional] 
 **take** | **float**|  | [optional] 
 **order** | **str**| string: \&quot;ASC\&quot; | \&quot;DESC\&quot; | [optional] 
 **filter** | **str**| id|name: string, example: \&quot;1\&quot; or \&quot;name\&quot;, name: exact agent name, example: \&quot;name1\&quot;, agent_ids[]: array of agent ids, example: \&quot;1;2;3\&quot;, statuses[]: array of statuses, one of PENDING, WARNING, ERROR, CONNECTED, OFFLINE, example: \&quot;OFFLINE;ERROR;WARNING\&quot;, networks[]: array of networks ids, example: \&quot;1;2;3\&quot;, providers[]: array of providers ids, example: \&quot;1;2;3\&quot;, | [optional] 
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

# **index_networks**
> PlatformResponseNetworkObjectArray_ index_networks(skip=skip, take=take, order=order, filter=filter)



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
    api_response = api_instance.index_networks(skip=skip, take=take, order=order, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->index_networks: %s\n" % e)
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

# **patch_agents**
> PlatformResponseSuccessBoolean_ patch_agents(body, agent_id)



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
    api_response = api_instance.patch_agents(body, agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->patch_agents: %s\n" % e)
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

# **remove_agent_group**
> InlineResponse204 remove_agent_group(group_id)



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
    api_response = api_instance.remove_agent_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->remove_agent_group: %s\n" % e)
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

# **remove_network_agents**
> InlineResponse204 remove_network_agents(body, network_id)



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
    api_response = api_instance.remove_network_agents(body, network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->remove_network_agents: %s\n" % e)
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

# **save_logs_read_timestamp**
> InlineResponse204 save_logs_read_timestamp(body)



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
    api_response = api_instance.save_logs_read_timestamp(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->save_logs_read_timestamp: %s\n" % e)
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

# **topology_networks**
> PlatformResponseNetworkTopologyObjectArray_ topology_networks(network_id=network_id)



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
    api_response = api_instance.topology_networks(network_id=network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->topology_networks: %s\n" % e)
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

# **update_agent_group**
> InlineResponse204 update_agent_group(body, group_id)



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
    api_response = api_instance.update_agent_group(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->update_agent_group: %s\n" % e)
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

# **update_agent_services_subnets_status**
> update_agent_services_subnets_status(body)



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
    api_instance.update_agent_services_subnets_status(body)
except ApiException as e:
    print("Exception when calling PlatformApi->update_agent_services_subnets_status: %s\n" % e)
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

# **update_api_key**
> InlineResponse204 update_api_key(body, api_key_id)



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
    api_response = api_instance.update_api_key(body, api_key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->update_api_key: %s\n" % e)
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

# **update_connection_services**
> update_connection_services(body)



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
    api_instance.update_connection_services(body)
except ApiException as e:
    print("Exception when calling PlatformApi->update_connection_services: %s\n" % e)
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

