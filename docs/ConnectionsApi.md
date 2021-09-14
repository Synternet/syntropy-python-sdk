# syntropy_sdk.ConnectionsApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_connection_agents_destroy**](ConnectionsApi.md#platform_connection_agents_destroy) | **POST** /api/platform/connections/agents/remove | Delete connections
[**platform_connection_create_mesh**](ConnectionsApi.md#platform_connection_create_mesh) | **POST** /api/platform/connections/mesh | Create connections (mesh)
[**platform_connection_create_p2p**](ConnectionsApi.md#platform_connection_create_p2p) | **POST** /api/platform/connections/point-to-point | Create connections (p2p)
[**platform_connection_groups_destroy**](ConnectionsApi.md#platform_connection_groups_destroy) | **POST** /api/platform/connections/groups/remove | Delete connections (groups)
[**platform_connection_groups_index**](ConnectionsApi.md#platform_connection_groups_index) | **GET** /api/platform/connections/groups | Get connections (groups)
[**platform_connection_groups_sdn_toggle**](ConnectionsApi.md#platform_connection_groups_sdn_toggle) | **PATCH** /api/platform/connections/groups | Toggles SDN for specific connection
[**platform_connection_index**](ConnectionsApi.md#platform_connection_index) | **GET** /api/platform/connections | Get connections
[**v1_platform_create_connections_mesh**](ConnectionsApi.md#v1_platform_create_connections_mesh) | **POST** /api/platform/v1/connections/mesh | Create Connections Mesh
[**v1_platform_create_p2p_connections**](ConnectionsApi.md#v1_platform_create_p2p_connections) | **POST** /api/platform/v1/connections/point-to-point | Create P2P Connections
[**v1_platform_delete_connections_groups**](ConnectionsApi.md#v1_platform_delete_connections_groups) | **POST** /api/platform/v1/connections/groups/delete | Delete Connections
[**v1_platform_get_connections_groups**](ConnectionsApi.md#v1_platform_get_connections_groups) | **POST** /api/platform/v1/connections/groups | Get Connections

# **platform_connection_agents_destroy**
> platform_connection_agents_destroy(body)

Delete connections

Deletes agent connections. Agent itself is not deleted.

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
api_instance = syntropy_sdk.ConnectionsApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.AgentsObject()] # list[AgentsObject] | 

try:
    # Delete connections
    api_instance.platform_connection_agents_destroy(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->platform_connection_agents_destroy: %s\n" % e)
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

# **platform_connection_create_mesh**
> platform_connection_create_mesh(body, paths=paths)

Create connections (mesh)

Create mesh of connections.

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
api_instance = syntropy_sdk.ConnectionsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.ConnectionCreationBodyMesh() # ConnectionCreationBodyMesh | 
paths = ['paths_example'] # list[str] | Comma separated servers ids list for SDN path. (optional)

try:
    # Create connections (mesh)
    api_instance.platform_connection_create_mesh(body, paths=paths)
except ApiException as e:
    print("Exception when calling ConnectionsApi->platform_connection_create_mesh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionCreationBodyMesh**](ConnectionCreationBodyMesh.md)|  | 
 **paths** | [**list[str]**](str.md)| Comma separated servers ids list for SDN path. | [optional] 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_create_p2p**
> platform_connection_create_p2p(body, paths=paths)

Create connections (p2p)

Create connections for agents pairs.

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
api_instance = syntropy_sdk.ConnectionsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.ConnectionCreationBodyP2p() # ConnectionCreationBodyP2p | 
paths = ['paths_example'] # list[str] | Comma separated servers ids list for SDN path. (optional)

try:
    # Create connections (p2p)
    api_instance.platform_connection_create_p2p(body, paths=paths)
except ApiException as e:
    print("Exception when calling ConnectionsApi->platform_connection_create_p2p: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionCreationBodyP2p**](ConnectionCreationBodyP2p.md)|  | 
 **paths** | [**list[str]**](str.md)| Comma separated servers ids list for SDN path. | [optional] 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_groups_destroy**
> platform_connection_groups_destroy(body)

Delete connections (groups)

Deletes `connections` and `connections groups` by groups.

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
api_instance = syntropy_sdk.ConnectionsApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.AgentConnectionGroupIdObject()] # list[AgentConnectionGroupIdObject] | 

try:
    # Delete connections (groups)
    api_instance.platform_connection_groups_destroy(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->platform_connection_groups_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AgentConnectionGroupIdObject]**](AgentConnectionGroupIdObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_groups_index**
> PlatformResponseAgentConnGroupFindAndCountObjectArray_ platform_connection_groups_index(skip=skip, take=take, order=order, filter=filter)

Get connections (groups)

Retrieves connection groups.

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
api_instance = syntropy_sdk.ConnectionsApi(syntropy_sdk.ApiClient(configuration))
skip = syntropy_sdk.SkipNumber() # SkipNumber |  (optional)
take = syntropy_sdk.TakeNumber() # TakeNumber |  (optional)
order = syntropy_sdk.OrderString() # OrderString | agent_connection_group_id | agent_1_name | agent_2_name | agent_connection_group_updated_at: \"ASC\" | \"DESC\" (optional)
filter = syntropy_sdk.WhereString() # WhereString | ids[]: array of connection group ids ids, example: \"1;2;3\", (optional)

try:
    # Get connections (groups)
    api_response = api_instance.platform_connection_groups_index(skip=skip, take=take, order=order, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->platform_connection_groups_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | [**SkipNumber**](.md)|  | [optional] 
 **take** | [**TakeNumber**](.md)|  | [optional] 
 **order** | [**OrderString**](.md)| agent_connection_group_id | agent_1_name | agent_2_name | agent_connection_group_updated_at: \&quot;ASC\&quot; | \&quot;DESC\&quot; | [optional] 
 **filter** | [**WhereString**](.md)| ids[]: array of connection group ids ids, example: \&quot;1;2;3\&quot;, | [optional] 

### Return type

[**PlatformResponseAgentConnGroupFindAndCountObjectArray_**](PlatformResponseAgentConnGroupFindAndCountObjectArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_groups_sdn_toggle**
> platform_connection_groups_sdn_toggle(body)

Toggles SDN for specific connection

Enables or disables SDN for specified connection

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
api_instance = syntropy_sdk.ConnectionsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.ConnGroupSdnToggleObject() # ConnGroupSdnToggleObject | 

try:
    # Toggles SDN for specific connection
    api_instance.platform_connection_groups_sdn_toggle(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->platform_connection_groups_sdn_toggle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnGroupSdnToggleObject**](ConnGroupSdnToggleObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_connection_index**
> PlatformResponseAgentConnectionFindAndCountObjectArray_ platform_connection_index(skip=skip, take=take, order=order, filter=filter, show_sdn_connections=show_sdn_connections, load_relations=load_relations)

Get connections

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
api_instance = syntropy_sdk.ConnectionsApi(syntropy_sdk.ApiClient(configuration))
skip = syntropy_sdk.SkipNumber() # SkipNumber |  (optional)
take = syntropy_sdk.TakeNumber() # TakeNumber |  (optional)
order = syntropy_sdk.OrderString() # OrderString | string: \"ASC\" | \"DESC\" (optional)
filter = syntropy_sdk.WhereString() # WhereString | id|name: string, example: \"1\" or \"name\", connectionId: string, example: \"1\", name: exact agent name, example: \"name1\", agent_ids[]: array of agent ids, example: \"1;2;3\", statuses[]: array of statuses, one of PENDING, WARNING, ERROR, CONNECTED, OFFLINE, example: \"OFFLINE;ERROR;WARNING\", providers[]: array of providers ids, example: \"1;2;3\", agent_connection_updated_at_from: date from which connection was last modified, agent_connection_updated_at_to: date to which connection was last modified (optional)
show_sdn_connections = syntropy_sdk.ShowSdnConnections() # ShowSdnConnections |  (optional)
load_relations = true # bool |  (optional) (default to true)

try:
    # Get connections
    api_response = api_instance.platform_connection_index(skip=skip, take=take, order=order, filter=filter, show_sdn_connections=show_sdn_connections, load_relations=load_relations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->platform_connection_index: %s\n" % e)
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

# **v1_platform_create_connections_mesh**
> v1_platform_create_connections_mesh(body)

Create Connections Mesh

Create connections mesh. Learn more about connections [here (wrong link, need section!)](https://docs.syntropystack.com/docs/what-is-syntropy-agent).

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
api_instance = syntropy_sdk.ConnectionsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.CreateConnectionsMeshRequestV1() # CreateConnectionsMeshRequestV1 | 

try:
    # Create Connections Mesh
    api_instance.v1_platform_create_connections_mesh(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_platform_create_connections_mesh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateConnectionsMeshRequestV1**](CreateConnectionsMeshRequestV1.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_platform_create_p2p_connections**
> v1_platform_create_p2p_connections(body)

Create P2P Connections

Create point to point connections. Learn more about connections [here (wrong link, need section!)](https://docs.syntropystack.com/docs/what-is-syntropy-agent).

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
api_instance = syntropy_sdk.ConnectionsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.CreateP2pConnectionsRequestV1() # CreateP2pConnectionsRequestV1 | 

try:
    # Create P2P Connections
    api_instance.v1_platform_create_p2p_connections(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_platform_create_p2p_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateP2pConnectionsRequestV1**](CreateP2pConnectionsRequestV1.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_platform_delete_connections_groups**
> v1_platform_delete_connections_groups(body)

Delete Connections

Delete connections.

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
api_instance = syntropy_sdk.ConnectionsApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.DeleteConnectionsGroupsRequestV1Inner()] # list[DeleteConnectionsGroupsRequestV1Inner] | 

try:
    # Delete Connections
    api_instance.v1_platform_delete_connections_groups(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_platform_delete_connections_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DeleteConnectionsGroupsRequestV1Inner]**](DeleteConnectionsGroupsRequestV1Inner.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_platform_get_connections_groups**
> PlatformResponseV1GetConnectionsGroupsResponseV1_ v1_platform_get_connections_groups(body)

Get Connections

Return connections. Learn more about connections [here (wrong link, need section!)](https://docs.syntropystack.com/docs/what-is-syntropy-agent).

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
api_instance = syntropy_sdk.ConnectionsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.GetConnectionsGroupsRequestV1() # GetConnectionsGroupsRequestV1 | 

try:
    # Get Connections
    api_response = api_instance.v1_platform_get_connections_groups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_platform_get_connections_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetConnectionsGroupsRequestV1**](GetConnectionsGroupsRequestV1.md)|  | 

### Return type

[**PlatformResponseV1GetConnectionsGroupsResponseV1_**](PlatformResponseV1GetConnectionsGroupsResponseV1_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

