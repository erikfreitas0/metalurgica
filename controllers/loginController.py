from flask import request, jsonify
from models.usuario import Usuario
from database.db import db


def login_usuario():
    if request.method == 'POST':
        data = request.get_json()
        login = data.get('login')
        senha = data.get('senha')

        # Tente encontrar um usuário com as credenciais fornecidas
        usuario = Usuario.query.filter_by(login=login, senha=senha).first()

        if usuario:
            # Usuário encontrado com sucesso
            return jsonify({"message": "Login realizado com sucesso!"}), 200
        else:
            # Credenciais inválidas
            return jsonify({"error": "Credenciais inválidas!"}), 401