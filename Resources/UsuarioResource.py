from flask import Blueprint
from flask_restful import reqparse

from Models.UsuarioModel import UsuarioModel
from Utils.tratar_dados import (tratar_dados_usuario,
                                tratar_dados_usuario_update)

bp_usuario = Blueprint("usuario", __name__)


@bp_usuario.route("/create", methods=['POST'])
def create():
    dados = tratar_dados_usuario(reqparse.RequestParser())

    if UsuarioModel.find_usuario(dados["usuario"]):
        return {"mensagem": "usuário com esse login já existe"}, 200

    usuario = UsuarioModel(**dados)
    usuario.save_usuario()

    return usuario.json(), 201

@bp_usuario.route("/get/<string:usuario>", methods=['GET'])
def get_by_id(usuario):
    usuario = UsuarioModel.find_usuario(usuario)
    if usuario == None:
        return {"mensagem": "usuário não encontrado"}, 404
    return usuario.json(), 200

@bp_usuario.route("/get", methods=['GET'])
def get_all():
    return {"usuários": [usuario.json() for usuario in UsuarioModel.query.all()]}

@bp_usuario.route("/update/<string:login>", methods=['PUT'])
def update(login):
    dados = tratar_dados_usuario_update(reqparse.RequestParser())
    usuario_encontrado = UsuarioModel.find_usuario(login)

    if usuario_encontrado:
        usuario_encontrado.update_usuario(**dados)
        usuario_encontrado.save_usuario()
        return usuario_encontrado.json(), 200

    return {"mensagem": "usuário não encontrado"}, 404

@bp_usuario.route("/delete/<string:login>", methods=['DELETE'])
def delete(login):
    usuario_encontrado = UsuarioModel.find_usuario(login)

    if usuario_encontrado:
        usuario_encontrado.delete_usuario()
        return {"mensagem": "usuário deletado"}, 200
    return {"mensagem": "usuário não encontrado"}, 404