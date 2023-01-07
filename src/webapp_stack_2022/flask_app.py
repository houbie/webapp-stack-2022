import os
from pathlib import Path

import serverless_wsgi
from aws_lambda_powertools.logging import Logger

from webapp_stack_2022.common.application_factory import create_app

OPEN_API_DIR = os.environ.get("LAMBDA_TASK_ROOT", Path(__file__).parents[2])

logger = Logger()

app = create_app(
    __name__,
    "openApi.yaml",
    specification_dir=OPEN_API_DIR,
    base_path=f'/{os.environ.get("API_BASEPATH", "api")}',
).app


def handler(event, context):
    logger.debug("Delegating %s to flask app", event["path"])
    return serverless_wsgi.handle_request(app, event, context)
