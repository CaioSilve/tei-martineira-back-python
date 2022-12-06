from database import db


class UsuarioModel(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80))
    senha = db.Column(db.String(80))
    nome = db.Column(db.String(80))
    sobrenome = db.Column(db.String(80))

    def __init__(self, usuario, senha, nome, sobrenome):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.sobrenome = sobrenome

    def json(self):
        return {
            'id': self.id,
            'usuario': self.usuario,
            'senha': self.senha,
            'nome': self.nome,
            'sobrenome': self.sobrenome
        }

    @classmethod
    def find_usuario(cls, usuario):
        usuario = cls.query.filter_by(usuario=usuario).first()
        if usuario:
            return usuario
        return None

    def save_usuario(self):
        db.session.add(self)
        db.session.commit()

    def update_usuario(self, senha, nome, sobrenome):
        self.senha = senha
        self.nome = nome
        self.sobrenome = sobrenome

    def delete_usuario(self):
        db.session.delete(self)
        db.session.commit()