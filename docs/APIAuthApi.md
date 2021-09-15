# syntropy_sdk.APIAuthApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_auth_acess_token_login**](APIAuthApi.md#v1_auth_acess_token_login) | **POST** /api/auth/v1/access-token/login | Access Token Login

# **v1_auth_acess_token_login**
> AuthResponseV1AzureUserTokenDto_ v1_auth_acess_token_login(body)

Access Token Login

Exchange acess token for bearer token.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.APIAuthApi()
body = syntropy_sdk.AccessTokenLoginRequestV1() # AccessTokenLoginRequestV1 | 

try:
    # Access Token Login
    api_response = api_instance.v1_auth_acess_token_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIAuthApi->v1_auth_acess_token_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenLoginRequestV1**](AccessTokenLoginRequestV1.md)|  | 

### Return type

[**AuthResponseV1AzureUserTokenDto_**](AuthResponseV1AzureUserTokenDto_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

