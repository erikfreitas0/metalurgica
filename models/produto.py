from database.db import db

class Produto(db.Model):
    
    # Definição das colunas
    codigo = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.codigo'), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    peso = db.Column(db.Float(precision=2), nullable=False)
    espessura = db.Column(db.Float(precision=2), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=True)
    status = db.Column(db.String(20), default='Pendente', nullable=False)
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    # Construtor da classe
    def __init__(self, usuario_id, tipo, peso, espessura, preco=None, status='Pendente'):
        self.usuario_id = usuario_id
        self.tipo = tipo
        self.peso = peso
        self.espessura = espessura
        self.preco = preco
        self.status = status

    # Método para converter o objeto em um dicionário
    def to_dict(self):
        return {
            'codigo': self.codigo,
            'usuario_id': self.usuario_id,
            'tipo': self.tipo,
            'peso': self.peso,
            'espessura': self.espessura,
            'preco': self.preco,
            'status': self.status,
            'data_criacao': self.data_criacao.strftime('%Y-%m-%d %H:%M:%S') if self.data_criacao else None
        }

