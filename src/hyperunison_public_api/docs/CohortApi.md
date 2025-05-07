# hyperunison_public_api_sdk.CohortApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_cohort_execute_query**](CohortApi.md#public_cohort_execute_query) | **POST** /api/public/cohort/biobank/execute-query | 


# **public_cohort_execute_query**
> ResponseToUCDMResultWithSql public_cohort_execute_query(api_key)



### Example


```python
import time
import hyperunison_public_api_sdk
from hyperunison_public_api_sdk.api import cohort_api
from hyperunison_public_api_sdk.model.public_cohort_execute_query_request import PublicCohortExecuteQueryRequest
from hyperunison_public_api_sdk.model.response_to_ucdm_result_with_sql import ResponseToUCDMResultWithSql
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperunison_public_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with hyperunison_public_api_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cohort_api.CohortApi(api_client)
    api_key = "apiKey_example" # str | Authorization by Api key
    public_cohort_execute_query_request = PublicCohortExecuteQueryRequest(
        yaml="yaml_example",
        skip_cache="skip_cache_example",
    ) # PublicCohortExecuteQueryRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.public_cohort_execute_query(api_key)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling CohortApi->public_cohort_execute_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.public_cohort_execute_query(api_key, public_cohort_execute_query_request=public_cohort_execute_query_request)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling CohortApi->public_cohort_execute_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Authorization by Api key |
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

