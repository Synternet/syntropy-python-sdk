# syntropy_sdk.AuthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_delete_account**](AuthApi.md#auth_delete_account) | **GET** /api/auth/delete-account/{code} | 
[**auth_geoip**](AuthApi.md#auth_geoip) | **GET** /api/auth/{ip}/geoip | 
[**auth_local_login**](AuthApi.md#auth_local_login) | **POST** /api/auth/local/login | 
[**auth_logout**](AuthApi.md#auth_logout) | **POST** /api/auth/logout | 
[**auth_pair_latency_test_report**](AuthApi.md#auth_pair_latency_test_report) | **POST** /api/auth/pair-latency-test-report | 
[**auth_pair_latency_test_report_bulk**](AuthApi.md#auth_pair_latency_test_report_bulk) | **POST** /api/auth/pair-latency-test-report/bulk | 
[**auth_pair_speedtest_report**](AuthApi.md#auth_pair_speedtest_report) | **POST** /api/auth/pair-speedtest-report | 
[**auth_provider_attach**](AuthApi.md#auth_provider_attach) | **POST** /api/auth/provider/attach | 
[**auth_provider_detach**](AuthApi.md#auth_provider_detach) | **POST** /api/auth/provider/detach | 
[**auth_provider_login**](AuthApi.md#auth_provider_login) | **POST** /api/auth/provider/login | 
[**auth_provider_register**](AuthApi.md#auth_provider_register) | **POST** /api/auth/provider/register | 
[**auth_refresh_token**](AuthApi.md#auth_refresh_token) | **POST** /api/auth/refresh-token | 
[**auth_register**](AuthApi.md#auth_register) | **POST** /api/auth/register | 
[**auth_reset_password**](AuthApi.md#auth_reset_password) | **POST** /api/auth/reset-password | 
[**auth_send_delete_account_link**](AuthApi.md#auth_send_delete_account_link) | **POST** /api/auth/send-delete-account-link | 
[**auth_send_reset_password_link**](AuthApi.md#auth_send_reset_password_link) | **POST** /api/auth/send-reset-password-link | 
[**auth_send_verify_email_link**](AuthApi.md#auth_send_verify_email_link) | **POST** /api/auth/send-verify-email-link | 
[**auth_speedtest_report**](AuthApi.md#auth_speedtest_report) | **POST** /api/auth/speedtest-report | 
[**auth_user**](AuthApi.md#auth_user) | **GET** /api/auth/user | 
[**auth_user_change_email**](AuthApi.md#auth_user_change_email) | **POST** /api/auth/user/change-email | 
[**auth_user_change_password**](AuthApi.md#auth_user_change_password) | **POST** /api/auth/user/change-password | 
[**auth_user_delete**](AuthApi.md#auth_user_delete) | **POST** /api/auth/user/delete | 
[**auth_user_host_create**](AuthApi.md#auth_user_host_create) | **POST** /api/auth/user/hosts | 
[**auth_user_host_destroy**](AuthApi.md#auth_user_host_destroy) | **DELETE** /api/auth/user/hosts/{id} | 
[**auth_user_host_index**](AuthApi.md#auth_user_host_index) | **GET** /api/auth/user/hosts | 
[**auth_verify_email**](AuthApi.md#auth_verify_email) | **GET** /api/auth/verify-email/{code} | 
[**auth_verify_email_deprecated**](AuthApi.md#auth_verify_email_deprecated) | **POST** /api/auth/verify-email | 

# **auth_delete_account**
> Object auth_delete_account(code)



Deletes user's account.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
code = 'code_example' # str | Account deletion code (received by mail).

try:
    api_response = api_instance.auth_delete_account(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Account deletion code (received by mail). | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_geoip**
> GeoIpObject auth_geoip(ip)



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
ip = 'ip_example' # str | 

try:
    api_response = api_instance.auth_geoip(ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_geoip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**|  | 

### Return type

[**GeoIpObject**](GeoIpObject.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_local_login**
> AuthInfo auth_local_login(body)



Log ins user using local credentials.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.auth_local_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_local_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**AuthInfo**](AuthInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_logout**
> auth_logout()



Log ins user using local credentials.

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

# **auth_pair_latency_test_report**
> Object auth_pair_latency_test_report(body)



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
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.auth_pair_latency_test_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_pair_latency_test_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_pair_latency_test_report_bulk**
> Object auth_pair_latency_test_report_bulk(body)



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
body = [syntropy_sdk.UserPairLatencyTestReportObject()] # list[UserPairLatencyTestReportObject] | 

try:
    api_response = api_instance.auth_pair_latency_test_report_bulk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_pair_latency_test_report_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UserPairLatencyTestReportObject]**](UserPairLatencyTestReportObject.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_pair_speedtest_report**
> Object auth_pair_speedtest_report(body)



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
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.auth_pair_speedtest_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_pair_speedtest_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_provider_attach**
> Object auth_provider_attach(body)



Attached social account to local account.

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
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.auth_provider_attach(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_provider_attach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_provider_detach**
> Object auth_provider_detach(body)



Detaches social account from local account.

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
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.auth_provider_detach(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_provider_detach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_provider_login**
> AuthInfo auth_provider_login(body)



Log ins to local account using social account credentials.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.auth_provider_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_provider_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**AuthInfo**](AuthInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_provider_register**
> AuthInfo auth_provider_register(body, attach=attach)



Creates user using provider credentials.Social provider must be attached to main account.

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
body = NULL # dict(str, object) | 
attach = syntropy_sdk.AutoAttach() # AutoAttach |  (optional)

try:
    api_response = api_instance.auth_provider_register(body, attach=attach)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_provider_register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **attach** | [**AutoAttach**](.md)|  | [optional] 

### Return type

[**AuthInfo**](AuthInfo.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_refresh_token**
> AuthInfo auth_refresh_token(refresh_token)



Issues access token and refresh token with new expiration dates and latest user info.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
refresh_token = 'refresh_token_example' # str | 

try:
    api_response = api_instance.auth_refresh_token(refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**|  | 

### Return type

[**AuthInfo**](AuthInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_register**
> AuthInfo auth_register(body, ref=ref)



Creates user using supplied local credentials. Optionally, social provider can be attached to main account.

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
body = NULL # dict(str, object) | 
ref = syntropy_sdk.MailBodyTemplates() # MailBodyTemplates |  (optional)

try:
    api_response = api_instance.auth_register(body, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **ref** | [**MailBodyTemplates**](.md)|  | [optional] 

### Return type

[**AuthInfo**](AuthInfo.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_reset_password**
> Object auth_reset_password(body)



Sets password reset code owner's password to new password.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.auth_reset_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_send_delete_account_link**
> Object auth_send_delete_account_link(ref=ref)



Populates or updates user's (find by mail) account deletion code.

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
ref = syntropy_sdk.MailBodyTemplates() # MailBodyTemplates |  (optional)

try:
    api_response = api_instance.auth_send_delete_account_link(ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_send_delete_account_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | [**MailBodyTemplates**](.md)|  | [optional] 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_send_reset_password_link**
> Object auth_send_reset_password_link(body, ref=ref)



Populates or updates user's (find by email) password reset code.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
body = NULL # dict(str, object) | 
ref = syntropy_sdk.MailBodyTemplates() # MailBodyTemplates |  (optional)

try:
    api_response = api_instance.auth_send_reset_password_link(body, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_send_reset_password_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **ref** | [**MailBodyTemplates**](.md)|  | [optional] 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_send_verify_email_link**
> Object auth_send_verify_email_link(body, ref=ref)



Populates or updates user's (find by email) email verification code.

### Example
```python
from __future__ import print_function
import time
import syntropy_sdk
from syntropy_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = syntropy_sdk.AuthApi()
body = NULL # dict(str, object) | 
ref = syntropy_sdk.MailBodyTemplates() # MailBodyTemplates |  (optional)

try:
    api_response = api_instance.auth_send_verify_email_link(body, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_send_verify_email_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **ref** | [**MailBodyTemplates**](.md)|  | [optional] 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_speedtest_report**
> Object auth_speedtest_report(body)



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
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.auth_speedtest_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_speedtest_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user**
> AuthUserObject auth_user()



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
    api_response = api_instance.auth_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthUserObject**](AuthUserObject.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_change_email**
> ResponseObject auth_user_change_email(body, ref=ref)



Changes authorized user's email address. Changing email address invalidates email confirmation and required reconfirmation.

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
body = NULL # dict(str, object) | 
ref = syntropy_sdk.MailBodyTemplates() # MailBodyTemplates |  (optional)

try:
    api_response = api_instance.auth_user_change_email(body, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_change_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **ref** | [**MailBodyTemplates**](.md)|  | [optional] 

### Return type

[**ResponseObject**](ResponseObject.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_change_password**
> auth_user_change_password(body)



Changes authorized user's password.

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
body = NULL # dict(str, object) | 

try:
    api_instance.auth_user_change_password(body)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_delete**
> auth_user_delete(body)



Removes current logged in user from database.

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
body = NULL # dict(str, object) | 

try:
    api_instance.auth_user_delete(body)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_host_create**
> UserHostObject auth_user_host_create(body)



Creates CUSTOM host entry where owner is logged in user.

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
body = NULL # dict(str, object) | 

try:
    api_response = api_instance.auth_user_host_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_host_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**UserHostObject**](UserHostObject.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_host_destroy**
> Object auth_user_host_destroy(id)



Deletes CUSTOM host where owner is logged in user.

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
id = 1.2 # float | 

try:
    api_response = api_instance.auth_user_host_destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_host_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**Object**](Object.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_host_index**
> list[UserHostObject] auth_user_host_index()



Returns authorized user available hosts.

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
    api_response = api_instance.auth_user_host_index()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_host_index: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserHostObject]**](UserHostObject.md)

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

# **auth_verify_email_deprecated**
> Object auth_verify_email_deprecated(body)



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
body = NULL # dict(str, object) | Email verification code (received by mail).

try:
    api_response = api_instance.auth_verify_email_deprecated(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_verify_email_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)| Email verification code (received by mail). | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

