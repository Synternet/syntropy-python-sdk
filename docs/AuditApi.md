# syntropy_sdk.AuditApi

All URIs are relative to *https://api.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_network_audit_search**](AuditApi.md#v1_network_audit_search) | **POST** /v1/network/audit/logs/search | Search audit logs

# **v1_network_audit_search**
> V1NetworkAuditSearchResponse v1_network_audit_search(body)

Search audit logs

Retrieves list of audit logs by given criteria.

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
api_instance = syntropy_sdk.AuditApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkAuditSearchRequest() # V1NetworkAuditSearchRequest | Request

try:
    # Search audit logs
    api_response = api_instance.v1_network_audit_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->v1_network_audit_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAuditSearchRequest**](V1NetworkAuditSearchRequest.md)| Request | 

### Return type

[**V1NetworkAuditSearchResponse**](V1NetworkAuditSearchResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

