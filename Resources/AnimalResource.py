from flask import Blueprint
from flask_restful import reqparse

from Models.AnimalModel import AnimalModel
from Models.ClienteModel import ClienteModel
from Utils.tratar_dados import tratar_dados_animal, tratar_dados_animal_update

bp_animal = Blueprint("animal", __name__)


@bp_animal.route("/create", methods=['POST'])
def create():
    dados = tratar_dados_animal(reqparse.RequestParser())

    if ClienteModel.find_cliente(dados["dono_id"]):

        animal = AnimalModel(**dados)
        animal.save_animal()

        return animal.json(), 201
    return {"mensagem": "dono não encontrado, um animal precisa ter um dono"}, 404

@bp_animal.route("/get/<int:id>", methods=['GET'])
def get_by_id(id):
    animal = AnimalModel.find_animal(id)
    if animal == None:
        return {"mensagem": "animal não encontrado"}, 404
    return animal.json(), 200

@bp_animal.route("/get", methods=['GET'])
def get_all():
    return {"animais": [animal.json() for animal in AnimalModel.query.all()]}

@bp_animal.route("/update/<int:id>", methods=['PUT'])
def update(id):
    dados = tratar_dados_animal_update(reqparse.RequestParser())
    animal_encontrado = AnimalModel.find_animal(id)

    if animal_encontrado:
        animal_encontrado.update_animal(**dados)
        animal_encontrado.save_animal()
        return animal_encontrado.json(), 200

    return {"mensagem": "animal não encontrado"}, 404

@bp_animal.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
    animal_encontrado = AnimalModel.find_animal(id)

    if animal_encontrado:
        animal_encontrado.delete_animal()
        return {"mensagem": "animal deletado"}, 200
    return {"mensagem": "animal não encontrado"}, 404