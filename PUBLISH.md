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