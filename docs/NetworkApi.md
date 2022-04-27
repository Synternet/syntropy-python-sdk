# syntropy_sdk.NetworkApi

All URIs are relative to *https://api.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_network_get**](NetworkApi.md#v1_network_get) | **GET** /v1/network | Get Network view

# **v1_network_get**
> V1NetworkGetResponse v1_network_get()

Get Network view

Gets current network view.

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
    # Get Network view
    api_response = api_instance.v1_network_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->v1_network_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1NetworkGetResponse**](V1NetworkGetResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

