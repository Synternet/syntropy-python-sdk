# syntropy_sdk.RulesApi

All URIs are relative to *https://api.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rules_connection_point_to_tag_update**](RulesApi.md#rules_connection_point_to_tag_update) | **PATCH** /v1/network/rules/connections/point-to-tag | Upsert point-to-tag
[**v1_network_rules_connections_point_to_tag_create**](RulesApi.md#v1_network_rules_connections_point_to_tag_create) | **POST** /v1/network/rules/connections/point-to-tag | Create point-to-tag
[**v1_network_rules_connections_point_to_tag_get_one**](RulesApi.md#v1_network_rules_connections_point_to_tag_get_one) | **GET** /v1/network/rules/connections/point-to-tag/{agent_id} | Get point-to-tag
[**v1_network_rules_connections_point_to_tag_search**](RulesApi.md#v1_network_rules_connections_point_to_tag_search) | **POST** /v1/network/rules/connections/point-to-tag/search | Search point-to-tag Rules
[**v1_network_rules_search**](RulesApi.md#v1_network_rules_search) | **POST** /v1/network/rules/search | Search Rules
[**v1_rules_connection_point_to_tag_remove**](RulesApi.md#v1_rules_connection_point_to_tag_remove) | **POST** /v1/network/rules/connections/point-to-tag/remove | Remove point-to-tag

# **rules_connection_point_to_tag_update**
> rules_connection_point_to_tag_update(body)

Upsert point-to-tag

Simultaneously adds, removes, replaces point-to-tags Rules.

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
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.ConnectionsPointtotagBody()] # list[ConnectionsPointtotagBody] | Operations list

try:
    # Upsert point-to-tag
    api_instance.rules_connection_point_to_tag_update(body)
except ApiException as e:
    print("Exception when calling RulesApi->rules_connection_point_to_tag_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ConnectionsPointtotagBody]**](ConnectionsPointtotagBody.md)| Operations list | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_rules_connections_point_to_tag_create**
> V1NetworkRulesConnectionsPointToTagCreateResponse v1_network_rules_connections_point_to_tag_create(body)

Create point-to-tag

Creates point to tag Rule.

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
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1RulesPointToTag() # V1RulesPointToTag | 

try:
    # Create point-to-tag
    api_response = api_instance.v1_network_rules_connections_point_to_tag_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->v1_network_rules_connections_point_to_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1RulesPointToTag**](V1RulesPointToTag.md)|  | 

### Return type

[**V1NetworkRulesConnectionsPointToTagCreateResponse**](V1NetworkRulesConnectionsPointToTagCreateResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_rules_connections_point_to_tag_get_one**
> V1NetworkRulesConnectionsPointToTagGetOneResponse v1_network_rules_connections_point_to_tag_get_one(agent_id)

Get point-to-tag

Retrieve point-to-tag Rules by `agent_id`.

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
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
agent_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Get point-to-tag
    api_response = api_instance.v1_network_rules_connections_point_to_tag_get_one(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->v1_network_rules_connections_point_to_tag_get_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**IdNumber**](.md)|  | 

### Return type

[**V1NetworkRulesConnectionsPointToTagGetOneResponse**](V1NetworkRulesConnectionsPointToTagGetOneResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_rules_connections_point_to_tag_search**
> V1NetworkRulesConnectionsPointToTagSearchResponse v1_network_rules_connections_point_to_tag_search(body)

Search point-to-tag Rules

Gets list of point-to-tag Rules by given criteria.

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
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkRulesConnectionsPointToTagSearchRequest() # V1NetworkRulesConnectionsPointToTagSearchRequest | Search request

try:
    # Search point-to-tag Rules
    api_response = api_instance.v1_network_rules_connections_point_to_tag_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->v1_network_rules_connections_point_to_tag_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkRulesConnectionsPointToTagSearchRequest**](V1NetworkRulesConnectionsPointToTagSearchRequest.md)| Search request | 

### Return type

[**V1NetworkRulesConnectionsPointToTagSearchResponse**](V1NetworkRulesConnectionsPointToTagSearchResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_rules_search**
> V1NetworkRulesSearchResponse v1_network_rules_search(body=body)

Search Rules

Gets list of Rules by given criteria.

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
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkRulesSearchRequest() # V1NetworkRulesSearchRequest |  (optional)

try:
    # Search Rules
    api_response = api_instance.v1_network_rules_search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->v1_network_rules_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkRulesSearchRequest**](V1NetworkRulesSearchRequest.md)|  | [optional] 

### Return type

[**V1NetworkRulesSearchResponse**](V1NetworkRulesSearchResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_rules_connection_point_to_tag_remove**
> v1_rules_connection_point_to_tag_remove(body)

Remove point-to-tag

Removes point-to-tag Rules by given criteria.

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
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1RulesPointToTag() # V1RulesPointToTag | 

try:
    # Remove point-to-tag
    api_instance.v1_rules_connection_point_to_tag_remove(body)
except ApiException as e:
    print("Exception when calling RulesApi->v1_rules_connection_point_to_tag_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1RulesPointToTag**](V1RulesPointToTag.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

