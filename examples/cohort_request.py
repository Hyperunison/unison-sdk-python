from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

try:
    import pydevd_pycharm

    pydevd_pycharm.settrace('host.docker.internal', port=55147, stdoutToServer=True, stderrToServer=True)
except:
    pass

query = 'CDM: ovision/OMOP:5.4\nSELECT:\n  - gender\n  - race\n  - year_of_birth\n\nFROM: [ATLAS1]\n\nLIMIT: 500\n'
api_key = 'X5Xqu9AtnIimfI2WyRCWFF4rTiN299GbzOgJ4k00xvNQSUwIc4kKlxhXiM4qp5qn'
api = UnisonSDKApi(
    Configuration(
        host='http://host.docker.internal:8082',
    )
)

# Execute Cohort request
response = api.execute_cohort_request(
    api_key,
    query
)
print(response)