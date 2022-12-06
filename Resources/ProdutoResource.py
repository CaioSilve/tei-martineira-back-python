from flask import Blueprint
from flask_restful import reqparse

from Models.ProdutoModel import ProdutoModel
from Utils.tratar_dados import tratar_dados_animal_update, tratar_dados_produto

bp_produto = Blueprint("produto", __name__)


@bp_produto.route("/create", methods=['POST'])
def create():
    dados = tratar_dados_produto(reqparse.RequestParser())

    produto = ProdutoModel(**dados)
    produto.save_produto()

    return produto.json(), 201

@bp_produto.route("/get/<int:id>", methods=['GET'])
def get_by_id(id):
    produto = ProdutoModel.find_produto(id)
    if produto == None:
        return {"mensagem": "produto não encontrado"}, 404
    return produto.json(), 200

@bp_produto.route("/get", methods=['GET'])
def get_all():
    return {"produtos": [produto.json() for produto in ProdutoModel.query.all()]}

@bp_produto.route("/update/<int:id>", methods=['PUT'])
def update(id):
    dados = tratar_dados_produto(reqparse.RequestParser())
    produto_encontrado = ProdutoModel.find_produto(id)

    if produto_encontrado:
        produto_encontrado.update_produto(**dados)
        produto_encontrado.save_produto()
        return produto_encontrado.json(), 200

    return {"mensagem": "produto não encontrado"}, 404

@bp_produto.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
    produto_encontrado = ProdutoModel.find_produto(id)

    if produto_encontrado:
        produto_encontrado.delete_produto()
        return {"mensagem": "produto deletado"}, 200
    return {"mensagem": "produto não encontrado"}, 404