set -e

cp ./templates/UnisonSDKApi.template ./src/hyperunison_public_api/UnisonSDKApi.py
cp ./templates/__init__.template ./src/hyperunison_public_api/__init__.py

sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api/cohort_api.py
sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api/pipeline_api.py
sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api/structure_api.py
sed -i 's/from hyperunison_public_api_sdk./from ../g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api/suggester_api.py
sed -i 's/from hyperunison_public_api_sdk.exceptions import/from .exceptions import/g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/rest.py
sed -i 's/from hyperunison_public_api_sdk.exceptions import/from .exceptions import/g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/configuration.py
sed -i 's/from hyperunison_public_api_sdk import rest/from . import rest/g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api_client.py
sed -i 's/from hyperunison_public_api_sdk./from ./g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/api_client.py

for file in ./src/hyperunison_public_api/hyperunison_public_api_sdk/model/*; do
    if [ -f "$file" ] && [ "$(basename "$file")" != "__init__.py" ]; then
        sed -i 's/from hyperunison_public_api_sdk./from ../g' "$file"
        echo "$file content changed"
    fi
done

sed -i 's/from hyperunison_public_api_sdk./from ./g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/model_utils.py
sed -i 's/from hyperunison_public_api_sdk./from ./g' ./src/hyperunison_public_api/hyperunison_public_api_sdk/__init__.py