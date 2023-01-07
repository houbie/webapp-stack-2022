from pathlib import Path

from mirakuru import TCPExecutor
from port_for import get_port

from webapp_stack_2022.flask_app import app

path_dynamodb_jar = Path(__file__).parents[1].joinpath(".dynamodb/DynamoDBLocal.jar")
port = get_port(None)
dynamo_url = f"http://localhost:{port}"

dynamodb_executor = TCPExecutor(
    f"""java
        -Djava.library.path=./DynamoDBLocal_lib
        -jar {path_dynamodb_jar}
        -inMemory
        -port {port}""",
    host="localhost",
    port=port,
    timeout=60,
)

# dynamodb_executor.start()
# CountryHolidays.Meta.host = dynamo_url
# CountryHolidays.create_table(read_capacity_units=100, write_capacity_units=100, wait=True)

print("starting flask")
app.run(port=8080, debug=True)

print("stopping local dynamo")
dynamodb_executor.stop()
