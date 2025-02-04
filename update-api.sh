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

./correct-imports.sh
