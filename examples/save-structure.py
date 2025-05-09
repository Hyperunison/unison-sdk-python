from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

api_key = 'X5Xqu9AtnIimfI2WyRCWFF4rTiN299GbzOgJ4k00xvNQSUwIc4kKlxhXiM4qp5qn'
yaml = ''
api = UnisonSDKApi(
    Configuration(
        host='http://localhost:8082',
    )
)
response = api.save_structure(
    api_key,
    yaml=yaml
)
print(response)