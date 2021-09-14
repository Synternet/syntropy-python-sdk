# syntropy_sdk.NetworkApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_network_info**](NetworkApi.md#platform_network_info) | **GET** /api/platform/network/info | Get network

# **platform_network_info**
> PlatformResponseNetworkInfoObject_ platform_network_info()

Get network

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
api_instance = syntropy_sdk.NetworkApi(syntropy_sdk.ApiClient(configuration))

try:
    # Get network
    api_response = api_instance.platform_network_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->platform_network_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PlatformResponseNetworkInfoObject_**](PlatformResponseNetworkInfoObject_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

