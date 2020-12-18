# syntropy_sdk.AgentProvidersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AgentProvidersApi.md#create) | **POST** /api/agent-providers | 
[**destroy**](AgentProvidersApi.md#destroy) | **DELETE** /api/agent-providers/{id} | 
[**index**](AgentProvidersApi.md#index) | **GET** /api/agent-providers | 
[**show**](AgentProvidersApi.md#show) | **GET** /api/agent-providers/{id} | 
[**update**](AgentProvidersApi.md#update) | **PATCH** /api/agent-providers/{id} | 

# **create**
> AgentProviderObject create(body)



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
api_instance = syntropy_sdk.AgentProvidersApi(syntropy_sdk.ApiClient(configuration))
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentProvidersApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**AgentProviderObject**](AgentProviderObject.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> destroy(id)



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
api_instance = syntropy_sdk.AgentProvidersApi(syntropy_sdk.ApiClient(configuration))
id = 1.2 # float | 

try:
    api_instance.destroy(id)
except ApiException as e:
    print("Exception when calling AgentProvidersApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index**
> list[AgentProviderObject] index(skip=skip, take=take, order=order, filter=filter)



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
api_instance = syntropy_sdk.AgentProvidersApi(syntropy_sdk.ApiClient(configuration))
skip = 1.2 # float |  (optional)
take = 1.2 # float |  (optional)
order = 'order_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)

try:
    api_response = api_instance.index(skip=skip, take=take, order=order, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentProvidersApi->index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**|  | [optional] 
 **take** | **float**|  | [optional] 
 **order** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**list[AgentProviderObject]**](AgentProviderObject.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> AgentProviderObject show(id)



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
api_instance = syntropy_sdk.AgentProvidersApi(syntropy_sdk.ApiClient(configuration))
id = 1.2 # float | 

try:
    api_response = api_instance.show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentProvidersApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**AgentProviderObject**](AgentProviderObject.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> AgentProviderObject update(body, id)



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
api_instance = syntropy_sdk.AgentProvidersApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.TsoaPartialAgentProviderObject_() # TsoaPartialAgentProviderObject_ | 
id = 1.2 # float | 

try:
    api_response = api_instance.update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentProvidersApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TsoaPartialAgentProviderObject_**](TsoaPartialAgentProviderObject_.md)|  | 
 **id** | **float**|  | 

### Return type

[**AgentProviderObject**](AgentProviderObject.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

