import os
import tarfile
from types import SimpleNamespace

import pytest
import requests
from pytest_dynamodb import factories, plugin

os.environ["AWS_REGION"] = "eu-west-1"


def download_dynamodb_local(target_dir):
    url = "https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz"
    local_filename = url.split("/", maxsplit=1)[0]
    with requests.get(url, stream=True) as resp:
        with open(local_filename, "wb") as file:
            for chunk in resp.iter_content(chunk_size=8192):
                file.write(chunk)
    with tarfile.open(local_filename, "r:gz") as tar:
        tar.extractall(path=target_dir)
    os.remove(local_filename)
    print(f"downloaded local dynamodb to {target_dir}")


def prepare_dynamodb_local(download_dir) -> None:
    if not os.path.exists(f"{download_dir}/DynamoDBLocal.jar"):
        download_dynamodb_local(download_dir)

    if os.environ.get("CUSTOM_DYNAMODB_PORT"):

        @pytest.fixture(scope="session")
        def external_dynamodb_proc_fixture():
            return SimpleNamespace(host="localhost", port=os.environ.get("CUSTOM_DYNAMODB_PORT", "9999"))

        plugin.dynamodb_proc = external_dynamodb_proc_fixture
    else:
        plugin.dynamodb_proc = factories.dynamodb_proc(download_dir)
