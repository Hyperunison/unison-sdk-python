# Hyperunison Python SDK

You can use this SDK to execute UQL queries via Public API.

## Installation
If you need to install this SDK, you should add the line
```shell
hyperunison-public-api-sdk===1.1.8
```
to the file **requirements.txt**.

Or you can run the command
```shell
pip install hyperunison-public-api-sdk
```
in CLI.

## API keys

You will need to create API key to use the Public API. You can do it in Web interface of the site.

## The example of using

```python
from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

# Init variables
query = ''
api_key = ''
biobank_id = '1'
api = UnisonSDKApi(
    Configuration(
        host='',
    )
)

# Execute Cohort request
response = api.execute_cohort_request(
    api_key,
    biobank_id,
    query
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
```