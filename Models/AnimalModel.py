from sqlalchemy.orm import relationship

from database import db
from Models.ExameModel import ExameModel


class AnimalModel(db.Model):
    __tablename__ = 'animal'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    tipo = db.Column(db.String(80))
    raca = db.Column(db.String(80))
    dono_id = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    dono = db.relationship("ClienteModel")
    idade = db.Column(db.Integer)
    exames = db.relationship("ExameModel")

    def __init__(self, nome, tipo, raca, dono_id, idade):
        self.nome = nome
        self.tipo = tipo
        self.raca = raca
        self.dono_id = dono_id
        self.idade = idade

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'tipo': self.tipo,
            'raca': self.raca,
            'dono_id': self.dono_id,
            'idade': self.idade
        }

    @classmethod
    def find_animal(cls, id):
        animal = cls.query.filter_by(id=id).first()
        if animal:
            return animal
        return None

    def save_animal(self):
        db.session.add(self)
        db.session.commit()

    def update_animal(self, nome, tipo, raca, idade):
        self.nome = nome
        self.tipo = tipo
        self.raca = raca
        self.idade = idade

    def delete_animal(self):
        db.session.delete(self)
        db.session.commit()