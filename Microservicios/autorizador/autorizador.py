import logging, datetime
from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from modelos import db, Usuario, UsuarioSchema
from modelos.modelos import LogMicroServicios

usuario_schema = UsuarioSchema()

import logging
from flask import Flask

app = Flask(__name__)
activo = None

class VistaAutorizador:

    def __init__(self):
        self.activo = True

    def autenticacionUsuario(usuario, contrasena):
        nuevo_log = LogMicroServicios(fecha = datetime.datetime.now(), mensaje = "Se recibe petición de autenticación por usuario: " + usuario, microservicio = "Autorizador")
        db.session.add(nuevo_log)
        usuario = db.session.query(Usuario.id, Usuario.usuario).filter(Usuario.usuario == usuario, 
            Usuario.contrasena == contrasena).first()
        db.session.commit()
        if usuario is None:
            nuevo_log = LogMicroServicios(fecha = datetime.datetime.now(), mensaje = "Autenticación de usuario rechazada" , microservicio = "Autorizador")
            db.session.add(nuevo_log)
            db.session.commit()
            return 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == request.json["contrasena"]).first()
            nuevo_log = LogMicroServicios(fecha = datetime.datetime.now(), mensaje = "Autenticación de usuario completada" , microservicio = "Autorizador")
            db.session.add(nuevo_log)
            db.session.commit()
            return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso}

    def autorizarUsuario(usuario):
        nuevo_log = LogMicroServicios(fecha = datetime.datetime.now(), mensaje = "Se recibe petición de autorización para usuario: " + usuario, microservicio = "Autorizador")
        db.session.add(nuevo_log)
        user = Usuario.query.filter(Usuario.usuario == usuario).first()
        usuarioJson =  usuario_schema.dump(user)
        if(usuarioJson['rol'] == "admin"):
            nuevo_log = LogMicroServicios(fecha = datetime.datetime.now(), mensaje = "Usuario " + usuario + " tiene permisos de admin", microservicio = "Autorizador")
            db.session.add(nuevo_log)
            db.session.commit()
            return 200
        else:
            nuevo_log = LogMicroServicios(fecha = datetime.datetime.now(), mensaje = "Usuario " + usuario + " no tiene permisos de admin", microservicio = "Autorizador")
            db.session.add(nuevo_log)
            db.session.commit()
            return 401
