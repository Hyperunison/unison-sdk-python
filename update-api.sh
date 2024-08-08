set -e

rm -rf src/hyperunison_public_api/
mkdir src/hyperunison_public_api/

curl -s https://dev-api.hyperunison.com/api/public/doc.json > src/hyperunison_public_api/api.json

docker run --rm -v "${PWD}/src/hyperunison_public_api/:/local" \
  openapitools/openapi-generator-cli:v6.6.0 generate \
  -i /local/api.json \
  -g python-prior \
  -o /local/ \
  -p packageName=hyperunison_public_api_sdk

cp ./templates/UnisonSDKApi.template ./src/hyperunison_public_api/UnisonSDKApi.py
cp ./templates/__init__.template ./src/hyperunison_public_api/__init__.py

sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api/public_api_api.py
sed -i 's/from hyperunison_public_api_sdk.exceptions import/from .exceptions import/g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/rest.py
sed -i 's/from hyperunison_public_api_sdk.exceptions import/from .exceptions import/g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/configuration.py
sed -i 's/from hyperunison_public_api_sdk import rest/from . import rest/g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api_client.py
sed -i 's/from hyperunison_public_api_sdk./from ./g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api_client.py

sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/model/public_cohort_execute_query_request.py
sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/model/response_to_ucdm_result_with_sql.py
sed -i 's/from hyperunison_public_api_sdk./from ./g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/model_utils.py
sed -i 's/from hyperunison_public_api_sdk./from ./g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/__init__.py

#docker-compose exec -ti unison-agent pip install -r requirements.txt
