# auto_api_client.PublicAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_cohort_execute_query**](PublicAPIApi.md#public_cohort_execute_query) | **POST** /api/public/cohort/biobank/{biobankId}/execute-query | 


# **public_cohort_execute_query**
> ResponseToUCDMResultWithSql public_cohort_execute_query(api_key, biobank_id)



### Example


```python
import time
import auto_api_client
from auto_api_client.api import public_api_api
from auto_api_client.model.public_cohort_execute_query_request import PublicCohortExecuteQueryRequest
from auto_api_client.model.response_to_ucdm_result_with_sql import ResponseToUCDMResultWithSql
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auto_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with auto_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api_api.PublicAPIApi(api_client)
    api_key = "apiKey_example" # str | Authorization by Api key
    biobank_id = "4" # str | 
    public_cohort_execute_query_request = PublicCohortExecuteQueryRequest(
        yaml="yaml_example",
        skip_cache="skip_cache_example",
    ) # PublicCohortExecuteQueryRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.public_cohort_execute_query(api_key, biobank_id)
        pprint(api_response)
    except auto_api_client.ApiException as e:
        print("Exception when calling PublicAPIApi->public_cohort_execute_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.public_cohort_execute_query(api_key, biobank_id, public_cohort_execute_query_request=public_cohort_execute_query_request)
        pprint(api_response)
    except auto_api_client.ApiException as e:
        print("Exception when calling PublicAPIApi->public_cohort_execute_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Authorization by Api key |
 **biobank_id** | **str**|  |
 **public_cohort_execute_query_request** | [**PublicCohortExecuteQueryRequest**](PublicCohortExecuteQueryRequest.md)|  | [optional]

### Return type

[**ResponseToUCDMResultWithSql**](ResponseToUCDMResultWithSql.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get UCDM result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

