import os
from pathlib import Path

import pytest

from tests.dynamodb_local import prepare_dynamodb_local
from webapp_stack_2022.flask_app import app

os.environ["AWS_REGION"] = "eu-west-1"

prepare_dynamodb_local(Path(__file__).parent.joinpath("../.dynamodb"))


@pytest.fixture
def load_csv():
    def load(file: str) -> object:
        csv_file = Path(__file__).with_name("data").joinpath(file)
        return open(csv_file, "rb")

    return load


@pytest.fixture
def flask_client():
    with app.test_client() as client:
        yield client
