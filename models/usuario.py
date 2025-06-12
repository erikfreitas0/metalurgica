from database.db import db

class Usuario(db.Model):
    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(20))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(10))
    login = db.Column(db.String(100))  
    senha = db.Column(db.String(100))
    
    def __init__(self, nome, cpf, email, telefone, login, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.login = login
        self.senha = senha

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'login': self.login,
            'senha': self.senha
        }
