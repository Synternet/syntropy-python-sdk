# syntropy_sdk.APIKeysApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](APIKeysApi.md#create_api_key) | **POST** /auth/api-key | Create API key
[**delete_api_key**](APIKeysApi.md#delete_api_key) | **DELETE** /auth/api-key/{api_key_id} | Delete API keys
[**get_api_key**](APIKeysApi.md#get_api_key) | **GET** /auth/api-key | Get API keys

# **create_api_key**
> ApiResponseApiKeyObject_ create_api_key(body)

Create API key

Create API key.

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
api_instance = syntropy_sdk.APIKeysApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.ApiKeyCreateRequest() # ApiKeyCreateRequest | 

try:
    # Create API key
    api_response = api_instance.create_api_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->create_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiKeyCreateRequest**](ApiKeyCreateRequest.md)|  | 

### Return type

[**ApiResponseApiKeyObject_**](ApiResponseApiKeyObject_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> delete_api_key(api_key_id)

Delete API keys

Delete API key.

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
api_instance = syntropy_sdk.APIKeysApi(syntropy_sdk.ApiClient(configuration))
api_key_id = syntropy_sdk.ApiKeyId() # ApiKeyId | 

try:
    # Delete API keys
    api_instance.delete_api_key(api_key_id)
except ApiException as e:
    print("Exception when calling APIKeysApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | [**ApiKeyId**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> ApiResponseApiKeyDtoArray_ get_api_key(skip=skip, take=take, order=order, filter=filter)

Get API keys

Get API keys.

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
api_instance = syntropy_sdk.APIKeysApi(syntropy_sdk.ApiClient(configuration))
skip = 1.2 # float |  (optional)
take = 1.2 # float |  (optional)
order = 'order_example' # str | string: \"ASC\" | \"DESC\" (optional)
filter = 'filter_example' # str | api_key_id: string, api_key_name: string (optional)

try:
    # Get API keys
    api_response = api_instance.get_api_key(skip=skip, take=take, order=order, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->get_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**|  | [optional] 
 **take** | **float**|  | [optional] 
 **order** | **str**| string: \&quot;ASC\&quot; | \&quot;DESC\&quot; | [optional] 
 **filter** | **str**| api_key_id: string, api_key_name: string | [optional] 

### Return type

[**ApiResponseApiKeyDtoArray_**](ApiResponseApiKeyDtoArray_.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

