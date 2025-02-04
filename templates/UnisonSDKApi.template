from typing import List

from .hyperunison_public_api_sdk.api.cohort_api import CohortApi
from .hyperunison_public_api_sdk.api.pipeline_api import PipelineApi
from .hyperunison_public_api_sdk.model.public_cohort_execute_query_request import PublicCohortExecuteQueryRequest
from hyperunison_public_api_sdk.model.run_custom_workflow_request import RunCustomWorkflowRequest

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

    def execute_cohort_request(
            self,
            api_key: str,
            biobank_id: str,
            yaml: str
    ):
        return self.cohort_api_instance.public_cohort_execute_query(
            api_key = api_key,
            biobank_id = biobank_id,
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