from flaskr import create_app
from flask_restful import Api
from flask import Flask
from azure.storage.queue import (
        QueueClient
)

from .modelos import db, LogProcesados
import os , datetime

app = Flask('default')  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ABC_procesados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# Retrieve the connection string from an environment
# variable named AZURE_STORAGE_CONNECTION_STRING
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Name queue
q_name = "queue-5101bead-8473-406a-95b4-76aea1640c68"


# Instantiate a QueueClient object which will
# be used to manipulate the queue
print("Getting queue: " + q_name)
print(connect_str)
queue_client = QueueClient.from_connection_string(connect_str, q_name)


# Deleting Message
properties = queue_client.get_queue_properties()
count = properties.approximate_message_count
print("Message init count: " + str(count))
blockNumber = 4
while True:
    messages = queue_client.receive_messages()
    for message in messages:
        mensaje_log = LogProcesados(date_processed = datetime.datetime.now(),message_id = message.id,message_content = message.content, is_processed = False, block_number = blockNumber)
        db.session.add(mensaje_log)
        db.session.commit()
        queue_client.delete_message(message.id, message.pop_receipt)
    properties = queue_client.get_queue_properties()
    count = properties.approximate_message_count
    print("Message count: " + str(count))

