from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

api_key = 'X5Xqu9AtnIimfI2WyRCWFF4rTiN299GbzOgJ4k00xvNQSUwIc4kKlxhXiM4qp5qn'
job_id = '52654'
api = UnisonSDKApi(
    Configuration(
        host='http://localhost:8082',
    )
)
response = api.get_job_status(
    api_key,
    job_id
)
print(response)