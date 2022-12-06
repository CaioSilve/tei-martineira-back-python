from flask import Blueprint
from flask_restful import reqparse

from Models.ClienteModel import ClienteModel
from Utils.tratar_dados import tratar_dados_cliente

bp_cliente = Blueprint("cliente", __name__)


@bp_cliente.route("/create", methods=['POST'])
def create():
    dados = tratar_dados_cliente(reqparse.RequestParser())

    cliente = ClienteModel(**dados)
    cliente.save_cliente()

    return cliente.json(), 201

@bp_cliente.route("/get/<int:id>", methods=['GET'])
def get_by_id(id):
    cliente = ClienteModel.find_cliente(id)
    if cliente == None:
        return {"mensagem": "cliente não encontrado"}, 404
    return cliente.json(), 200

@bp_cliente.route("/get", methods=['GET'])
def get_all():
    return {"clientes": [cliente.json() for cliente in ClienteModel.query.all()]}

@bp_cliente.route("/update/<int:id>", methods=['PUT'])
def update(id):
    dados = tratar_dados_cliente(reqparse.RequestParser())
    cliente_encontrado = ClienteModel.find_cliente(id)

    if cliente_encontrado:
        cliente_encontrado.update_cliente(**dados)
        cliente_encontrado.save_cliente()
        return cliente_encontrado.json(), 200

    cliente = ClienteModel(**dados)
    cliente.save_cliente()

    return cliente.json(), 201

@bp_cliente.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
    cliente_encontrado = ClienteModel.find_cliente(id)

    if cliente_encontrado:
        cliente_encontrado.delete_cliente()
        return {"mensagem": "cliente deletado"}, 200
    return {"mensagem": "cliente não encontrado"}, 404