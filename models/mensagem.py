from database.db import db

class Mensagem(db.Model):
    # Definição das colunas
    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(20))  # Alterado para String para acomodar código de área e números
    mensagem = db.Column(db.String(500))

    def __init__(self, nome, email, telefone, mensagem):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.mensagem = mensagem

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'mensagem': self.mensagem
        }
