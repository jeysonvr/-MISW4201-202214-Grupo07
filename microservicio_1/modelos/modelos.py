from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

// Información de los mensajes enviados
class LogEnviados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_send = db.Column(db.String(128))
    date_processed = db.Column(db.String(128))
    message_id = db.Column(db.String(200))
    message_content = db.Column(db.String(2000))
    is_processed = db.Column(db.Boolean)
    block_number = db.Column(db.Numeric(500))
    

