from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

api_key = 'X5Xqu9AtnIimfI2WyRCWFF4rTiN299GbzOgJ4k00xvNQSUwIc4kKlxhXiM4qp5qn'
code = 'ALERG2'
cdm = 'demo/OMOP:5.4'
limit = '100'
api = UnisonSDKApi(
    Configuration(
        host='http://localhost:8082',
    )
)
response = api.export_cdm(
    api_key,
    code=code,
    cdm=cdm,
    limit=limit,
    connection_string = '',
    cdm_tables = ["person"]
)
print(response)