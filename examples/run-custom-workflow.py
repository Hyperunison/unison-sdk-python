from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

api_key = 'X5Xqu9AtnIimfI2WyRCWFF4rTiN299GbzOgJ4k00xvNQSUwIc4kKlxhXiM4qp5qn'
pipeline_version_id = '1'
api = UnisonSDKApi(
    Configuration(
        host='http://localhost:8082',
    )
)
response = api.run_custom_workflow(
    api_key,
    pipeline_version_id=pipeline_version_id,
    parameters=[],
    project='',
    biobanks = [],
    cohort='',
)
print(response)