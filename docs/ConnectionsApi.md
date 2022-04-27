# syntropy_sdk.ConnectionsApi

All URIs are relative to *https://api.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_network_connections_create_mesh**](ConnectionsApi.md#v1_network_connections_create_mesh) | **POST** /v1/network/connections/mesh | Create Connections Mesh
[**v1_network_connections_create_p2_p**](ConnectionsApi.md#v1_network_connections_create_p2_p) | **POST** /v1/network/connections/point-to-point | Create P2P Connections
[**v1_network_connections_delete**](ConnectionsApi.md#v1_network_connections_delete) | **DELETE** /v1/network/connections/{agent_connection_group_id} | Delete Connection
[**v1_network_connections_get**](ConnectionsApi.md#v1_network_connections_get) | **GET** /v1/network/connections | Get Connections
[**v1_network_connections_remove**](ConnectionsApi.md#v1_network_connections_remove) | **POST** /v1/network/connections/remove | Delete Connections
[**v1_network_connections_search**](ConnectionsApi.md#v1_network_connections_search) | **POST** /v1/network/connections/search | Search Connections
[**v1_network_connections_services_delete**](ConnectionsApi.md#v1_network_connections_services_delete) | **DELETE** /v1/network/connections/services/{agent_connection_subnet_id} | Delete Connection service
[**v1_network_connections_services_get**](ConnectionsApi.md#v1_network_connections_services_get) | **GET** /v1/network/connections/services | Get Connection services
[**v1_network_connections_services_remove**](ConnectionsApi.md#v1_network_connections_services_remove) | **POST** /v1/network/connections/services/remove | Delete Connection services
[**v1_network_connections_services_update**](ConnectionsApi.md#v1_network_connections_services_update) | **PATCH** /v1/network/connections/services | Update Connection services
[**v1_network_connections_update**](ConnectionsApi.md#v1_network_connections_update) | **PATCH** /v1/network/connections | Update Connections

# **v1_network_connections_create_mesh**
> v1_network_connections_create_mesh(body)

Create Connections Mesh

Creates Mesh Connections.

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
body = syntropy_sdk.V1NetworkConnectionsCreateMeshRequest() # V1NetworkConnectionsCreateMeshRequest | 

try:
    # Create Connections Mesh
    api_instance.v1_network_connections_create_mesh(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_network_connections_create_mesh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkConnectionsCreateMeshRequest**](V1NetworkConnectionsCreateMeshRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_connections_create_p2_p**
> v1_network_connections_create_p2_p(body)

Create P2P Connections

Creates point to point Connections.

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
body = syntropy_sdk.V1NetworkConnectionsCreateP2PRequest() # V1NetworkConnectionsCreateP2PRequest | 

try:
    # Create P2P Connections
    api_instance.v1_network_connections_create_p2_p(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_network_connections_create_p2_p: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkConnectionsCreateP2PRequest**](V1NetworkConnectionsCreateP2PRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_connections_delete**
> v1_network_connections_delete(agent_connection_group_id)

Delete Connection

Deletes Agent Connection.

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
agent_connection_group_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Delete Connection
    api_instance.v1_network_connections_delete(agent_connection_group_id)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_network_connections_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_connection_group_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_connections_get**
> V1NetworkConnectionsGetResponse v1_network_connections_get(skip=skip, take=take, filter=filter)

Get Connections

Retrieves a list of Agent Connections.

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
filter = syntropy_sdk.WhereString() # WhereString | array of Agent Connection ids (optional)

try:
    # Get Connections
    api_response = api_instance.v1_network_connections_get(skip=skip, take=take, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_network_connections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | [**SkipNumber**](.md)|  | [optional] 
 **take** | [**TakeNumber**](.md)|  | [optional] 
 **filter** | [**WhereString**](.md)| array of Agent Connection ids | [optional] 

### Return type

[**V1NetworkConnectionsGetResponse**](V1NetworkConnectionsGetResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_connections_remove**
> v1_network_connections_remove(body)

Delete Connections

Deletes Agent Connections by `agent_connection_group_id`.

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
body = syntropy_sdk.V1NetworkConnectionsRemoveRequest() # V1NetworkConnectionsRemoveRequest | 

try:
    # Delete Connections
    api_instance.v1_network_connections_remove(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_network_connections_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkConnectionsRemoveRequest**](V1NetworkConnectionsRemoveRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_connections_search**
> V1NetworkConnectionsSearchResponse v1_network_connections_search(body)

Search Connections

Search Agent Connections.

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
body = syntropy_sdk.V1NetworkConnectionsSearchRequest() # V1NetworkConnectionsSearchRequest | 

try:
    # Search Connections
    api_response = api_instance.v1_network_connections_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_network_connections_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkConnectionsSearchRequest**](V1NetworkConnectionsSearchRequest.md)|  | 

### Return type

[**V1NetworkConnectionsSearchResponse**](V1NetworkConnectionsSearchResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_connections_services_delete**
> v1_network_connections_services_delete(agent_connection_subnet_id)

Delete Connection service

Deletes Agent Connection service by `agent_connection_subnet_id`.

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
agent_connection_subnet_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Delete Connection service
    api_instance.v1_network_connections_services_delete(agent_connection_subnet_id)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_network_connections_services_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_connection_subnet_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_connections_services_get**
> V1NetworkConnectionsServicesGetResponse v1_network_connections_services_get(filter=filter)

Get Connection services

Retrieves Agent Connection services.

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
filter = syntropy_sdk.WhereString() # WhereString | array of Agent Connection group ids (optional)

try:
    # Get Connection services
    api_response = api_instance.v1_network_connections_services_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_network_connections_services_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**WhereString**](.md)| array of Agent Connection group ids | [optional] 

### Return type

[**V1NetworkConnectionsServicesGetResponse**](V1NetworkConnectionsServicesGetResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_connections_services_remove**
> v1_network_connections_services_remove(body)

Delete Connection services

Deletes Agent Connection services.

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
body = syntropy_sdk.V1NetworkConnectionsServicesRemoveRequest() # V1NetworkConnectionsServicesRemoveRequest | 

try:
    # Delete Connection services
    api_instance.v1_network_connections_services_remove(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_network_connections_services_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkConnectionsServicesRemoveRequest**](V1NetworkConnectionsServicesRemoveRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_connections_services_update**
> v1_network_connections_services_update(body)

Update Connection services

Updates Agent Connection services.

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
body = syntropy_sdk.V1NetworkConnectionsServicesUpdateRequest() # V1NetworkConnectionsServicesUpdateRequest | 

try:
    # Update Connection services
    api_instance.v1_network_connections_services_update(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_network_connections_services_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkConnectionsServicesUpdateRequest**](V1NetworkConnectionsServicesUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_connections_update**
> v1_network_connections_update(body)

Update Connections

Enables or disables SDN for specified Connections.

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
body = syntropy_sdk.V1NetworkConnectionsUpdateRequest() # V1NetworkConnectionsUpdateRequest | 

try:
    # Update Connections
    api_instance.v1_network_connections_update(body)
except ApiException as e:
    print("Exception when calling ConnectionsApi->v1_network_connections_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkConnectionsUpdateRequest**](V1NetworkConnectionsUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

