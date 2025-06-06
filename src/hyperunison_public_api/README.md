# hyperunison-public-api-sdk
API for Python and R libraries

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonPriorClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import hyperunison_public_api_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import hyperunison_public_api_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import hyperunison_public_api_sdk
from pprint import pprint
from hyperunison_public_api_sdk.api import cohort_api
from hyperunison_public_api_sdk.model.public_cohort_execute_query_request import PublicCohortExecuteQueryRequest
from hyperunison_public_api_sdk.model.response_to_ucdm_result_with_sql import ResponseToUCDMResultWithSql
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperunison_public_api_sdk.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with hyperunison_public_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohort_api.CohortApi(api_client)
    api_key = "apiKey_example" # str | Authorization by Api key
    public_cohort_execute_query_request = PublicCohortExecuteQueryRequest(
        yaml="yaml_example",
        skip_cache="skip_cache_example",
    ) # PublicCohortExecuteQueryRequest |  (optional)

    try:
        api_response = api_instance.public_cohort_execute_query(api_key, public_cohort_execute_query_request=public_cohort_execute_query_request)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling CohortApi->public_cohort_execute_query: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CohortApi* | [**public_cohort_execute_query**](docs/CohortApi.md#public_cohort_execute_query) | **POST** /api/public/cohort/biobank/execute-query | 
*PipelineApi* | [**get_multi_pipeline**](docs/PipelineApi.md#get_multi_pipeline) | **GET** /api/public/pipeline/{id} | 
*PipelineApi* | [**run_custom_workflow**](docs/PipelineApi.md#run_custom_workflow) | **POST** /api/public/pipeline/workflow/run/{pipelineVersionId}/ | 
*StructureApi* | [**bulk_update_structure**](docs/StructureApi.md#bulk_update_structure) | **POST** /api/public/structure/save | 
*StructureApi* | [**export_database**](docs/StructureApi.md#export_database) | **POST** /api/public/structure/biobanks/{biobankCode}/cdm-export | 
*StructureApi* | [**get_app_publicapi_structure_getbiobankstructuremappingstatus**](docs/StructureApi.md#get_app_publicapi_structure_getbiobankstructuremappingstatus) | **GET** /api/public/structure/{biobankCode}/status | 
*StructureApi* | [**get_job**](docs/StructureApi.md#get_job) | **GET** /api/public/structure/job/{jobId} | 
*SuggesterApi* | [**generate_suggests**](docs/SuggesterApi.md#generate_suggests) | **GET** /api/public/suggester/generate/{biobankCode} | 


## Documentation For Models

 - [BiobankOMOPExportResponse](docs/BiobankOMOPExportResponse.md)
 - [BulkUpdateStructureRequest](docs/BulkUpdateStructureRequest.md)
 - [DataItemDictionaryWithAccuracyListResponse](docs/DataItemDictionaryWithAccuracyListResponse.md)
 - [DataItemDictionaryWithAccuracyResponse](docs/DataItemDictionaryWithAccuracyResponse.md)
 - [Job](docs/Job.md)
 - [MultiRunPipeline](docs/MultiRunPipeline.md)
 - [NextflowPipelineOutputFormatterResult](docs/NextflowPipelineOutputFormatterResult.md)
 - [NextflowPipelineOutputFormatterResultItemStatus](docs/NextflowPipelineOutputFormatterResultItemStatus.md)
 - [PublicCohortExecuteQueryRequest](docs/PublicCohortExecuteQueryRequest.md)
 - [ResponseToUCDMResultWithSql](docs/ResponseToUCDMResultWithSql.md)
 - [RunCustomWorkflowRequest](docs/RunCustomWorkflowRequest.md)
 - [RunPipeline](docs/RunPipeline.md)
 - [RunnerAgent](docs/RunnerAgent.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in hyperunison_public_api_sdk.apis and hyperunison_public_api_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from hyperunison_public_api_sdk.api.default_api import DefaultApi`
- `from hyperunison_public_api_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import hyperunison_public_api_sdk
from hyperunison_public_api_sdk.apis import *
from hyperunison_public_api_sdk.models import *
```

