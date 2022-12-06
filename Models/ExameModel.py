from datetime import datetime

from database import db


class ExameModel(db.Model):
    __tablename__ = 'exame'

    id = db.Column(db.Integer, primary_key=True)
    paciente = db.Column(db.Integer, db.ForeignKey("animal.id"))
    procedimento = db.Column(db.String(80))
    resultado = db.Column(db.String(80))
    data = db.Column(db.DateTime)

    def __init__(self, paciente, procedimento, resultado, data):
        self.paciente = paciente
        self.procedimento = procedimento
        self.resultado = resultado
        self.data = datetime.strptime(data, '%d/%m/%Y %H:%M')

    def json(self):
        return {
            'id': self.id,
            'paciente': self.paciente,
            'procedimento': self.procedimento,
            'resultado': self.resultado,
            'data': self.data.strftime('%d/%m/%Y %H:%M')
        }

    @classmethod
    def find_exame(cls, id):
        exame = cls.query.filter_by(id=id).first()
        if exame:
            return exame
        return None

    def save_exame(self):
        db.session.add(self)
        db.session.commit()

    def update_exame(self, procedimento, resultado, data):
        self.procedimento = procedimento
        self.resultado = resultado
        self.data = datetime.strptime(data, '%d/%m/%Y %H:%M')

    def delete_exame(self):
        db.session.delete(self)
        db.session.commit()