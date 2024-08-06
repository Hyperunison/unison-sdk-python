# Hyperunison Python SDK

You can use this SDK to execute 

## Example

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