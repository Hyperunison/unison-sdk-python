from auto_api_client.api.public_api_api import PublicAPIApi
from auto_api_client.model.public_cohort_execute_query_request import PublicCohortExecuteQueryRequest

from src.auto.auto_api_client.api_client import ApiClient


class UnisonSDKApi:

    def __init__(self, configuration):
        self.api_instance = PublicAPIApi(
            ApiClient(
                configuration = configuration
            )
        )

    def execute_cohort_request(self, api_key, biobank_id, yaml):
        return self.api_instance.public_cohort_execute_query(
            api_key = api_key,
            biobank_id = biobank_id,
            public_cohort_execute_query_request=PublicCohortExecuteQueryRequest(
                yaml=yaml
            )
        )