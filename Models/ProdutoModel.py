from sqlalchemy.orm import relationship

from database import db
from Models.ExameModel import ExameModel


class ProdutoModel(db.Model):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(80))
    tipo = db.Column(db.String(80))
    valorUnit = db.Column(db.Float)
    qtde = db.Column(db.Integer)
    validade = db.Column(db.String(80))
    pedido_id = db.Column(db.Integer, db.ForeignKey("pedido.id"))

    def __init__(self, desc, tipo, valorUnit, qtde, validade):
        self.desc = desc
        self.tipo = tipo
        self.valorUnit = valorUnit
        self.qtde = qtde
        self.validade = validade

    def json(self):
        return {
            'id': self.id,
            'desc': self.desc,
            'tipo': self.tipo,
            'valorUnit': self.valorUnit,
            'qtde': self.qtde,
            'validade': self.validade,
        }

    @classmethod
    def find_produto(cls, id):
        produto = cls.query.filter_by(id=id).first()
        if produto:
            return produto
        return None

    def save_produto(self):
        db.session.add(self)
        db.session.commit()

    def update_produto(self, desc, tipo, valorUnit, qtde, validade):
        self.desc = desc
        self.tipo = tipo
        self.valorUnit = valorUnit
        self.qtde = qtde
        self.validade = validade

    def delete_produto(self):
        db.session.delete(self)
        db.session.commit()

    def associar_pedido(self, id):
        self.pedido_id = id
        db.session.commit()