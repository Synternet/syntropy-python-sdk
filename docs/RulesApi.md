# syntropy_sdk.RulesApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rules_connection_point_to_tag_create**](RulesApi.md#rules_connection_point_to_tag_create) | **POST** /api/rules/connections/point-to-tag | Create point-to-tag
[**rules_connection_point_to_tag_remove**](RulesApi.md#rules_connection_point_to_tag_remove) | **POST** /api/rules/connections/point-to-tag/remove | Remove point-to-tag
[**rules_connection_point_to_tag_search**](RulesApi.md#rules_connection_point_to_tag_search) | **POST** /api/rules/connections/point-to-tag/search | Search point-to-tag
[**rules_connection_point_to_tag_show_by_id**](RulesApi.md#rules_connection_point_to_tag_show_by_id) | **GET** /api/rules/connections/point-to-tag/{agent_id} | Get point-to-tag
[**rules_connection_point_to_tag_update**](RulesApi.md#rules_connection_point_to_tag_update) | **PATCH** /api/rules/connections/point-to-tag | Patch point-to-tag
[**rules_search**](RulesApi.md#rules_search) | **POST** /api/rules/search | Search rules

# **rules_connection_point_to_tag_create**
> rules_connection_point_to_tag_create(body)

Create point-to-tag

Create rules (rule per tag) for platform agent to connect to all other agents with selected tags.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = syntropy_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.PointtotagPointToTag() # PointtotagPointToTag | Rule per Tag data.

try:
    # Create point-to-tag
    api_instance.rules_connection_point_to_tag_create(body)
except ApiException as e:
    print("Exception when calling RulesApi->rules_connection_point_to_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PointtotagPointToTag**](PointtotagPointToTag.md)| Rule per Tag data. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_connection_point_to_tag_remove**
> rules_connection_point_to_tag_remove(body)

Remove point-to-tag

Remove rules (rule per tag) for platform agent to stop connecting with all other agents with selected tags.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = syntropy_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.PointtotagPointToTag() # PointtotagPointToTag | Rule per Tag data.

try:
    # Remove point-to-tag
    api_instance.rules_connection_point_to_tag_remove(body)
except ApiException as e:
    print("Exception when calling RulesApi->rules_connection_point_to_tag_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PointtotagPointToTag**](PointtotagPointToTag.md)| Rule per Tag data. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_connection_point_to_tag_search**
> PointtotagSearchResponse rules_connection_point_to_tag_search(body)

Search point-to-tag

Search point-to-tag

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = syntropy_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.PointtotagSearchRequest() # PointtotagSearchRequest | Search request

try:
    # Search point-to-tag
    api_response = api_instance.rules_connection_point_to_tag_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->rules_connection_point_to_tag_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PointtotagSearchRequest**](PointtotagSearchRequest.md)| Search request | 

### Return type

[**PointtotagSearchResponse**](PointtotagSearchResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_connection_point_to_tag_show_by_id**
> PointtotagResponse rules_connection_point_to_tag_show_by_id(agent_id)

Get point-to-tag

Retrieve single pointed tag based on given ID

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = syntropy_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
agent_id = 56 # int | AgentID

try:
    # Get point-to-tag
    api_response = api_instance.rules_connection_point_to_tag_show_by_id(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->rules_connection_point_to_tag_show_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| AgentID | 

### Return type

[**PointtotagResponse**](PointtotagResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_connection_point_to_tag_update**
> rules_connection_point_to_tag_update(body)

Patch point-to-tag

Simultaneously adds, removes, replaces point-to-tags rules.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = syntropy_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.ConnectionsPointtotagBody()] # list[ConnectionsPointtotagBody] | Operations list

try:
    # Patch point-to-tag
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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_search**
> RulesResponse rules_search(body=body)

Search rules

Search rules

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = syntropy_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.RulesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.RulesRequest() # RulesRequest | Search request (optional)

try:
    # Search rules
    api_response = api_instance.rules_search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->rules_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RulesRequest**](RulesRequest.md)| Search request | [optional] 

### Return type

[**RulesResponse**](RulesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

