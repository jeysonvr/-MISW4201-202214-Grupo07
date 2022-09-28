import logging, datetime
from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from modelos import db, Usuario


import logging
from flask import Flask

app = Flask(__name__)
activo = None

class VistaAutorizador:

    def __init__(self):
        self.activo = True

    def autenticacionUsuario(usuario, contrasena):
        usuario = db.session.query(Usuario.id, Usuario.usuario).filter(Usuario.usuario == usuario, 
            Usuario.contrasena == contrasena).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == request.json["contrasena"]).first()
            db.session.commit()
            return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso}