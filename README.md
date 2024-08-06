# Hyperunison Python SDK

You can use this SDK to execute UQL queries via Public API.

## API keys

You will need to create API key to use the Public API. You can do it in Web interface of the site.

## The example of using

```python
from src.UnisonSDKApi import UnisonSDKApi
from src.auto.auto_api_client.configuration import Configuration
    
query = ''
api_key = ''
biobank_id = 1
api = UnisonSDKApi(
    Configuration(
        host='',
    )
)
response = api.execute_cohort_request(
    api_key,
    biobank_id,
    query
)
print(response)
```