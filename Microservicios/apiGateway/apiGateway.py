import logging, datetime
from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from modelos import db, Usuario, LogMicroServicios
from autorizador import VistaAutorizador 
from gestionInformacion import VistaGestionInformacion


import logging
from flask import Flask

app = Flask(__name__)

def autenticacionUsuario(usuario, contrasena):
    usuarioExistente = db.session.query(Usuario.id, Usuario.usuario).filter(Usuario.usuario == usuario, 
        Usuario.contrasena == contrasena).first()
    db.session.commit()
    if usuarioExistente is None:
        return None
    return usuarioExistente

class VistaLogIn(Resource):

    def post(self):
        nuevo_log = LogMicroServicios(fecha = datetime.datetime.now(), mensaje = "Ingreso a autenticación por usuario: " + request.json["usuario"] , microservicio = "Api Gateway")
        db.session.add(nuevo_log)
        autenticacion = VistaAutorizador.autenticacionUsuario(request.json["usuario"],request.json["contrasena"])
        if (autenticacion == 404):
            db.session.commit()
            return "El usuario no existe", autenticacion
        autorizador = VistaAutorizador.autorizarUsuario(autenticacion["token"]) # Cambiar metodo para que reciba el token y se valide
        if (autorizador == 200):
            VistaGestionInformacion.getUsuario(request.json["usuario"],request.json["contrasena"])
        return "Acceso permitido" , autorizador        