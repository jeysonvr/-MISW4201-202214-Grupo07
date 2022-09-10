from flaskr import create_app
from flask_restful import Api
from azure.storage.queue import (
        QueueClient
)

import os, uuid

app = create_app('default')
app_context = app.app_context()
app_context.push()

# Retrieve the connection string from an environment
# variable named AZURE_STORAGE_CONNECTION_STRING
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Create a unique name for the queue
q_name = "queue-" + str(uuid.uuid4())

# Instantiate a QueueClient object which will
# be used to create and manipulate the queue
print("Creating queue: " + q_name)
queue_client = QueueClient.from_connection_string(connect_str, q_name)

# Create the queue
queue_client.create_queue()