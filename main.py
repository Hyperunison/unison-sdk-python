from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

try:
    import pydevd_pycharm

    pydevd_pycharm.settrace('host.docker.internal', port=55147, stdoutToServer=True, stderrToServer=True)
except:
    pass

# Init variables
query = 'CDM: ovision/OMOP:5.4\nSELECT:\n  - gender\n  - race\n  - year_of_birth\n\nFROM: [ATLAS1]\n\nLIMIT: 500\n'
api_key = 'HpipYth6ARM7G7ipR9iJJHXw8RY5xeG9EBsFKX2fIQREnNgzj63rdahFuYCMKjWN'
biobank_id = '1'
api = UnisonSDKApi(
    Configuration(
        host='http://host.docker.internal:8082',
    )
)

# Execute Cohort request
response = api.execute_cohort_request(
    api_key,
    biobank_id,
    query
)
print(response)

# Get multi pipeline
response = api.get_multi_pipeline(
    api_key=api_key,
    id='0'
)
print(response)

# Run custom workflow
api.run_custom_workflow(
    api_key=api_key,
    pipeline_version_id='0',
    parameters=list([]),
    project='',
    biobanks=list([]),
    cohort=''
)