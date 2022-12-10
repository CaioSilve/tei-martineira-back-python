from datetime import datetime

from database import db


class PedidoModel(db.Model):
    __tablename__ = 'pedido'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    precoTotal = db.Column(db.Float)
    produtos = db.relationship("ProdutoModel")
    data = db.Column(db.DateTime)

    def __init__(self, cliente_id, data):
        self.cliente_id = cliente_id
        self.data = datetime.strptime(data, '%d/%m/%Y')

    def json(self):
        total = 0.0
        for produto in self.produtos:
            total += (produto.valorUnit * produto.qtde)
        self.precoTotal = total

        return {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'precoTotal': self.precoTotal,
            "produtos": [produto.json() for produto in self.produtos],
            'data': self.data.strftime('%d/%m/%Y')
        }

    @classmethod
    def find_pedido(cls, id):
        pedido = cls.query.filter_by(id=id).first()
        if pedido:
            return pedido
        return None

    def save_pedido(self):
        db.session.add(self)
        db.session.commit()

    def update_pedido(self, data):
        self.data = datetime.strptime(data, '%d/%m/%Y')

    def delete_pedido(self):
        db.session.delete(self)
        db.session.commit()

    def add_produto(self, produto):
        produto.associar_pedido(self.id)