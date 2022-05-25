# syntropy_sdk.NotificationApi

All URIs are relative to *https://api-sandbox.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_network_notification_user_contact_update**](NotificationApi.md#v1_network_notification_user_contact_update) | **POST** /v1/network/notification/user-contact | Update User contact

# **v1_network_notification_user_contact_update**
> v1_network_notification_user_contact_update(body)

Update User contact

Updates User contact information.

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
api_instance = syntropy_sdk.NotificationApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkNotificationContactUpdateRequest() # V1NetworkNotificationContactUpdateRequest | 

try:
    # Update User contact
    api_instance.v1_network_notification_user_contact_update(body)
except ApiException as e:
    print("Exception when calling NotificationApi->v1_network_notification_user_contact_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkNotificationContactUpdateRequest**](V1NetworkNotificationContactUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

