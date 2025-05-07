#!/bin/bash

set -e

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 [pypi|testpypi]"
    exit 1
fi

REPO_NAME="$1"

if [[ "$REPO_NAME" != "pypi" && "$REPO_NAME" != "testpypi" ]]; then
    echo "Error: argument must be 'pypi' or 'testpypi'"
    exit 1
fi

./correct-imports.sh

# Step 1: Clean up old builds
rm -rf ./build ./dist ./*.egg-info

# Step 2: Build the package
python3 -m build

# Step 3: Fix the metadata in the built files
for file in dist/*.whl dist/*.tar.gz; do
  echo "Fixing metadata in $file..."
  python3 fix-metadata.py "$file"
done

# Step 4: Checking built distributions
echo "Checking built distributions..."
twine check dist/*

repo_name="$1"
python3 -m twine upload --verbose --repository "$repo_name" dist/*