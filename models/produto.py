from database.db import db

class Produto(db.Model):
    # Definição das colunas
    codigo = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100))
    peso = db.Column(db.Float)
    espessura = db.Column(db.Float)
    preco = db.Column(db.Float)

    def __init__(self, tipo, peso, espessura, preco):
        self.tipo = tipo
        self.peso = peso
        self.espessura = espessura
        self.preco = preco 

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'tipo': self.tipo,
            'peso': self.peso,
            'espessura': self.espessura,
            'preco': self.preco
        }
