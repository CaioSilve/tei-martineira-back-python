from flask import Blueprint
from flask_restful import reqparse

from Models.AnimalModel import AnimalModel
from Models.ExameModel import ExameModel
from Utils.tratar_dados import tratar_dados_exame, tratar_dados_exame_update

bp_exame = Blueprint("exame", __name__)


@bp_exame.route("/create", methods=['POST'])
def create():
    dados = tratar_dados_exame(reqparse.RequestParser())

    if AnimalModel.find_animal(dados["paciente"]):

        exame = ExameModel(**dados)
        exame.save_exame()

        return exame.json(), 201
    return {"mensagem": "animal não encontrado, um exame precisa ter um animal"}, 404

@bp_exame.route("/get/<int:id>", methods=['GET'])
def get_by_id(id):
    exame = ExameModel.find_exame(id)
    if exame == None:
        return {"mensagem": "exame não encontrado"}, 404
    return exame.json(), 200

@bp_exame.route("/get", methods=['GET'])
def get_all():
    return {"exames": [exame.json() for exame in ExameModel.query.all()]}

@bp_exame.route("/update/<int:id>", methods=['PUT'])
def update(id):
    dados = tratar_dados_exame_update(reqparse.RequestParser())
    exame_encontrado = ExameModel.find_exame(id)

    if exame_encontrado:
        exame_encontrado.update_exame(**dados)
        exame_encontrado.save_exame()
        return exame_encontrado.json(), 200

    return {"mensagem": "exame não encontrado"}, 404

@bp_exame.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
    exame_encontrado = ExameModel.find_exame(id)

    if exame_encontrado:
        exame_encontrado.delete_exame()
        return {"mensagem": "exame deletado"}, 200
    return {"mensagem": "exame não encontrado"}, 404