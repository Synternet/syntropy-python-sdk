# syntropy_sdk.AuthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contact**](AuthApi.md#add_contact) | **POST** /auth/authorization/contact | 
[**auth**](AuthApi.md#auth) | **GET** /auth/authorization | 
[**auth_access_token_list**](AuthApi.md#auth_access_token_list) | **GET** /auth/authorization/access-token | 
[**auth_access_token_login**](AuthApi.md#auth_access_token_login) | **POST** /auth/authorization/access-token/login | 
[**auth_access_token_permissions_list**](AuthApi.md#auth_access_token_permissions_list) | **GET** /auth/authorization/permissions/access-token | 
[**auth_access_token_user_create**](AuthApi.md#auth_access_token_user_create) | **POST** /auth/authorization/access-token | 
[**auth_access_token_user_delete**](AuthApi.md#auth_access_token_user_delete) | **DELETE** /auth/authorization/access-token/{id} | 
[**auth_create_user**](AuthApi.md#auth_create_user) | **POST** /auth/authorization/create-user | 
[**auth_external_login**](AuthApi.md#auth_external_login) | **POST** /auth/authorization/external/login | 
[**auth_logout**](AuthApi.md#auth_logout) | **POST** /auth/authorization/logout | 
[**auth_show_user**](AuthApi.md#auth_show_user) | **GET** /auth/authorization/user | 
[**auth_verify_email**](AuthApi.md#auth_verify_email) | **GET** /auth/authorization/verify-email/{code} | 
[**update_settings**](AuthApi.md#update_settings) | **PUT** /auth/authorization/settings | 
[**validate_captcha**](AuthApi.md#validate_captcha) | **POST** /auth/authorization/validate-captcha | 
[**validate_captcha_0**](AuthApi.md#validate_captcha_0) | **POST** /auth/authorization/validate-limit | 
[**validate_user_credentials**](AuthApi.md#validate_user_credentials) | **POST** /auth/authorization/validate-user | 

# **add_contact**
> Object add_contact(body)



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
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.ContactRequest() # ContactRequest | 

try:
    api_response = api_instance.add_contact(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->add_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContactRequest**](ContactRequest.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth**
> str auth()



Verifies jwt token and returns entity data.

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
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    api_response = api_instance.auth()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_access_token_list**
> list[AccessTokenReadData] auth_access_token_list(skip=skip, take=take, order=order)



List access tokens.

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
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
skip = 0 # float |  (optional) (default to 0)
take = 10 # float |  (optional) (default to 10)
order = syntropy_sdk.AccessTokenOrder() # AccessTokenOrder |  (optional)

try:
    api_response = api_instance.auth_access_token_list(skip=skip, take=take, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_access_token_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**|  | [optional] [default to 0]
 **take** | **float**|  | [optional] [default to 10]
 **order** | [**AccessTokenOrder**](.md)|  | [optional] 

### Return type

[**list[AccessTokenReadData]**](AccessTokenReadData.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_access_token_login**
> AzureUserTokenDto auth_access_token_login(body)



Retrieve JWT from access token.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
body = syntropy_sdk.AccessTokenData() # AccessTokenData | 

try:
    api_response = api_instance.auth_access_token_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_access_token_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenData**](AccessTokenData.md)|  | 

### Return type

[**AzureUserTokenDto**](AzureUserTokenDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_access_token_permissions_list**
> list[PermissionObject] auth_access_token_permissions_list()



Entire list of available permissions access tokens can have.

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
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    api_response = api_instance.auth_access_token_permissions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_access_token_permissions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PermissionObject]**](PermissionObject.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_access_token_user_create**
> AccessTokenData auth_access_token_user_create(body)



Create scopes access token.

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
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.AccessTokenWriteData() # AccessTokenWriteData | 

try:
    api_response = api_instance.auth_access_token_user_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_access_token_user_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenWriteData**](AccessTokenWriteData.md)|  | 

### Return type

[**AccessTokenData**](AccessTokenData.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_access_token_user_delete**
> Object auth_access_token_user_delete(id)



Delete scopes access token.

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
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.auth_access_token_user_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_access_token_user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_create_user**
> auth_create_user(body)



Used by Azure as web hook after new user is registered.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
body = syntropy_sdk.Object() # Object | 

try:
    api_instance.auth_create_user(body)
except ApiException as e:
    print("Exception when calling AuthApi->auth_create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_external_login**
> AzureUserTokenDto auth_external_login(body)



Logs in user using resource owner password credentials flow.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
body = syntropy_sdk.LoginRequest() # LoginRequest | 

try:
    api_response = api_instance.auth_external_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_external_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**AzureUserTokenDto**](AzureUserTokenDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_logout**
> auth_logout()



Deletes session cookies.

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
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    api_instance.auth_logout()
except ApiException as e:
    print("Exception when calling AuthApi->auth_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_show_user**
> UserDataResponse auth_show_user()



Returns authorized user data. This is recommended way to get the latest user's information.

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
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    api_response = api_instance.auth_show_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_show_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDataResponse**](UserDataResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_verify_email**
> Object auth_verify_email(code)



Verifies user's email address.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
code = 'code_example' # str | Email verification code (received by mail).

try:
    api_response = api_instance.auth_verify_email(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_verify_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Email verification code (received by mail). | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> Object update_settings(body)



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
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.UserSettingsObject() # UserSettingsObject | 

try:
    api_response = api_instance.update_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserSettingsObject**](UserSettingsObject.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_captcha**
> validate_captcha(body)



Validates user captcha.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
body = syntropy_sdk.Body1() # Body1 | 

try:
    api_instance.validate_captcha(body)
except ApiException as e:
    print("Exception when calling AuthApi->validate_captcha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_captcha_0**
> validate_captcha_0()



Validates if user limit has been reached.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()

try:
    api_instance.validate_captcha_0()
except ApiException as e:
    print("Exception when calling AuthApi->validate_captcha_0: %s\n" % e)
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

# **validate_user_credentials**
> validate_user_credentials(body)



Validates user credentials against legacy database.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
body = syntropy_sdk.Body() # Body | 

try:
    api_instance.validate_user_credentials(body)
except ApiException as e:
    print("Exception when calling AuthApi->validate_user_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

