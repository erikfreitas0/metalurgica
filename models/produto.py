from database.db import db

class produto(db.Model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'tipo': self.tipo,
            'peso': self.peso,
            'espessura': self.espessura,
            'durabilidade': self.durabilidade,
            'local': self.local,
            'preco': self.preco
        }
    codigo = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100))
    peso = db.Column(db.Float(100))
    espessura = db.Column(db.String(100))
    durabilidade = db.Column(db.Integer(20))
    local = db.Column(db.String(100))
    preco = db.Column(db.Float(100))
    

    def __init__(self, tipo):
        self.tipo = tipo
        self.peso = peso
        self.espessura = espessura
        self.durabilidade = durabilidade
        self.local = local
        self.preco = preco