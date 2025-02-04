set -e

cp ./templates/UnisonSDKApi.template ./src/hyperunison_public_api/UnisonSDKApi.py
cp ./templates/__init__.template ./src/hyperunison_public_api/__init__.py

sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api/cohort_api.py
sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api/pipeline_api.py
sed -i 's/from hyperunison_public_api_sdk.exceptions import/from .exceptions import/g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/rest.py
sed -i 's/from hyperunison_public_api_sdk.exceptions import/from .exceptions import/g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/configuration.py
sed -i 's/from hyperunison_public_api_sdk import rest/from . import rest/g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api_client.py
sed -i 's/from hyperunison_public_api_sdk./from ./g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api_client.py

sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/model/public_cohort_execute_query_request.py
sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/model/run_custom_workflow_request.py
sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/model/response_to_ucdm_result_with_sql.py
sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/model/multi_run_pipeline.py
sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/model/run_pipeline.py
sed -i 's/from hyperunison_public_api_sdk./from ./g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/model_utils.py
sed -i 's/from hyperunison_public_api_sdk./from ./g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/__init__.py