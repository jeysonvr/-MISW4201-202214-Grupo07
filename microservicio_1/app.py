from flask_restful import Api
from flask import Flask
from azure.storage.queue import (
        QueueClient
)

from .modelos import db, LogEnviados
import os , datetime


app = Flask('default')  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ABC_enviados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# Retrieve the connection string from an environment
# variable named AZURE_STORAGE_CONNECTION_STRING
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Create a unique name for the queue
q_name = "queue-5101bead-8473-406a-95b4-76aea1640c68"


# Instantiate a QueueClient object which will
# be used to create and manipulate the queue
print("Starting queue: " + q_name)
print(connect_str)
queue_client = QueueClient.from_connection_string(connect_str, q_name)

# Insert Message
message = u"Alarm message"
print("Adding message: " + message)
blockNumber = 4
for index in range(1,50):
    mensaje_enviado = queue_client.send_message(message + str(index))
    mensaje_log = LogEnviados(date_send = datetime.datetime.now(),message_id = mensaje_enviado.id,message_content = mensaje_enviado.content, is_processed = False, block_number = blockNumber)
    db.session.add(mensaje_log)
    db.session.commit()

    


