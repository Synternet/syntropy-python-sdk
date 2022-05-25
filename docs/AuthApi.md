# syntropy_sdk.AuthApi

All URIs are relative to *https://api-sandbox.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_network_auth_access_token_login**](AuthApi.md#v1_network_auth_access_token_login) | **POST** /v1/network/auth/access-token/login | Login (Access token)
[**v1_network_auth_access_tokens_create**](AuthApi.md#v1_network_auth_access_tokens_create) | **POST** /v1/network/auth/access-tokens | Create Access token
[**v1_network_auth_access_tokens_delete**](AuthApi.md#v1_network_auth_access_tokens_delete) | **DELETE** /v1/network/auth/access-tokens/{access_token_id} | Delete Access token
[**v1_network_auth_access_tokens_get**](AuthApi.md#v1_network_auth_access_tokens_get) | **GET** /v1/network/auth/access-tokens | Get Access tokens
[**v1_network_auth_access_tokens_permissions_get**](AuthApi.md#v1_network_auth_access_tokens_permissions_get) | **GET** /v1/network/auth/access-tokens/permissions | Get Access token permissions
[**v1_network_auth_api_keys_create**](AuthApi.md#v1_network_auth_api_keys_create) | **POST** /v1/network/auth/api-keys | Create API key
[**v1_network_auth_api_keys_delete**](AuthApi.md#v1_network_auth_api_keys_delete) | **DELETE** /v1/network/auth/api-keys/{api_key_id} | Delete API key
[**v1_network_auth_api_keys_get**](AuthApi.md#v1_network_auth_api_keys_get) | **GET** /v1/network/auth/api-keys | Get API keys
[**v1_network_auth_logout**](AuthApi.md#v1_network_auth_logout) | **POST** /v1/network/auth/logout | Logout
[**v1_network_auth_mfa_confirm**](AuthApi.md#v1_network_auth_mfa_confirm) | **POST** /v1/network/auth/mfa/confirm | Confirm MFA
[**v1_network_auth_mfa_disable**](AuthApi.md#v1_network_auth_mfa_disable) | **POST** /v1/network/auth/mfa/disable | Disable MFA
[**v1_network_auth_mfa_disable_using_backup**](AuthApi.md#v1_network_auth_mfa_disable_using_backup) | **POST** /v1/network/auth/mfa/disable-using-backup | Disable MFA (backup)
[**v1_network_auth_mfa_generate**](AuthApi.md#v1_network_auth_mfa_generate) | **GET** /v1/network/auth/mfa/generate | Generate MFA
[**v1_network_auth_settings_update**](AuthApi.md#v1_network_auth_settings_update) | **PATCH** /v1/network/auth/user/settings | Update User settings
[**v1_network_auth_user_get**](AuthApi.md#v1_network_auth_user_get) | **GET** /v1/network/auth/user | Get User info
[**v1_network_auth_user_invitations_get**](AuthApi.md#v1_network_auth_user_invitations_get) | **GET** /v1/network/auth/user/invitations | Get invitations for authenticated user
[**v1_network_auth_users_get**](AuthApi.md#v1_network_auth_users_get) | **GET** /v1/network/auth/users | Get workspace users
[**v1_network_auth_users_remove**](AuthApi.md#v1_network_auth_users_remove) | **POST** /v1/network/auth/users/remove | Remove users from workspace
[**v1_network_auth_users_role_update**](AuthApi.md#v1_network_auth_users_role_update) | **PATCH** /v1/network/auth/users/{user_id}/role | Update user role in the workspace
[**v1_network_auth_verify_email**](AuthApi.md#v1_network_auth_verify_email) | **POST** /v1/network/auth/verify-email/{code} | Verify email
[**v1_network_auth_workspace_create**](AuthApi.md#v1_network_auth_workspace_create) | **POST** /v1/network/auth/workspaces | Create workspace
[**v1_network_auth_workspace_delete**](AuthApi.md#v1_network_auth_workspace_delete) | **DELETE** /v1/network/auth/workspaces/{workspace_id} | Delete workspace
[**v1_network_auth_workspace_get**](AuthApi.md#v1_network_auth_workspace_get) | **GET** /v1/network/auth/workspaces | Get workspaces
[**v1_network_auth_workspace_update**](AuthApi.md#v1_network_auth_workspace_update) | **PATCH** /v1/network/auth/workspaces/{workspace_id} | Update workspace
[**v1_network_auth_workspaces_invitations_accept**](AuthApi.md#v1_network_auth_workspaces_invitations_accept) | **POST** /v1/network/auth/workspaces/invitations/{invitation_id}/accept | Accept workspace invitation
[**v1_network_auth_workspaces_invitations_create**](AuthApi.md#v1_network_auth_workspaces_invitations_create) | **POST** /v1/network/auth/workspaces/invitations | Create workspace invitation
[**v1_network_auth_workspaces_invitations_decline**](AuthApi.md#v1_network_auth_workspaces_invitations_decline) | **POST** /v1/network/auth/workspaces/invitations/{invitation_id}/decline | Decline workspace invitation
[**v1_network_auth_workspaces_invitations_get**](AuthApi.md#v1_network_auth_workspaces_invitations_get) | **GET** /v1/network/auth/workspaces/invitations | Get workspace invitations
[**v1_network_auth_workspaces_invitations_remove**](AuthApi.md#v1_network_auth_workspaces_invitations_remove) | **POST** /v1/network/auth/workspaces/invitations/remove | Delete workspace invitations
[**v1_network_auth_workspaces_leave**](AuthApi.md#v1_network_auth_workspaces_leave) | **POST** /v1/network/auth/workspaces/leave | Leave workspace

# **v1_network_auth_access_token_login**
> V1NetworkAuthAccessTokenLoginResponse v1_network_auth_access_token_login(body)

Login (Access token)

Retrieve JWT from Access token.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
body = syntropy_sdk.V1NetworkAuthAccessTokenLoginRequest() # V1NetworkAuthAccessTokenLoginRequest | 

try:
    # Login (Access token)
    api_response = api_instance.v1_network_auth_access_token_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_access_token_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthAccessTokenLoginRequest**](V1NetworkAuthAccessTokenLoginRequest.md)|  | 

### Return type

[**V1NetworkAuthAccessTokenLoginResponse**](V1NetworkAuthAccessTokenLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_access_tokens_create**
> V1NetworkAuthAccessTokensCreateResponse v1_network_auth_access_tokens_create(body)

Create Access token

Creates Access token.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuthAccessTokensCreateRequest() # V1NetworkAuthAccessTokensCreateRequest | 

try:
    # Create Access token
    api_response = api_instance.v1_network_auth_access_tokens_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_access_tokens_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthAccessTokensCreateRequest**](V1NetworkAuthAccessTokensCreateRequest.md)|  | 

### Return type

[**V1NetworkAuthAccessTokensCreateResponse**](V1NetworkAuthAccessTokensCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_access_tokens_delete**
> v1_network_auth_access_tokens_delete(access_token_id)

Delete Access token

Deletes Access token.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
access_token_id = 'access_token_id_example' # str | 

try:
    # Delete Access token
    api_instance.v1_network_auth_access_tokens_delete(access_token_id)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_access_tokens_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_access_tokens_get**
> V1NetworkAuthAccessTokensGetResponse v1_network_auth_access_tokens_get(skip=skip, take=take, order=order)

Get Access tokens

Lists Access tokens.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
skip = syntropy_sdk.SkipNumber() # SkipNumber |  (optional)
take = syntropy_sdk.TakeNumber() # TakeNumber |  (optional)
order = syntropy_sdk.AccessTokenOrder() # AccessTokenOrder |  (optional)

try:
    # Get Access tokens
    api_response = api_instance.v1_network_auth_access_tokens_get(skip=skip, take=take, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_access_tokens_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | [**SkipNumber**](.md)|  | [optional] 
 **take** | [**TakeNumber**](.md)|  | [optional] 
 **order** | [**AccessTokenOrder**](.md)|  | [optional] 

### Return type

[**V1NetworkAuthAccessTokensGetResponse**](V1NetworkAuthAccessTokensGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_access_tokens_permissions_get**
> V1NetworkAuthAccessTokensPermissionsGetResponse v1_network_auth_access_tokens_permissions_get()

Get Access token permissions

Retrieves a list of Access token permissions

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    # Get Access token permissions
    api_response = api_instance.v1_network_auth_access_tokens_permissions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_access_tokens_permissions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1NetworkAuthAccessTokensPermissionsGetResponse**](V1NetworkAuthAccessTokensPermissionsGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_api_keys_create**
> V1NetworkAuthApiKeysCreateResponse v1_network_auth_api_keys_create(body)

Create API key

Creates API key.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuthApiKeysCreateRequest() # V1NetworkAuthApiKeysCreateRequest | 

try:
    # Create API key
    api_response = api_instance.v1_network_auth_api_keys_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_api_keys_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthApiKeysCreateRequest**](V1NetworkAuthApiKeysCreateRequest.md)|  | 

### Return type

[**V1NetworkAuthApiKeysCreateResponse**](V1NetworkAuthApiKeysCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_api_keys_delete**
> v1_network_auth_api_keys_delete(api_key_id)

Delete API key

Deletes API key.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
api_key_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Delete API key
    api_instance.v1_network_auth_api_keys_delete(api_key_id)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_api_keys_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_api_keys_get**
> V1NetworkAuthApiKeysGetResponse v1_network_auth_api_keys_get(skip=skip, take=take, order=order, filter=filter)

Get API keys

Gets API keys.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
skip = syntropy_sdk.SkipNumber() # SkipNumber |  (optional)
take = syntropy_sdk.TakeNumber() # TakeNumber |  (optional)
order = syntropy_sdk.OrderString() # OrderString | string: \"ASC\" | \"DESC\" (optional)
filter = syntropy_sdk.WhereString() # WhereString | array of api_key_ids (optional)

try:
    # Get API keys
    api_response = api_instance.v1_network_auth_api_keys_get(skip=skip, take=take, order=order, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_api_keys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | [**SkipNumber**](.md)|  | [optional] 
 **take** | [**TakeNumber**](.md)|  | [optional] 
 **order** | [**OrderString**](.md)| string: \&quot;ASC\&quot; | \&quot;DESC\&quot; | [optional] 
 **filter** | [**WhereString**](.md)| array of api_key_ids | [optional] 

### Return type

[**V1NetworkAuthApiKeysGetResponse**](V1NetworkAuthApiKeysGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_logout**
> v1_network_auth_logout()

Logout

Deletes session cookies.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    # Logout
    api_instance.v1_network_auth_logout()
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_mfa_confirm**
> V1NetworkAuthMfaConfirmResponse v1_network_auth_mfa_confirm(body)

Confirm MFA

Confirms MFA.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuthMfaConfirmRequest() # V1NetworkAuthMfaConfirmRequest | 

try:
    # Confirm MFA
    api_response = api_instance.v1_network_auth_mfa_confirm(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_mfa_confirm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthMfaConfirmRequest**](V1NetworkAuthMfaConfirmRequest.md)|  | 

### Return type

[**V1NetworkAuthMfaConfirmResponse**](V1NetworkAuthMfaConfirmResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_mfa_disable**
> v1_network_auth_mfa_disable(body)

Disable MFA

Disables MFA.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuthMfaDisableRequest() # V1NetworkAuthMfaDisableRequest | 

try:
    # Disable MFA
    api_instance.v1_network_auth_mfa_disable(body)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_mfa_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthMfaDisableRequest**](V1NetworkAuthMfaDisableRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_mfa_disable_using_backup**
> v1_network_auth_mfa_disable_using_backup(body)

Disable MFA (backup)

Disables MFA using backup.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuthMfaDisableUsingBackupRequest() # V1NetworkAuthMfaDisableUsingBackupRequest | 

try:
    # Disable MFA (backup)
    api_instance.v1_network_auth_mfa_disable_using_backup(body)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_mfa_disable_using_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthMfaDisableUsingBackupRequest**](V1NetworkAuthMfaDisableUsingBackupRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_mfa_generate**
> V1NetworkAuthMfaGenerateResponse v1_network_auth_mfa_generate()

Generate MFA

Generates MFA.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    # Generate MFA
    api_response = api_instance.v1_network_auth_mfa_generate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_mfa_generate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1NetworkAuthMfaGenerateResponse**](V1NetworkAuthMfaGenerateResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_settings_update**
> v1_network_auth_settings_update(body)

Update User settings

Updates User settings.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.UserSettingsUpdateBody() # UserSettingsUpdateBody | 

try:
    # Update User settings
    api_instance.v1_network_auth_settings_update(body)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserSettingsUpdateBody**](UserSettingsUpdateBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_user_get**
> V1NetworkAuthUserGetResponse v1_network_auth_user_get()

Get User info

Returns authorized User data. This is recommended way to get the latest user's information.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    # Get User info
    api_response = api_instance.v1_network_auth_user_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1NetworkAuthUserGetResponse**](V1NetworkAuthUserGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_user_invitations_get**
> V1NetworkAuthUserInvitationsGetResponse v1_network_auth_user_invitations_get()

Get invitations for authenticated user

Gets invitations for authenticated user.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    # Get invitations for authenticated user
    api_response = api_instance.v1_network_auth_user_invitations_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_user_invitations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1NetworkAuthUserInvitationsGetResponse**](V1NetworkAuthUserInvitationsGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_users_get**
> V1NetworkAuthUsersGetResponse v1_network_auth_users_get()

Get workspace users

Gets workspace users.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    # Get workspace users
    api_response = api_instance.v1_network_auth_users_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1NetworkAuthUsersGetResponse**](V1NetworkAuthUsersGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_users_remove**
> v1_network_auth_users_remove(body)

Remove users from workspace

Removes users from workspace.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuthUsersRemoveRequest() # V1NetworkAuthUsersRemoveRequest | 

try:
    # Remove users from workspace
    api_instance.v1_network_auth_users_remove(body)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_users_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthUsersRemoveRequest**](V1NetworkAuthUsersRemoveRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_users_role_update**
> v1_network_auth_users_role_update(body, user_id)

Update user role in the workspace

Updates user role in the workspace.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuthUsersRoleUpdateRequest() # V1NetworkAuthUsersRoleUpdateRequest | 
user_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Update user role in the workspace
    api_instance.v1_network_auth_users_role_update(body, user_id)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_users_role_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthUsersRoleUpdateRequest**](V1NetworkAuthUsersRoleUpdateRequest.md)|  | 
 **user_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_verify_email**
> v1_network_auth_verify_email(code)

Verify email

Verifies User's email address.

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
    api_instance.v1_network_auth_verify_email(code)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_verify_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Email verification code (received by mail). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_workspace_create**
> V1NetworkAuthWorkspaceCreateResponse v1_network_auth_workspace_create(body)

Create workspace

Creates workspace.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuthWorkspaceCreateRequest() # V1NetworkAuthWorkspaceCreateRequest | 

try:
    # Create workspace
    api_response = api_instance.v1_network_auth_workspace_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_workspace_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthWorkspaceCreateRequest**](V1NetworkAuthWorkspaceCreateRequest.md)|  | 

### Return type

[**V1NetworkAuthWorkspaceCreateResponse**](V1NetworkAuthWorkspaceCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_workspace_delete**
> v1_network_auth_workspace_delete(workspace_id)

Delete workspace

Deletes workspace.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
workspace_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Delete workspace
    api_instance.v1_network_auth_workspace_delete(workspace_id)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_workspace_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_workspace_get**
> V1NetworkAuthWorkspaceGetResponse v1_network_auth_workspace_get()

Get workspaces

Gets workspaces.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    # Get workspaces
    api_response = api_instance.v1_network_auth_workspace_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_workspace_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1NetworkAuthWorkspaceGetResponse**](V1NetworkAuthWorkspaceGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_workspace_update**
> v1_network_auth_workspace_update(body, workspace_id)

Update workspace

Updates workspace.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuthWorkspaceUpdateRequest() # V1NetworkAuthWorkspaceUpdateRequest | 
workspace_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Update workspace
    api_instance.v1_network_auth_workspace_update(body, workspace_id)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_workspace_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthWorkspaceUpdateRequest**](V1NetworkAuthWorkspaceUpdateRequest.md)|  | 
 **workspace_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_workspaces_invitations_accept**
> v1_network_auth_workspaces_invitations_accept(invitation_id)

Accept workspace invitation

Accepts workspace invitation.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
invitation_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Accept workspace invitation
    api_instance.v1_network_auth_workspaces_invitations_accept(invitation_id)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_workspaces_invitations_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_workspaces_invitations_create**
> V1NetworkAuthWorkspacesInvitationsCreateResponse v1_network_auth_workspaces_invitations_create(body)

Create workspace invitation

Creates workspace invitation.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuthWorkspacesInvitationsCreateRequest() # V1NetworkAuthWorkspacesInvitationsCreateRequest | 

try:
    # Create workspace invitation
    api_response = api_instance.v1_network_auth_workspaces_invitations_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_workspaces_invitations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthWorkspacesInvitationsCreateRequest**](V1NetworkAuthWorkspacesInvitationsCreateRequest.md)|  | 

### Return type

[**V1NetworkAuthWorkspacesInvitationsCreateResponse**](V1NetworkAuthWorkspacesInvitationsCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_workspaces_invitations_decline**
> v1_network_auth_workspaces_invitations_decline(invitation_id)

Decline workspace invitation

Declines workspace invitation.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
invitation_id = syntropy_sdk.IdNumber() # IdNumber | 

try:
    # Decline workspace invitation
    api_instance.v1_network_auth_workspaces_invitations_decline(invitation_id)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_workspaces_invitations_decline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | [**IdNumber**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_workspaces_invitations_get**
> V1NetworkAuthWorkspacesInvitationsGetResponse v1_network_auth_workspaces_invitations_get()

Get workspace invitations

Gets workspace invitations.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    # Get workspace invitations
    api_response = api_instance.v1_network_auth_workspaces_invitations_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_workspaces_invitations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1NetworkAuthWorkspacesInvitationsGetResponse**](V1NetworkAuthWorkspacesInvitationsGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_workspaces_invitations_remove**
> v1_network_auth_workspaces_invitations_remove(body)

Delete workspace invitations

Deletes workspace invitations.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuthWorkspacesInvitationsRemoveRequest() # V1NetworkAuthWorkspacesInvitationsRemoveRequest | 

try:
    # Delete workspace invitations
    api_instance.v1_network_auth_workspaces_invitations_remove(body)
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_workspaces_invitations_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuthWorkspacesInvitationsRemoveRequest**](V1NetworkAuthWorkspacesInvitationsRemoveRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_network_auth_workspaces_leave**
> v1_network_auth_workspaces_leave()

Leave workspace

Leaves workspace.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessToken
configuration = syntropy_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi(syntropy_sdk.ApiClient(configuration))

try:
    # Leave workspace
    api_instance.v1_network_auth_workspaces_leave()
except ApiException as e:
    print("Exception when calling AuthApi->v1_network_auth_workspaces_leave: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

