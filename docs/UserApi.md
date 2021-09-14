# syntropy_sdk.UserApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setting_create**](UserApi.md#setting_create) | **POST** /api/settings | Update user settings
[**setting_index**](UserApi.md#setting_index) | **GET** /api/settings | Get user settings

# **setting_create**
> SettingReadObject setting_create(body)

Update user settings

Update user settings.

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
api_instance = syntropy_sdk.UserApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.SettingWriteObject() # SettingWriteObject | 

try:
    # Update user settings
    api_response = api_instance.setting_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->setting_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingWriteObject**](SettingWriteObject.md)|  | 

### Return type

[**SettingReadObject**](SettingReadObject.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setting_index**
> list[SettingReadObject] setting_index(skip=skip, take=take, order=order, filter=filter)

Get user settings

Get user settings.

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
api_instance = syntropy_sdk.UserApi(syntropy_sdk.ApiClient(configuration))
skip = 1.2 # float |  (optional)
take = 1.2 # float |  (optional)
order = 'order_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)

try:
    # Get user settings
    api_response = api_instance.setting_index(skip=skip, take=take, order=order, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->setting_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**|  | [optional] 
 **take** | **float**|  | [optional] 
 **order** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**list[SettingReadObject]**](SettingReadObject.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

