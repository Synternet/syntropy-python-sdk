# syntropy_sdk.MFAApi

All URIs are relative to *https://controller-sandbox-server.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_mfa_secret**](MFAApi.md#confirm_mfa_secret) | **POST** /auth/mfa/confirm | Confirm MFA
[**disable_mfa**](MFAApi.md#disable_mfa) | **POST** /auth/mfa/disable | Disable MFA
[**disable_mfa_using_backup**](MFAApi.md#disable_mfa_using_backup) | **POST** /auth/mfa/disable-using-backup | Disable MFA (backup)
[**generate_mfa_secret**](MFAApi.md#generate_mfa_secret) | **GET** /auth/mfa/generate | Generate MFA

# **confirm_mfa_secret**
> list[str] confirm_mfa_secret(body)

Confirm MFA

Confirm MFA.

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
api_instance = syntropy_sdk.MFAApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.ConfirmMFARequest() # ConfirmMFARequest | 

try:
    # Confirm MFA
    api_response = api_instance.confirm_mfa_secret(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MFAApi->confirm_mfa_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfirmMFARequest**](ConfirmMFARequest.md)|  | 

### Return type

**list[str]**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_mfa**
> disable_mfa(body)

Disable MFA

Disable MFA.

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
api_instance = syntropy_sdk.MFAApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.DisableMFARequest() # DisableMFARequest | 

try:
    # Disable MFA
    api_instance.disable_mfa(body)
except ApiException as e:
    print("Exception when calling MFAApi->disable_mfa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DisableMFARequest**](DisableMFARequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_mfa_using_backup**
> disable_mfa_using_backup(body)

Disable MFA (backup)

Disable MFA (backup).

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
api_instance = syntropy_sdk.MFAApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.DisableMFAUsingBackupRequest() # DisableMFAUsingBackupRequest | 

try:
    # Disable MFA (backup)
    api_instance.disable_mfa_using_backup(body)
except ApiException as e:
    print("Exception when calling MFAApi->disable_mfa_using_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DisableMFAUsingBackupRequest**](DisableMFAUsingBackupRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mfa_secret**
> CodeGenerationResponse generate_mfa_secret()

Generate MFA

Generate MFA.

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
api_instance = syntropy_sdk.MFAApi(syntropy_sdk.ApiClient(configuration))

try:
    # Generate MFA
    api_response = api_instance.generate_mfa_secret()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MFAApi->generate_mfa_secret: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CodeGenerationResponse**](CodeGenerationResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

