# Publish package to repository

## Download JSON file with docs in Swagger format

## Build API classes
```shell
    docker run --rm -v "${PWD}/src/hyperunison_public_api/:/local" \
      openapitools/openapi-generator-cli:v6.6.0 generate \
      -i /local/api.json \
      -g python-prior \
      -o /local/ \
      -p packageName=hyperunison_public_api_sdk
```

## Change version of package
This version is in file **pyproject.toml**.

## Build package
```shell
    rm -rf dist
    python3 -m build
```

## Send package to test repository
```shell
    python3 -m twine upload --repository testpypi dist/*
```

## Send package to production repository
```shell
    python3 -m twine upload --repository pypi dist/*
```

## Install Package from Test PyPI
```shell
    python3 -m pip install --index-url https://test.pypi.org/simple/ hyperunison_public_api_sdk
```

## Install Package from PyPI
```shell
    python3 -m pip install hyperunison_public_api_sdk
```