from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

api_key = 'X5Xqu9AtnIimfI2WyRCWFF4rTiN299GbzOgJ4k00xvNQSUwIc4kKlxhXiM4qp5qn'
pipeline_id = '62'
api = UnisonSDKApi(
    Configuration(
        host='http://localhost:8082',
    )
)
response = api.get_multi_pipeline(
    api_key,
    pipeline_id
)
print(response)