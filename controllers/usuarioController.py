from flask import request, jsonify
from models.usuario import Usuario
from database.db import db

def usuario_controller():
    if request.method == 'POST':
        # Lógica de cadastro de usuário
        try:
            data = request.get_json()
            user = Usuario(data['nome'], data['cpf'], data['email'], data['telefone'], data['login'], data['senha'])
            db.session.add(user)
            db.session.commit()
            return jsonify({'message': 'Usuário criado com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': f'O usuário não foi criado. Erro: {str(e)}'}), 405

    elif request.method == 'GET':
        # Lógica para obter usuários
        try:
            data = Usuario.query.all()
            return jsonify({'usuarios': [usuario.to_dict() for usuario in data]}), 200
        except Exception as e:
            return jsonify({'error': f'Não foi possível buscar os usuários. Erro: {str(e)}'}), 405

    elif request.method == 'PUT':
        # Lógica para atualizar um usuário
        try:
            data = request.get_json()
            put_usuario_id = data['id']
            put_usuario = Usuario.query.get(put_usuario_id)
            if not put_usuario:
                return jsonify({'error': 'Usuário não encontrado'}), 404
            # Atualizando os campos
            put_usuario.nome = data.get('nome', put_usuario.nome)
            put_usuario.cpf = data.get('cpf', put_usuario.cpf)
            put_usuario.email = data.get('email', put_usuario.email)
            put_usuario.telefone = data.get('telefone', put_usuario.telefone)
            put_usuario.login = data.get('login', put_usuario.login)
            put_usuario.senha = data.get('senha', put_usuario.senha)
            db.session.commit()
            return jsonify({'message': 'Usuário atualizado com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': f'Erro ao atualizar o usuário. Erro: {str(e)}'}), 400

    elif request.method == 'DELETE':
        # Lógica para excluir um usuário
        try:
            data = request.get_json()
            delete_usuario_id = data['id']
            delete_usuario = Usuario.query.get(delete_usuario_id)
            if not delete_usuario:
                return jsonify({'error': 'Usuário não encontrado'}), 404
            db.session.delete(delete_usuario)
            db.session.commit()
            return jsonify({'message': 'Usuário deletado com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': f'Erro ao excluir o usuário. Erro: {str(e)}'}), 400


