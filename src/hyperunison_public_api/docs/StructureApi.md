# hyperunison_public_api_sdk.StructureApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_structure**](StructureApi.md#bulk_update_structure) | **POST** /api/public/structure/save | 
[**export_database**](StructureApi.md#export_database) | **POST** /api/public/structure/biobanks/{biobankCode}/cdm-export | 
[**get_app_publicapi_structure_getbiobankstructuremappingstatus**](StructureApi.md#get_app_publicapi_structure_getbiobankstructuremappingstatus) | **GET** /api/public/structure/{code}/status | 
[**post_app_publicapi_structure_getexportjobstatus**](StructureApi.md#post_app_publicapi_structure_getexportjobstatus) | **POST** /api/public/structure/job/{jobId} | 


# **bulk_update_structure**
> DataItemDictionaryWithAccuracyListResponse bulk_update_structure()



### Example


```python
import time
import hyperunison_public_api_sdk
from hyperunison_public_api_sdk.api import structure_api
from hyperunison_public_api_sdk.model.data_item_dictionary_with_accuracy_list_response import DataItemDictionaryWithAccuracyListResponse
from hyperunison_public_api_sdk.model.bulk_update_structure_request import BulkUpdateStructureRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperunison_public_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with hyperunison_public_api_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = structure_api.StructureApi(api_client)
    api_key = "apiKey_example" # str | Authorization by Api key (optional)
    bulk_update_structure_request = BulkUpdateStructureRequest(
        yaml="yaml_example",
    ) # BulkUpdateStructureRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.bulk_update_structure(api_key=api_key, bulk_update_structure_request=bulk_update_structure_request)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling StructureApi->bulk_update_structure: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Authorization by Api key | [optional]
 **bulk_update_structure_request** | [**BulkUpdateStructureRequest**](BulkUpdateStructureRequest.md)|  | [optional]

### Return type

[**DataItemDictionaryWithAccuracyListResponse**](DataItemDictionaryWithAccuracyListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generate suggestion response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_database**
> BiobankOMOPExportResponse export_database(biobank_code)



### Example


```python
import time
import hyperunison_public_api_sdk
from hyperunison_public_api_sdk.api import structure_api
from hyperunison_public_api_sdk.model.biobank_omop_export_response import BiobankOMOPExportResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperunison_public_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with hyperunison_public_api_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = structure_api.StructureApi(api_client)
    biobank_code = "H" # str | 
    api_key = "apiKey_example" # str | Authorization by Api key (optional)
    cdm = "demo/OMOP:5.4" # str | CDM ID. Format: vendor/name:version. By Default: demo/OMOP:5.4 (OMOP 5.4) (optional) if omitted the server will use the default value of "demo/OMOP:5.4"
    limit = "" # str | Optional. Max count items in the export files, for each file. Use it for debug only (optional) if omitted the server will use the default value of ""
    cdm_tables = [] # [bool, date, datetime, dict, float, int, list, str, none_type] | Optional. An array of cdm tables to limit export. For example: ['person', 'procedure'] (optional) if omitted the server will use the default value of []
    format = "csv" # str | Format of the export. Available values: csv, postgresql, sqlite (optional) if omitted the server will use the default value of "csv"
    connection_string = "sqlite://qXzyC@Swg0_bs9ZayIMrKdgNvb6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz.5awxoFZxHzs6ED.kjUSnTINkY/snYv3_8jSQL653YHp9_ohS9pb0ziLqFde9fYgAwdpfxa30zS?7-'(u+-7Tfp&\`F+7-?{%@=iEPLVY*a@A[b_6cfy~~0GcD_@b4Y=U?otJ(e#=I@b(lK%|5-Ido" # str | For PostgreSQL formats only. Format: dbType://username:password@hostname:port/dbName (optional)
    run_dqd = "" # str | Check name to run. Default if none. Possible values: OMOP-5.4 (optional) if omitted the server will use the default value of ""

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.export_database(biobank_code)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling StructureApi->export_database: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.export_database(biobank_code, api_key=api_key, cdm=cdm, limit=limit, cdm_tables=cdm_tables, format=format, connection_string=connection_string, run_dqd=run_dqd)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling StructureApi->export_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biobank_code** | **str**|  |
 **api_key** | **str**| Authorization by Api key | [optional]
 **cdm** | **str**| CDM ID. Format: vendor/name:version. By Default: demo/OMOP:5.4 (OMOP 5.4) | [optional] if omitted the server will use the default value of "demo/OMOP:5.4"
 **limit** | **str**| Optional. Max count items in the export files, for each file. Use it for debug only | [optional] if omitted the server will use the default value of ""
 **cdm_tables** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| Optional. An array of cdm tables to limit export. For example: [&#39;person&#39;, &#39;procedure&#39;] | [optional] if omitted the server will use the default value of []
 **format** | **str**| Format of the export. Available values: csv, postgresql, sqlite | [optional] if omitted the server will use the default value of "csv"
 **connection_string** | **str**| For PostgreSQL formats only. Format: dbType://username:password@hostname:port/dbName | [optional]
 **run_dqd** | **str**| Check name to run. Default if none. Possible values: OMOP-5.4 | [optional] if omitted the server will use the default value of ""

### Return type

[**BiobankOMOPExportResponse**](BiobankOMOPExportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create pipelines to export OMOP database for specific biobanks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_publicapi_structure_getbiobankstructuremappingstatus**
> DataItemDictionaryWithAccuracyListResponse get_app_publicapi_structure_getbiobankstructuremappingstatus(code)



### Example


```python
import time
import hyperunison_public_api_sdk
from hyperunison_public_api_sdk.api import structure_api
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
    api_instance = structure_api.StructureApi(api_client)
    code = "code_example" # str | 
    api_key = "apiKey_example" # str | Authorization by Api key (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app_publicapi_structure_getbiobankstructuremappingstatus(code)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling StructureApi->get_app_publicapi_structure_getbiobankstructuremappingstatus: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_app_publicapi_structure_getbiobankstructuremappingstatus(code, api_key=api_key)
        pprint(api_response)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling StructureApi->get_app_publicapi_structure_getbiobankstructuremappingstatus: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  |
 **api_key** | **str**| Authorization by Api key | [optional]

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
**200** | Status by biobank code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_app_publicapi_structure_getexportjobstatus**
> post_app_publicapi_structure_getexportjobstatus(job_id)



### Example


```python
import time
import hyperunison_public_api_sdk
from hyperunison_public_api_sdk.api import structure_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperunison_public_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with hyperunison_public_api_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = structure_api.StructureApi(api_client)
    job_id = "4" # str | 
    api_key = "apiKey_example" # str | Authorization by Api key (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_app_publicapi_structure_getexportjobstatus(job_id)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling StructureApi->post_app_publicapi_structure_getexportjobstatus: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.post_app_publicapi_structure_getexportjobstatus(job_id, api_key=api_key)
    except hyperunison_public_api_sdk.ApiException as e:
        print("Exception when calling StructureApi->post_app_publicapi_structure_getexportjobstatus: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  |
 **api_key** | **str**| Authorization by Api key | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

