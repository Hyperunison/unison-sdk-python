import os
import sys
import shutil
import tarfile
import zipfile
import tempfile


def fix_metadata_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        lower = line.lower()
        if (
            lower.startswith("license-expression:") or
            lower.startswith("license-file:") or
            lower.startswith("license:") or
            (lower.startswith("dynamic:") and "license" in lower)
        ):
            continue
        cleaned_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)


def fix_wheel(file_path):
    with tempfile.TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdir)

        # Find and fix METADATA
        for root, dirs, files in os.walk(tmpdir):
            if 'METADATA' in files:
                fix_metadata_file(os.path.join(root, 'METADATA'))

        # Overwrite original file
        with zipfile.ZipFile(file_path, 'w') as zip_out:
            for foldername, subfolders, filenames in os.walk(tmpdir):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    arcname = os.path.relpath(filepath, tmpdir)
                    zip_out.write(filepath, arcname)

        print(f"Fixed in-place: {file_path}")


def fix_tar_gz(file_path):
    with tempfile.TemporaryDirectory() as tmpdir:
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(tmpdir)

        # Find and fix PKG-INFO
        for root, dirs, files in os.walk(tmpdir):
            if 'PKG-INFO' in files:
                fix_metadata_file(os.path.join(root, 'PKG-INFO'))

        # Overwrite original file
        with tarfile.open(file_path, 'w:gz') as tar_out:
            for foldername, subfolders, filenames in os.walk(tmpdir):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    arcname = os.path.relpath(filepath, tmpdir)
                    tar_out.add(filepath, arcname)

        print(f"Fixed in-place: {file_path}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python fix_package_metadata.py <path-to-whl-or-tar.gz>")
        sys.exit(1)

    package_path = sys.argv[1]
    if package_path.endswith('.whl'):
        fix_wheel(package_path)
    elif package_path.endswith('.tar.gz'):
        fix_tar_gz(package_path)
    else:
        print("Unsupported file type. Must be .whl or .tar.gz")
        sys.exit(1)


if __name__ == '__main__':
    main()
