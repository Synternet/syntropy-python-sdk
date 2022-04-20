# syntropy_sdk.AnalyticsApi

All URIs are relative to *https://api.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_network_a_bandwidth_get**](AnalyticsApi.md#v1_network_a_bandwidth_get) | **GET** /v1/network/a/bandwidth | Get bandwidth
[**v1_network_a_iface_active_change_get**](AnalyticsApi.md#v1_network_a_iface_active_change_get) | **GET** /v1/network/a/iface-active-change | Get active iface changes
[**v1_network_a_latency_get**](AnalyticsApi.md#v1_network_a_latency_get) | **GET** /v1/network/a/latency | Get latency
[**v1_network_a_packet_loss_get**](AnalyticsApi.md#v1_network_a_packet_loss_get) | **GET** /v1/network/a/packet-loss | Get packet loss
[**v1_network_a_statuses_search**](AnalyticsApi.md#v1_network_a_statuses_search) | **POST** /v1/network/a/statuses/search | Search statuses
[**v1_network_a_statuses_warnings_search**](AnalyticsApi.md#v1_network_a_statuses_warnings_search) | **POST** /v1/network/a/statuses/warnings/search | Search status warnings

# **v1_network_a_bandwidth_get**
> ADataResponse v1_network_a_bandwidth_get(agent_src_id, agent_dst_id, _from, to)

Get bandwidth

Retrieves Connections bandwidth information.

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
api_instance = syntropy_sdk.AnalyticsApi(syntropy_sdk.ApiClient(configuration))
agent_src_id = syntropy_sdk.IdNumber() # IdNumber | Source Agent Id
agent_dst_id = syntropy_sdk.IdNumber() # IdNumber | Destination Agent Id
_from = '2013-10-20T19:20:30+01:00' # datetime | 
to = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    # Get bandwidth
    api_response = api_instance.v1_network_a_bandwidth_get(agent_src_id, agent_dst_id, _from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->v1_network_a_bandwidth_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_src_id** | [**IdNumber**](.md)| Source Agent Id | 
 **agent_dst_id** | [**IdNumber**](.md)| Destination Agent Id | 
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 

### Return type

[**ADataResponse**](ADataResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_a_iface_active_change_get**
> ADataResponse v1_network_a_iface_active_change_get(agent_src_id, agent_dst_id, _from, to)

Get active iface changes

Retrieves active iface changes data.

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
api_instance = syntropy_sdk.AnalyticsApi(syntropy_sdk.ApiClient(configuration))
agent_src_id = 56 # int | Source Agent Id
agent_dst_id = 56 # int | Destination Agent Id
_from = '2013-10-20T19:20:30+01:00' # datetime | 
to = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    # Get active iface changes
    api_response = api_instance.v1_network_a_iface_active_change_get(agent_src_id, agent_dst_id, _from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->v1_network_a_iface_active_change_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_src_id** | **int**| Source Agent Id | 
 **agent_dst_id** | **int**| Destination Agent Id | 
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 

### Return type

[**ADataResponse**](ADataResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_a_latency_get**
> ADataResponse v1_network_a_latency_get(agent_src_id, agent_dst_id, _from, to)

Get latency

Retrieves Connections latency.

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
api_instance = syntropy_sdk.AnalyticsApi(syntropy_sdk.ApiClient(configuration))
agent_src_id = 56 # int | Source Agent Id
agent_dst_id = 56 # int | Destination Agent Id
_from = '2013-10-20T19:20:30+01:00' # datetime | 
to = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    # Get latency
    api_response = api_instance.v1_network_a_latency_get(agent_src_id, agent_dst_id, _from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->v1_network_a_latency_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_src_id** | **int**| Source Agent Id | 
 **agent_dst_id** | **int**| Destination Agent Id | 
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 

### Return type

[**ADataResponse**](ADataResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_a_packet_loss_get**
> ADataResponse v1_network_a_packet_loss_get(agent_src_id, agent_dst_id, _from, to)

Get packet loss

Retrieves Connections packet loss.

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
api_instance = syntropy_sdk.AnalyticsApi(syntropy_sdk.ApiClient(configuration))
agent_src_id = 56 # int | Source Agent Id
agent_dst_id = 56 # int | Destination Agent Id
_from = '2013-10-20T19:20:30+01:00' # datetime | 
to = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    # Get packet loss
    api_response = api_instance.v1_network_a_packet_loss_get(agent_src_id, agent_dst_id, _from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->v1_network_a_packet_loss_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_src_id** | **int**| Source Agent Id | 
 **agent_dst_id** | **int**| Destination Agent Id | 
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 

### Return type

[**ADataResponse**](ADataResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_a_statuses_search**
> V1NetworkAStatusesSearchResponse v1_network_a_statuses_search(body)

Search statuses

Retrieve Connection statuses by given criteria.

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
api_instance = syntropy_sdk.AnalyticsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAStatusesSearchRequest() # V1NetworkAStatusesSearchRequest | 

try:
    # Search statuses
    api_response = api_instance.v1_network_a_statuses_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->v1_network_a_statuses_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAStatusesSearchRequest**](V1NetworkAStatusesSearchRequest.md)|  | 

### Return type

[**V1NetworkAStatusesSearchResponse**](V1NetworkAStatusesSearchResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_a_statuses_warnings_search**
> V1NetworkAStatusesWarningsSearchResponse v1_network_a_statuses_warnings_search(body)

Search status warnings

Retrieves status warnings by given criteria.

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
api_instance = syntropy_sdk.AnalyticsApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAStatusesWarningsSearchRequest() # V1NetworkAStatusesWarningsSearchRequest | 

try:
    # Search status warnings
    api_response = api_instance.v1_network_a_statuses_warnings_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->v1_network_a_statuses_warnings_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAStatusesWarningsSearchRequest**](V1NetworkAStatusesWarningsSearchRequest.md)|  | 

### Return type

[**V1NetworkAStatusesWarningsSearchResponse**](V1NetworkAStatusesWarningsSearchResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

