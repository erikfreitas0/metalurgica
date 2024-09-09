from database.db import db

class usuario(db.Model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'senha': self.senha,
            'login': self.login
        }
    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.Integer(20))
    senha = db.Column(db.String(100))
    login = db.Column(db.String(100))

    def __init__(self, nome):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.login = login