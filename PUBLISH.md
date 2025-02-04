# Publish package to repository

## Change version of package
This version is in file **pyproject.toml**.

## Build package
```shell
    rm -rf dist
    python3 -m build
```

## Send package to repository
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