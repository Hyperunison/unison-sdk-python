from typing import List

from .hyperunison_public_api_sdk.api.cohort_api import CohortApi
from .hyperunison_public_api_sdk.api.pipeline_api import PipelineApi
from .hyperunison_public_api_sdk.api.suggester_api import SuggesterApi
from .hyperunison_public_api_sdk.api.structure_api import StructureApi
from .hyperunison_public_api_sdk.model.public_cohort_execute_query_request import PublicCohortExecuteQueryRequest
from .hyperunison_public_api_sdk.model.bulk_update_structure_request import BulkUpdateStructureRequest
from .hyperunison_public_api_sdk.model.run_custom_workflow_request import RunCustomWorkflowRequest

from .hyperunison_public_api_sdk.api_client import ApiClient


class UnisonSDKApi:

    def __init__(self, configuration):
        self.cohort_api_instance = CohortApi(
            ApiClient(
                configuration = configuration
            )
        )
        self.pipeline_api_instance = PipelineApi(
            ApiClient(
                configuration=configuration
            )
        )
        self.suggester_api_instance = SuggesterApi(
            ApiClient(
                configuration=configuration
            )
        )
        self.structure_api_instance = StructureApi(
            ApiClient(
                configuration=configuration
            )
        )

    def execute_cohort_request(
            self,
            api_key: str,
            yaml: str
    ):
        return self.cohort_api_instance.public_cohort_execute_query(
            api_key = api_key,
            public_cohort_execute_query_request=PublicCohortExecuteQueryRequest(
                yaml=yaml
            )
        )

    def get_multi_pipeline(
            self,
            api_key: str,
            id: str
    ):
        return self.pipeline_api_instance.get_multi_pipeline(
            api_key = api_key,
            id=id
        )

    def run_custom_workflow(
            self,
            api_key: str,
            pipeline_version_id: str,
            parameters: List[str],
            project: str,
            biobanks: List[str],
            cohort: str
    ):
        return self.pipeline_api_instance.run_custom_workflow(
            api_key=api_key,
            pipeline_version_id=pipeline_version_id,
            run_custom_workflow_request=RunCustomWorkflowRequest(
                parameters=parameters,
                project=project,
                biobanks=biobanks,
                cohort=cohort
            )
        )

    def save_structure(
            self,
            api_key: str,
            yaml: str
    ):
        return self.structure_api_instance.save_structure(
            api_key=api_key,
            bulk_update_structure_request=BulkUpdateStructureRequest(
                yaml=yaml
            )
        )

    def get_biobank_structure_mapping_status(
            self,
            api_key: str,
            code: str
    ):
        return self.structure_api_instance.get_app_publicapi_structure_getbiobankstructuremappingstatus(
            api_key=api_key,
            biobank_code=code
        )

    def export_cdm(
            self,
            api_key: str,
            code: str,
            cdm: str = '',
            limit: str = '',
            cdm_tables: List[str] = None,
            format: str = 'csv',
            connection_string: str = '',
            run_dqd: str = ''
    ):
        return self.structure_api_instance.export_database(
            api_key = api_key,
            biobank_code = code,
            cdm = cdm,
            limit = limit,
            cdm_tables = cdm_tables,
            format = format,
            connection_string = connection_string,
            run_dqd = run_dqd
        )

    def get_job_status(
            self,
            api_key: str,
            job_id: str
    ):
        return self.structure_api_instance.get_job(
            api_key=api_key,
            job_id=job_id
        )

    def suggester_generate(
            self,
            api_key: str,
            code: str,
            domain: str = '',
            vocabulary: str = '',
            only_standard_concept: str = '1',
            min_accuracy_to_run_gpt: str = ''
    ):
        return self.suggester_api_instance.generate(
            api_key=api_key,
            code=code,
            domain=domain,
            vocabulary=vocabulary,
            only_standard_concept=only_standard_concept,
            min_accuracy_to_run_gpt=min_accuracy_to_run_gpt
        )