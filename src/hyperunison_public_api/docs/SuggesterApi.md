# hyperunison_public_api_sdk.SuggesterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_suggests**](SuggesterApi.md#generate_suggests) | **GET** /api/public/suggester/generate/{code} | 


# **generate_suggests**
> DataItemDictionaryWithAccuracyListResponse generate_suggests(code)



### Example


```python
import time
import hyperunison_public_api_sdk
from hyperunison_public_api_sdk.api import suggester_api
from hyperunison_public_api_sdk.model.data_item_dictionary_with_accuracy_list_response import DataItemDictionaryWithAccuracyListResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperunison_public_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with hyperunison_public_api_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = suggester_api.SuggesterApi(api_client)
    code = "code_example" # str | 
    api_key = "apiKey_example" # str | Authorization by Api key (optional)
    api_key2 = "" # str | Authorization by Api key (optional) if omitted the server will use the default value of ""
    domain = "" # str | Domain value to generate suggests (by default - all available domains) (optional) if omitted the server will use the default value of ""
    vocabulary = "" # str | Vocabulary value to generate suggests (by default - all available vocabularies) (optional) if omitted the server will use the default value of ""
    only_standard_concept = "" # str | Suggest only standard concepts (by default - 1) (optional) if omitted the server will use the default value of ""
    min_accuracy_to_run_gpt = "" # str | Min accuracy rate to run suggester with ChatGPT (by default - 30) (optional) if omitted the server will use the default value of ""

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_suggests(code)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling SuggesterApi->generate_suggests: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_suggests(code, api_key=api_key, api_key2=api_key2, domain=domain, vocabulary=vocabulary, only_standard_concept=only_standard_concept, min_accuracy_to_run_gpt=min_accuracy_to_run_gpt)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling SuggesterApi->generate_suggests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  |
 **api_key** | **str**| Authorization by Api key | [optional]
 **api_key2** | **str**| Authorization by Api key | [optional] if omitted the server will use the default value of ""
 **domain** | **str**| Domain value to generate suggests (by default - all available domains) | [optional] if omitted the server will use the default value of ""
 **vocabulary** | **str**| Vocabulary value to generate suggests (by default - all available vocabularies) | [optional] if omitted the server will use the default value of ""
 **only_standard_concept** | **str**| Suggest only standard concepts (by default - 1) | [optional] if omitted the server will use the default value of ""
 **min_accuracy_to_run_gpt** | **str**| Min accuracy rate to run suggester with ChatGPT (by default - 30) | [optional] if omitted the server will use the default value of ""

### Return type

[**DataItemDictionaryWithAccuracyListResponse**](DataItemDictionaryWithAccuracyListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generate suggestion response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

