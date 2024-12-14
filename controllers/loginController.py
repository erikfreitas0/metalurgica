from flask import request, jsonify
from models.usuario import Usuario
from models.vendedor import Vendedor
from database.db import db

def login_controller():
    if request.method == 'POST':
        data = request.get_json()
        login = data.get('login')
        senha = data.get('senha')

        # Tente encontrar um usuário com as credenciais fornecidas
        usuario = Usuario.query.filter_by(login=login, senha=senha).first()
        vendedor = Vendedor.query.filter_by(login=login, senha=senha).first()

        if usuario:
            # Usuário encontrado com sucesso, retorna o ID e mensagem
            return jsonify({
                "message": "Login realizado com sucesso!",
                "usuario_id": usuario.codigo  # Inclui o ID do usuário
            }), 200
        
        elif vendedor:
            # Vendedor encontrado com sucesso, retorna o ID e mensagem
            return jsonify({
                "message": "Login realizado com sucesso!",
            }), 200
        
        else:
            # Credenciais inválidas
            return jsonify({"error": "Credenciais inválidas!"}), 401
