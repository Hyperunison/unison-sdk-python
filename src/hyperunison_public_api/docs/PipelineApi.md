# hyperunison_public_api_sdk.PipelineApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_multi_pipeline**](PipelineApi.md#get_multi_pipeline) | **GET** /api/public/pipeline/{id} | 
[**run_custom_workflow**](PipelineApi.md#run_custom_workflow) | **POST** /api/public/pipeline/workflow/run/{pipelineVersionId}/ | 


# **get_multi_pipeline**
> MultiRunPipeline get_multi_pipeline(id)



### Example


```python
import time
import hyperunison_public_api_sdk
from hyperunison_public_api_sdk.api import pipeline_api
from hyperunison_public_api_sdk.model.multi_run_pipeline import MultiRunPipeline
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperunison_public_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with hyperunison_public_api_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pipeline_api.PipelineApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_multi_pipeline(id)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling PipelineApi->get_multi_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**MultiRunPipeline**](MultiRunPipeline.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get next task for runner agent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_custom_workflow**
> MultiRunPipeline run_custom_workflow(pipeline_version_id)



### Example


```python
import time
import hyperunison_public_api_sdk
from hyperunison_public_api_sdk.api import pipeline_api
from hyperunison_public_api_sdk.model.multi_run_pipeline import MultiRunPipeline
from hyperunison_public_api_sdk.model.run_custom_workflow_request import RunCustomWorkflowRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperunison_public_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with hyperunison_public_api_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pipeline_api.PipelineApi(api_client)
    pipeline_version_id = "4" # str | 
    run_custom_workflow_request = RunCustomWorkflowRequest(
        parameters=[],
        project="",
        biobanks=[],
        cohort="",
    ) # RunCustomWorkflowRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.run_custom_workflow(pipeline_version_id)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling PipelineApi->run_custom_workflow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.run_custom_workflow(pipeline_version_id, run_custom_workflow_request=run_custom_workflow_request)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling PipelineApi->run_custom_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_version_id** | **str**|  |
 **run_custom_workflow_request** | [**RunCustomWorkflowRequest**](RunCustomWorkflowRequest.md)|  | [optional]

### Return type

[**MultiRunPipeline**](MultiRunPipeline.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Just OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

