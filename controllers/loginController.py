from flask import request, jsonify
from models.usuario import Usuario
from models.vendedor import Vendedor
from database.db import db

def login_controller():
    if request.method == 'POST':
        data = request.get_json()
        login = data.get('login')
        senha = data.get('senha')

        usuario = Usuario.query.filter_by(login=login, senha=senha).first()
        vendedor = Vendedor.query.filter_by(login=login, senha=senha).first()

        if usuario:
            return jsonify({
                "message": "Login realizado com sucesso!",
                "usuario_id": usuario.codigo 
            }), 200
        
        elif vendedor:
            return jsonify({
                "message": "Login realizado com sucesso!",
            }), 200
        
        else:
            return jsonify({"error": "Credenciais inválidas!"}), 401
