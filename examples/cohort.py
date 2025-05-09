from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

query = 'CDM: demo/OMOP:5.4\n'
query += 'SELECT:\n'
query += ' - gender\n'
query += ' - race\n'
query += ' - year_of_birth\n\n'
query += 'FROM: [ALERG2]\n\n'
query += 'LIMIT: 500\n'
api_key = 'X5Xqu9AtnIimfI2WyRCWFF4rTiN299GbzOgJ4k00xvNQSUwIc4kKlxhXiM4qp5qn'
api = UnisonSDKApi(
    Configuration(
        host='http://localhost:8082',
    )
)
response = api.execute_cohort_request(
    api_key,
    query
)
print(response)