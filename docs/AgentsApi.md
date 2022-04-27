# syntropy_sdk.AgentsApi

All URIs are relative to *https://api.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_network_agents_coordinates_search**](AgentsApi.md#v1_network_agents_coordinates_search) | **POST** /v1/network/agents/coordinates/search | Search Agent location coordinates
[**v1_network_agents_create**](AgentsApi.md#v1_network_agents_create) | **POST** /v1/network/agents | Create Agent
[**v1_network_agents_delete**](AgentsApi.md#v1_network_agents_delete) | **DELETE** /v1/network/agents/{agent_id} | Delete Agent
[**v1_network_agents_filters_search**](AgentsApi.md#v1_network_agents_filters_search) | **POST** /v1/network/agents/filters/search | Search Agent filters
[**v1_network_agents_get**](AgentsApi.md#v1_network_agents_get) | **GET** /v1/network/agents | Get Agents
[**v1_network_agents_logs_errors_search**](AgentsApi.md#v1_network_agents_logs_errors_search) | **POST** /v1/network/agents/logs/errors/search | Search Agent error logs
[**v1_network_agents_logs_reads_timestamp_search**](AgentsApi.md#v1_network_agents_logs_reads_timestamp_search) | **POST** /v1/network/agents/logs-reads-timestamp | Save log read timestamp
[**v1_network_agents_logs_search**](AgentsApi.md#v1_network_agents_logs_search) | **POST** /v1/network/agents/logs/search | Search Agent logs
[**v1_network_agents_providers_get**](AgentsApi.md#v1_network_agents_providers_get) | **GET** /v1/network/agents/providers | Get Agent providers
[**v1_network_agents_remove**](AgentsApi.md#v1_network_agents_remove) | **POST** /v1/network/agents/remove | Delete Agents
[**v1_network_agents_search**](AgentsApi.md#v1_network_agents_search) | **POST** /v1/network/agents/search | Search Agents
[**v1_network_agents_services_delete**](AgentsApi.md#v1_network_agents_services_delete) | **DELETE** /v1/network/agents/services/{agent_service_subnet_id} | Delete Agent service
[**v1_network_agents_services_get**](AgentsApi.md#v1_network_agents_services_get) | **GET** /v1/network/agents/services | Get Agent services.
[**v1_network_agents_services_remove**](AgentsApi.md#v1_network_agents_services_remove) | **POST** /v1/network/agents/services/remove | Delete Agent services
[**v1_network_agents_services_update**](AgentsApi.md#v1_network_agents_services_update) | **PATCH** /v1/network/agents/services/bulk | Update Agent services
[**v1_network_agents_settings_get**](AgentsApi.md#v1_network_agents_settings_get) | **GET** /v1/network/agents/settings | Get Agent settings
[**v1_network_agents_settings_update**](AgentsApi.md#v1_network_agents_settings_update) | **PATCH** /v1/network/agents/settings | Update Agent settings
[**v1_network_agents_tags_get**](AgentsApi.md#v1_network_agents_tags_get) | **GET** /v1/network/agents/tags | Get Agent tags
[**v1_network_agents_update**](AgentsApi.md#v1_network_agents_update) | **PATCH** /v1/network/agents/{agent_id} | Updates Agent
[**v1_network_agents_wg_config_get_one**](AgentsApi.md#v1_network_agents_wg_config_get_one) | **GET** /v1/network/agents/wg-config/{agent_id} | Get Agent Wg config

# **v1_network_agents_coordinates_search**
> V1NetworkAgentsCoordinatesSearchResponse v1_network_agents_coordinates_search(body)

Search Agent location coordinates

Retrieves Agents location coordinates.

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
body = syntropy_sdk.CoordinatesSearchBody() # CoordinatesSearchBody | 

try:
    # Search Agent location coordinates
    api_response = api_instance.v1_network_agents_coordinates_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_coordinates_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoordinatesSearchBody**](CoordinatesSearchBody.md)|  | 

### Return type

[**V1NetworkAgentsCoordinatesSearchResponse**](V1NetworkAgentsCoordinatesSearchResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_create**
> V1NetworkAgentsCreateResponse v1_network_agents_create(body)

Create Agent

Creates new agent. Only `VIRTUAL` agents creation is supported. Not `VIRTUAL` agents are automatically created when first WebSocket connection is established.

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
body = syntropy_sdk.V1NetworkAgentsCreateRequest() # V1NetworkAgentsCreateRequest | 

try:
    # Create Agent
    api_response = api_instance.v1_network_agents_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAgentsCreateRequest**](V1NetworkAgentsCreateRequest.md)|  | 

### Return type

[**V1NetworkAgentsCreateResponse**](V1NetworkAgentsCreateResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_delete**
> v1_network_agents_delete(agent_id)

Delete Agent

Deletes Agent with existing connections. Learn more about platform agents [here](https://docs.syntropystack.com/docs/what-is-syntropy-agent).

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
    # Delete Agent
    api_instance.v1_network_agents_delete(agent_id)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_delete: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_filters_search**
> V1NetworkAgentsFiltersSearchResponse v1_network_agents_filters_search(body)

Search Agent filters

Gets all unique Agents names and ids for filters.

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
body = syntropy_sdk.V1NetworkAgentsSearchRequest() # V1NetworkAgentsSearchRequest | 

try:
    # Search Agent filters
    api_response = api_instance.v1_network_agents_filters_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_filters_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAgentsSearchRequest**](V1NetworkAgentsSearchRequest.md)|  | 

### Return type

[**V1NetworkAgentsFiltersSearchResponse**](V1NetworkAgentsFiltersSearchResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_get**
> V1NetworkAgentsGetResponse v1_network_agents_get(skip=skip, take=take, filter=filter)

Get Agents

Returns list of Agents.

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
filter = syntropy_sdk.WhereString() # WhereString | array of agent ids (optional)

try:
    # Get Agents
    api_response = api_instance.v1_network_agents_get(skip=skip, take=take, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | [**SkipNumber**](.md)|  | [optional] 
 **take** | [**TakeNumber**](.md)|  | [optional] 
 **filter** | [**WhereString**](.md)| array of agent ids | [optional] 

### Return type

[**V1NetworkAgentsGetResponse**](V1NetworkAgentsGetResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_logs_errors_search**
> V1NetworkAgentsLogsErrorsSearchResponse v1_network_agents_logs_errors_search(body)

Search Agent error logs

Returns a list of Agent error logs.

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
body = syntropy_sdk.V1NetworkAgentsLogsErrorsSearchRequest() # V1NetworkAgentsLogsErrorsSearchRequest | 

try:
    # Search Agent error logs
    api_response = api_instance.v1_network_agents_logs_errors_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_logs_errors_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAgentsLogsErrorsSearchRequest**](V1NetworkAgentsLogsErrorsSearchRequest.md)|  | 

### Return type

[**V1NetworkAgentsLogsErrorsSearchResponse**](V1NetworkAgentsLogsErrorsSearchResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_logs_reads_timestamp_search**
> v1_network_agents_logs_reads_timestamp_search(body)

Save log read timestamp

Saves last logs read timestamp.

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
body = [syntropy_sdk.V1NetworkAgentsLogsReadsTimestampSearchRequest()] # list[V1NetworkAgentsLogsReadsTimestampSearchRequest] | 

try:
    # Save log read timestamp
    api_instance.v1_network_agents_logs_reads_timestamp_search(body)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_logs_reads_timestamp_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[V1NetworkAgentsLogsReadsTimestampSearchRequest]**](V1NetworkAgentsLogsReadsTimestampSearchRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_logs_search**
> V1NetworkAgentsLogsSearchResponse v1_network_agents_logs_search(body)

Search Agent logs

Search Agent logs.

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
body = syntropy_sdk.V1NetworkAgentsLogsSearchRequest() # V1NetworkAgentsLogsSearchRequest | 

try:
    # Search Agent logs
    api_response = api_instance.v1_network_agents_logs_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_logs_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAgentsLogsSearchRequest**](V1NetworkAgentsLogsSearchRequest.md)|  | 

### Return type

[**V1NetworkAgentsLogsSearchResponse**](V1NetworkAgentsLogsSearchResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_providers_get**
> V1NetworkAgentsProvidersGetResponse v1_network_agents_providers_get(skip=skip, take=take, order=order, filter=filter)

Get Agent providers

Returns list of Agent providers.

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
filter = syntropy_sdk.WhereString() # WhereString | array of agent provider ids (optional)

try:
    # Get Agent providers
    api_response = api_instance.v1_network_agents_providers_get(skip=skip, take=take, order=order, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | [**SkipNumber**](.md)|  | [optional] 
 **take** | [**TakeNumber**](.md)|  | [optional] 
 **order** | [**AgentProviderOrderString**](.md)|  | [optional] 
 **filter** | [**WhereString**](.md)| array of agent provider ids | [optional] 

### Return type

[**V1NetworkAgentsProvidersGetResponse**](V1NetworkAgentsProvidersGetResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_remove**
> v1_network_agents_remove(body)

Delete Agents

Deletes Agents with existing connections. Learn more about platform agents [here](https://docs.syntropystack.com/docs/what-is-syntropy-agent).

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
body = syntropy_sdk.V1NetworkAgentsRemoveRequest() # V1NetworkAgentsRemoveRequest | 

try:
    # Delete Agents
    api_instance.v1_network_agents_remove(body)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAgentsRemoveRequest**](V1NetworkAgentsRemoveRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_search**
> V1NetworkAgentsSearchResponse v1_network_agents_search(body)

Search Agents

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
body = syntropy_sdk.V1NetworkAgentsSearchRequest() # V1NetworkAgentsSearchRequest | 

try:
    # Search Agents
    api_response = api_instance.v1_network_agents_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAgentsSearchRequest**](V1NetworkAgentsSearchRequest.md)|  | 

### Return type

[**V1NetworkAgentsSearchResponse**](V1NetworkAgentsSearchResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_services_delete**
> v1_network_agents_services_delete(agent_service_subnet_id)

Delete Agent service

Deletes Agent service.

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
agent_service_subnet_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Delete Agent service
    api_instance.v1_network_agents_services_delete(agent_service_subnet_id)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_services_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_service_subnet_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_services_get**
> V1NetworkAgentsServicesGetResponse v1_network_agents_services_get(filter=filter)

Get Agent services.

Returns list of Agent services

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
filter = syntropy_sdk.WhereString() # WhereString | array of agent ids (optional)

try:
    # Get Agent services.
    api_response = api_instance.v1_network_agents_services_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_services_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**WhereString**](.md)| array of agent ids | [optional] 

### Return type

[**V1NetworkAgentsServicesGetResponse**](V1NetworkAgentsServicesGetResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_services_remove**
> v1_network_agents_services_remove(body)

Delete Agent services

Deletes Agent services.

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
body = syntropy_sdk.V1NetworkAgentsServicesRemoveRequest() # V1NetworkAgentsServicesRemoveRequest | 

try:
    # Delete Agent services
    api_instance.v1_network_agents_services_remove(body)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_services_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAgentsServicesRemoveRequest**](V1NetworkAgentsServicesRemoveRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_services_update**
> v1_network_agents_services_update(body)

Update Agent services

Updates Agent services.

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
body = syntropy_sdk.V1NetworkAgentsServicesUpdateRequest() # V1NetworkAgentsServicesUpdateRequest | 

try:
    # Update Agent services
    api_instance.v1_network_agents_services_update(body)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_services_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAgentsServicesUpdateRequest**](V1NetworkAgentsServicesUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_settings_get**
> V1NetworkAgentsSettingsGetResponse v1_network_agents_settings_get()

Get Agent settings

Gets Agents settings.

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
    # Get Agent settings
    api_response = api_instance.v1_network_agents_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1NetworkAgentsSettingsGetResponse**](V1NetworkAgentsSettingsGetResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_settings_update**
> v1_network_agents_settings_update(body)

Update Agent settings

Updates Agents settings.

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
body = syntropy_sdk.V1NetworkAgentsSettingsUpdateRequest() # V1NetworkAgentsSettingsUpdateRequest | 

try:
    # Update Agent settings
    api_instance.v1_network_agents_settings_update(body)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAgentsSettingsUpdateRequest**](V1NetworkAgentsSettingsUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_tags_get**
> V1NetworkAgentsTagsGetResponse v1_network_agents_tags_get()

Get Agent tags

Returns a list of user Agent tags.

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
    # Get Agent tags
    api_response = api_instance.v1_network_agents_tags_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_tags_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1NetworkAgentsTagsGetResponse**](V1NetworkAgentsTagsGetResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_update**
> v1_network_agents_update(body, agent_id)

Updates Agent

Update Agent.

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
body = syntropy_sdk.V1NetworkAgentsUpdateRequest() # V1NetworkAgentsUpdateRequest | 
agent_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Updates Agent
    api_instance.v1_network_agents_update(body, agent_id)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAgentsUpdateRequest**](V1NetworkAgentsUpdateRequest.md)|  | 
 **agent_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_agents_wg_config_get_one**
> V1NetworkAgentsWgConfigGetOneResponse v1_network_agents_wg_config_get_one(agent_id)

Get Agent Wg config

Returns Agents WireGuard configuration.

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
    # Get Agent Wg config
    api_response = api_instance.v1_network_agents_wg_config_get_one(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->v1_network_agents_wg_config_get_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**IdNumber**](.md)|  | 

### Return type

[**V1NetworkAgentsWgConfigGetOneResponse**](V1NetworkAgentsWgConfigGetOneResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

