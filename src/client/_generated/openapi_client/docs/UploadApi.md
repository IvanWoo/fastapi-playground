# client._generated.openapi_client.UploadApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_file_upload_post**](UploadApi.md#upload_file_upload_post) | **POST** /upload/ | Upload File
[**upload_files_upload_many_post**](UploadApi.md#upload_files_upload_many_post) | **POST** /upload-many/ | Upload Files


# **upload_file_upload_post**
> object upload_file_upload_post(file)

Upload File

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
    api_instance = client._generated.openapi_client.UploadApi(api_client)
    file = None # bytearray | 

    try:
        # Upload File
        api_response = api_instance.upload_file_upload_post(file)
        print("The response of UploadApi->upload_file_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->upload_file_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_files_upload_many_post**
> object upload_files_upload_many_post(files, entity)

Upload Files

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
    api_instance = client._generated.openapi_client.UploadApi(api_client)
    files = None # List[bytearray] | 
    entity = 'entity_example' # str | 

    try:
        # Upload Files
        api_response = api_instance.upload_files_upload_many_post(files, entity)
        print("The response of UploadApi->upload_files_upload_many_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->upload_files_upload_many_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **List[bytearray]**|  | 
 **entity** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

