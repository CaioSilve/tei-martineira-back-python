from flask import Blueprint
from flask_restful import reqparse

from Models.ClienteModel import ClienteModel
from Models.PedidoModel import PedidoModel
from Models.ProdutoModel import ProdutoModel
from Utils.tratar_dados import (tratar_dados_pedido,
                                tratar_dados_pedido_add_produto,
                                tratar_dados_pedido_update)

bp_pedido = Blueprint("pedido", __name__)


@bp_pedido.route("/create", methods=['POST'])
def create():
    dados = tratar_dados_pedido(reqparse.RequestParser())

    if ClienteModel.find_cliente(dados["cliente_id"]):

        pedido = PedidoModel(**dados)
        pedido.save_pedido()

        return pedido.json(), 201
    return {"mensagem": "cliente não encontrado, um pedido precisa ter um cliente"}, 404

@bp_pedido.route("/add_produto", methods=['POST'])
def add():
    dados = tratar_dados_pedido_add_produto(reqparse.RequestParser())

    produto = ProdutoModel.find_produto(dados["produto_id"])

    if produto:
        pedido = PedidoModel.find_pedido(dados["pedido_id"])
        if pedido:
            pedido.add_produto(produto)
            pedido.save_pedido()

            return pedido.json(), 201
        return {"mensagem": "pedido não encontrado."}, 404
    return {"mensagem": "produto não encontrado."}, 404

@bp_pedido.route("/get/<int:id>", methods=['GET'])
def get_by_id(id):
    pedido = PedidoModel.find_pedido(id)
    if pedido == None:
        return {"mensagem": "pedido não encontrado"}, 404
    return pedido.json(), 200

@bp_pedido.route("/get", methods=['GET'])
def get_all():
    return {"pedidos": [pedido.json() for pedido in PedidoModel.query.all()]}

@bp_pedido.route("/update/<int:id>", methods=['PUT'])
def update(id):
    dados = tratar_dados_pedido_update(reqparse.RequestParser())
    pedido_encontrado = PedidoModel.find_pedido(id)

    if pedido_encontrado:
        pedido_encontrado.update_pedido(**dados)
        pedido_encontrado.save_pedido()
        return pedido_encontrado.json(), 200

    return {"mensagem": "pedido não encontrado"}, 404

@bp_pedido.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
    pedido_encontrado = PedidoModel.find_pedido(id)

    if pedido_encontrado:
        pedido_encontrado.delete_pedido()
        return {"mensagem": "pedido deletado"}, 200
    return {"mensagem": "pedido não encontrado"}, 404