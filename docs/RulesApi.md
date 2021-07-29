# syntropy_sdk. RulesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connection_point_to_tag_create**]( RulesApi.md#connection_point_to_tag_create) | **POST** /rules/connections/point-to-tag | Create rules
[**connection_point_to_tag_remove**]( RulesApi.md#connection_point_to_tag_remove) | **POST** /rules/connections/point-to-tag/remove | Remove rules
[**connection_point_to_tag_search**]( RulesApi.md#connection_point_to_tag_search) | **POST** /rules/connections/point-to-tag/search | Search rules
[**connection_point_to_tag_show_by_id**]( RulesApi.md#connection_point_to_tag_show_by_id) | **GET** /rules/connections/point-to-tag/{agent_id} | Retrieve single pointed tag based on given ID
[**connection_point_to_tag_update**]( RulesApi.md#connection_point_to_tag_update) | **PATCH** /rules/connections/point-to-tag | Patch rules

# **connection_point_to_tag_create**
> connection_point_to_tag_create(body)

Create rules

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
api_instance = syntropy_sdk. RulesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.PointToTagPointToTag() # PointToTagPointToTag | Rule per Tag data.

try:
    # Create rules
    api_instance.rules_connection_point_to_tag_create(body)
except ApiException as e:
    print("Exception when calling  RulesApi->rules_connection_point_to_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PointToTagPointToTag**](PointToTagPointToTag.md)| Rule per Tag data. | 

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

Remove rules

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
api_instance = syntropy_sdk. RulesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.PointToTagPointToTag() # PointToTagPointToTag | Rule per Tag data.

try:
    # Remove rules
    api_instance.rules_connection_point_to_tag_remove(body)
except ApiException as e:
    print("Exception when calling  RulesApi->rules_connection_point_to_tag_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PointToTagPointToTag**](PointToTagPointToTag.md)| Rule per Tag data. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_connection_point_to_tag_search**
> PointToTagSearchResponse rules_connection_point_to_tag_search(body)

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
api_instance = syntropy_sdk. RulesApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.PointToTagSearchRequest() # PointToTagSearchRequest | Search request

try:
    # Search rules
    api_response = api_instance.rules_connection_point_to_tag_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling  RulesApi->rules_connection_point_to_tag_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PointToTagSearchRequest**](PointToTagSearchRequest.md)| Search request | 

### Return type

[**PointToTagSearchResponse**](PointToTagSearchResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_connection_point_to_tag_show_by_id**
> PointToTagResponse rules_connection_point_to_tag_show_by_id(agent_id)

Retrieve single pointed tag based on given ID

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
api_instance = syntropy_sdk. RulesApi(syntropy_sdk.ApiClient(configuration))
agent_id = 56 # int | AgentID

try:
    # Retrieve single pointed tag based on given ID
    api_response = api_instance.rules_connection_point_to_tag_show_by_id(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling  RulesApi->rules_connection_point_to_tag_show_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| AgentID | 

### Return type

[**PointToTagResponse**](PointToTagResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_connection_point_to_tag_update**
> rules_connection_point_to_tag_update(body)

Patch rules

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
api_instance = syntropy_sdk. RulesApi(syntropy_sdk.ApiClient(configuration))
body = [syntropy_sdk.Body()] # list[Body] | Operations list

try:
    # Patch rules
    api_instance.rules_connection_point_to_tag_update(body)
except ApiException as e:
    print("Exception when calling  RulesApi->rules_connection_point_to_tag_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Body]**](Body.md)| Operations list | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

