from database import db
from Models.AnimalModel import AnimalModel


class ClienteModel(db.Model):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    email = db.Column(db.String(80))
    cidade = db.Column(db.String(80))
    endereco = db.Column(db.String(80))
    cpf = db.Column(db.String(80))
    celular = db.Column(db.String(80))
    telefone = db.Column(db.String(80))
    animais = db.relationship("AnimalModel")

    def __init__(self, nome, email, cpf, cidade, endereco, celular, telefone):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.cidade = cidade
        self.endereco = endereco
        self.celular = celular
        self.telefone = telefone

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'cidade': self.cidade,
            'endereco': self.endereco,
            'celular': self.celular,
            'telefone': self.telefone,
            "animais": [animal.json() for animal in self.animais]
        }

    @classmethod
    def find_cliente(cls, id):
        cliente = cls.query.filter_by(id=id).first()
        if cliente:
            return cliente
        return None

    def save_cliente(self):
        db.session.add(self)
        db.session.commit()

    def update_cliente(self, nome, email, cpf, cidade, endereco, celular, telefone):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.cidade = cidade
        self.endereco = endereco
        self.celular = celular
        self.telefone = telefone

    def delete_cliente(self):
        [animal.delete_animal() for animal in self.animais]
        db.session.delete(self)
        db.session.commit()