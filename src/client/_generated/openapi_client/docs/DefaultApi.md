# client._generated.openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_urls_url_list_get**](DefaultApi.md#get_all_urls_url_list_get) | **GET** /url-list | Get All Urls


# **get_all_urls_url_list_get**
> object get_all_urls_url_list_get()

Get All Urls

### Example


```python
import client._generated.openapi_client
from client._generated.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = client._generated.openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with client._generated.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client._generated.openapi_client.DefaultApi(api_client)

    try:
        # Get All Urls
        api_response = api_instance.get_all_urls_url_list_get()
        print("The response of DefaultApi->get_all_urls_url_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_urls_url_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

