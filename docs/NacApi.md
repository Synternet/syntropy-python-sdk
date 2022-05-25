# syntropy_sdk.NacApi

All URIs are relative to *https://api-sandbox.syntropystack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_network_nac_config_export**](NacApi.md#v1_network_nac_config_export) | **POST** /v1/network/nac/config/export | Export Nac config

# **v1_network_nac_config_export**
> V1NetworkNacConfigExportResponse v1_network_nac_config_export(body=body)

Export Nac config

Exports Network as a code config

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
api_instance = syntropy_sdk.NacApi(syntropy_sdk.ApiClient(configuration))
body = syntropy_sdk.V1NetworkNacConfigExportRequest() # V1NetworkNacConfigExportRequest |  (optional)

try:
    # Export Nac config
    api_response = api_instance.v1_network_nac_config_export(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NacApi->v1_network_nac_config_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkNacConfigExportRequest**](V1NetworkNacConfigExportRequest.md)|  | [optional] 

### Return type

[**V1NetworkNacConfigExportResponse**](V1NetworkNacConfigExportResponse.md)

### Authorization

[accessToken](../README.md#accessToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

