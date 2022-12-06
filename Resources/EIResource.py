import json

from flask import Blueprint
from flask_restful import reqparse

from Models.AnimalModel import AnimalModel
from Models.ClienteModel import ClienteModel
from Models.ExameModel import ExameModel
from Models.PedidoModel import PedidoModel
from Models.ProdutoModel import ProdutoModel
from Models.UsuarioModel import UsuarioModel
from Utils.importacoes import (importar_animal, importar_cliente,
                               importar_exame, importar_pedido,
                               importar_produto, importar_usuario)
from Utils.tratar_dados import tratar_import

bp_export = Blueprint("export", __name__)


@bp_export.route("/export", methods=['GET'])
def export():
    return {
        "animais": [animal.json() for animal in AnimalModel.query.all()],
        "clientes": [cliente.json() for cliente in ClienteModel.query.all()],
        "exames": [exame.json() for exame in ExameModel.query.all()],
        "pedidos": [pedido.json() for pedido in PedidoModel.query.all()],
        "produtos": [produto.json() for produto in ProdutoModel.query.all()],
        "usuarios": [usuario.json() for usuario in UsuarioModel.query.all()]
    }

@bp_export.route("/import", methods=['POST'])
def importa():
    try:
        dados = tratar_import(reqparse.RequestParser(bundle_errors=True))

        # A ordem importa
        importar_usuario(dados["usuarios"])
        importar_cliente(dados["clientes"])
        importar_animal(dados["animais"])
        importar_exame(dados["exames"])
        importar_produto(dados["produtos"])
        importar_pedido(dados["pedidos"])
    except:
        return {"mensagem": "formato inválido"}, 500
    
    return {"mensagem": "dados importados"}, 200
