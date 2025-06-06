"""
    Unison public API

    API for Python and R libraries  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ..api_client import ApiClient, Endpoint as _Endpoint
from ..model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ..model.biobank_omop_export_response import BiobankOMOPExportResponse
from ..model.bulk_update_structure_request import BulkUpdateStructureRequest
from ..model.data_item_dictionary_with_accuracy_list_response import DataItemDictionaryWithAccuracyListResponse
from ..model.job import Job


class StructureApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.bulk_update_structure_endpoint = _Endpoint(
            settings={
                'response_type': (DataItemDictionaryWithAccuracyListResponse,),
                'auth': [],
                'endpoint_path': '/api/public/structure/save',
                'operation_id': 'bulk_update_structure',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_key',
                    'bulk_update_structure_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'api_key':
                        (str,),
                    'bulk_update_structure_request':
                        (BulkUpdateStructureRequest,),
                },
                'attribute_map': {
                    'api_key': 'apiKey',
                },
                'location_map': {
                    'api_key': 'header',
                    'bulk_update_structure_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.export_database_endpoint = _Endpoint(
            settings={
                'response_type': (BiobankOMOPExportResponse,),
                'auth': [],
                'endpoint_path': '/api/public/structure/biobanks/{biobankCode}/cdm-export',
                'operation_id': 'export_database',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'biobank_code',
                    'api_key',
                    'cdm',
                    'limit',
                    'cdm_tables',
                    'format',
                    'connection_string',
                    'run_dqd',
                ],
                'required': [
                    'biobank_code',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'biobank_code',
                    'format',
                    'run_dqd',
                ]
            },
            root_map={
                'validations': {
                    ('biobank_code',): {

                        'regex': {
                            'pattern': r'\w+',  # noqa: E501
                        },
                    },
                    ('format',): {

                        'regex': {
                            'pattern': r'^(csv|postgresql|sqlite)$',  # noqa: E501
                        },
                    },
                    ('run_dqd',): {

                        'regex': {
                            'pattern': r'^(OMOP-5.4)?$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'biobank_code':
                        (str,),
                    'api_key':
                        (str,),
                    'cdm':
                        (str,),
                    'limit':
                        (str,),
                    'cdm_tables':
                        ([bool, date, datetime, dict, float, int, list, str, none_type],),
                    'format':
                        (str,),
                    'connection_string':
                        (str,),
                    'run_dqd':
                        (str,),
                },
                'attribute_map': {
                    'biobank_code': 'biobankCode',
                    'api_key': 'apiKey',
                    'cdm': 'cdm',
                    'limit': 'limit',
                    'cdm_tables': 'cdmTables[]',
                    'format': 'format',
                    'connection_string': 'connectionString',
                    'run_dqd': 'runDQD',
                },
                'location_map': {
                    'biobank_code': 'path',
                    'api_key': 'header',
                    'cdm': 'query',
                    'limit': 'query',
                    'cdm_tables': 'query',
                    'format': 'query',
                    'connection_string': 'query',
                    'run_dqd': 'query',
                },
                'collection_format_map': {
                    'cdm_tables': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_app_publicapi_structure_getbiobankstructuremappingstatus_endpoint = _Endpoint(
            settings={
                'response_type': (DataItemDictionaryWithAccuracyListResponse,),
                'auth': [],
                'endpoint_path': '/api/public/structure/{biobankCode}/status',
                'operation_id': 'get_app_publicapi_structure_getbiobankstructuremappingstatus',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'biobank_code',
                    'api_key',
                ],
                'required': [
                    'biobank_code',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'biobank_code':
                        (str,),
                    'api_key':
                        (str,),
                },
                'attribute_map': {
                    'biobank_code': 'biobankCode',
                    'api_key': 'apiKey',
                },
                'location_map': {
                    'biobank_code': 'path',
                    'api_key': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_job_endpoint = _Endpoint(
            settings={
                'response_type': (Job,),
                'auth': [],
                'endpoint_path': '/api/public/structure/job/{jobId}',
                'operation_id': 'get_job',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'job_id',
                    'api_key',
                ],
                'required': [
                    'job_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'job_id',
                ]
            },
            root_map={
                'validations': {
                    ('job_id',): {

                        'regex': {
                            'pattern': r'\d+',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'job_id':
                        (str,),
                    'api_key':
                        (str,),
                },
                'attribute_map': {
                    'job_id': 'jobId',
                    'api_key': 'apiKey',
                },
                'location_map': {
                    'job_id': 'path',
                    'api_key': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def bulk_update_structure(
        self,
        **kwargs
    ):
        """bulk_update_structure  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bulk_update_structure(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            api_key (str): Authorization by Api key. [optional]
            bulk_update_structure_request (BulkUpdateStructureRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DataItemDictionaryWithAccuracyListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.bulk_update_structure_endpoint.call_with_http_info(**kwargs)

    def export_database(
        self,
        biobank_code,
        **kwargs
    ):
        """export_database  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.export_database(biobank_code, async_req=True)
        >>> result = thread.get()

        Args:
            biobank_code (str):

        Keyword Args:
            api_key (str): Authorization by Api key. [optional]
            cdm (str): CDM ID. Format: vendor/name:version. By Default: demo/OMOP:5.4 (OMOP 5.4). [optional] if omitted the server will use the default value of "demo/OMOP:5.4"
            limit (str): Optional. Max count items in the export files, for each file. Use it for debug only. [optional] if omitted the server will use the default value of ""
            cdm_tables ([bool, date, datetime, dict, float, int, list, str, none_type]): Optional. An array of cdm tables to limit export. For example: ['person', 'procedure']. [optional] if omitted the server will use the default value of []
            format (str): Format of the export. Available values: csv, postgresql, sqlite. [optional] if omitted the server will use the default value of "csv"
            connection_string (str): For PostgreSQL formats only. Format: dbType://username:password@hostname:port/dbName. [optional]
            run_dqd (str): Check name to run. Default if none. Possible values: OMOP-5.4. [optional] if omitted the server will use the default value of ""
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            BiobankOMOPExportResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['biobank_code'] = \
            biobank_code
        return self.export_database_endpoint.call_with_http_info(**kwargs)

    def get_app_publicapi_structure_getbiobankstructuremappingstatus(
        self,
        biobank_code,
        **kwargs
    ):
        """get_app_publicapi_structure_getbiobankstructuremappingstatus  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_app_publicapi_structure_getbiobankstructuremappingstatus(biobank_code, async_req=True)
        >>> result = thread.get()

        Args:
            biobank_code (str):

        Keyword Args:
            api_key (str): Authorization by Api key. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DataItemDictionaryWithAccuracyListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['biobank_code'] = \
            biobank_code
        return self.get_app_publicapi_structure_getbiobankstructuremappingstatus_endpoint.call_with_http_info(**kwargs)

    def get_job(
        self,
        job_id,
        **kwargs
    ):
        """get_job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_job(job_id, async_req=True)
        >>> result = thread.get()

        Args:
            job_id (str):

        Keyword Args:
            api_key (str): Authorization by Api key. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Job
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['job_id'] = \
            job_id
        return self.get_job_endpoint.call_with_http_info(**kwargs)

