# syntropy_sdk.AuthApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contact**](AuthApi.md#add_contact) | **POST** /auth/authorization/contact | Update user contacts
[**auth_access_token_list**](AuthApi.md#auth_access_token_list) | **GET** /auth/authorization/access-token | Get access tokens
[**auth_access_token_login**](AuthApi.md#auth_access_token_login) | **POST** /auth/authorization/access-token/login | Login (access token)
[**auth_access_token_permissions_list**](AuthApi.md#auth_access_token_permissions_list) | **GET** /auth/authorization/permissions/access-token | Get access token permissions
[**auth_access_token_user_create**](AuthApi.md#auth_access_token_user_create) | **POST** /auth/authorization/access-token | Create access token
[**auth_access_token_user_delete**](AuthApi.md#auth_access_token_user_delete) | **DELETE** /auth/authorization/access-token/{id} | Delete access token
[**auth_logout**](AuthApi.md#auth_logout) | **POST** /auth/authorization/logout | Logout
[**auth_show_user**](AuthApi.md#auth_show_user) | **GET** /auth/authorization/user | Get user info
[**auth_verify_email**](AuthApi.md#auth_verify_email) | **GET** /auth/authorization/verify-email/{code} | Verify email
[**update_settings**](AuthApi.md#update_settings) | **PUT** /auth/authorization/settings | Update user settings

# **add_contact**
> Object add_contact(body)

Update user contacts

Update contacts information.

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
    # Update user contacts
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

# **auth_access_token_list**
> list[AccessTokenReadData] auth_access_token_list(skip=skip, take=take, order=order)

Get access tokens

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
    # Get access tokens
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

Login (access token)

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
    # Login (access token)
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

Get access token permissions

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
    # Get access token permissions
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

Create access token

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
    # Create access token
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

Delete access token

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
    # Delete access token
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

# **auth_logout**
> auth_logout()

Logout

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
    # Logout
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

Get user info

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
    # Get user info
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

Verify email

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
    # Verify email
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
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.UserSettingsObject() # UserSettingsObject | 

try:
    # Update user settings
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

