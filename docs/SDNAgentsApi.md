# syntropy_sdk.SDNAgentsApi

All URIs are relative to *https://api.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_network_sdn_agents_get**](SDNAgentsApi.md#v1_network_sdn_agents_get) | **GET** /v1/network/sdn-agents/ips | Get SDN Agent ips

# **v1_network_sdn_agents_get**
> V1NetworkSdnAgentsGetResponse v1_network_sdn_agents_get()

Get SDN Agent ips

Retrieves SDN Agent ips.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.SDNAgentsApi()

try:
    # Get SDN Agent ips
    api_response = api_instance.v1_network_sdn_agents_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SDNAgentsApi->v1_network_sdn_agents_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1NetworkSdnAgentsGetResponse**](V1NetworkSdnAgentsGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

