from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

try:
    import pydevd_pycharm

    pydevd_pycharm.settrace('host.docker.internal', port=55147, stdoutToServer=True, stderrToServer=True)
except:
    pass

api_key = 'X5Xqu9AtnIimfI2WyRCWFF4rTiN299GbzOgJ4k00xvNQSUwIc4kKlxhXiM4qp5qn'
api = UnisonSDKApi(
    Configuration(
        host='http://host.docker.internal:8082',
    )
)

# Get multi pipeline
response = api.get_multi_pipeline(
    api_key=api_key,
    id='1'
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