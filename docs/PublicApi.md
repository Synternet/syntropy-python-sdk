# syntropy_sdk.PublicApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_health**](PublicApi.md#public_health) | **GET** /api/public/health | Get health
[**public_info**](PublicApi.md#public_info) | **GET** /api/public/info | Get info

# **public_health**
> public_health()

Get health

Health check used for smoke tests.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.PublicApi()

try:
    # Get health
    api_instance.public_health()
except ApiException as e:
    print("Exception when calling PublicApi->public_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_info**
> PublicAppInfoObject public_info()

Get info

Social providers application ids and versions.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.PublicApi()

try:
    # Get info
    api_response = api_instance.public_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicAppInfoObject**](PublicAppInfoObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

