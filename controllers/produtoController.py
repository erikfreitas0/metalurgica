from flask import Blueprint, request, jsonify
from database.db import db
from models.produto import Produto
from models.usuario import Usuario

def produto_controller():
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            if data.get('usuario_id') is None:
                return jsonify({'error': 'Usuário não autenticado. Por favor, faça login.'}), 400

            print(data)

            # Verificação de dados obrigatórios
            if 'usuario_id' not in data or 'tipo' not in data or 'peso' not in data or 'espessura' not in data:
                return jsonify({'error': 'Campos obrigatórios faltando: usuario_id, tipo, peso, espessura'}), 400

            # Verificação de tipos numéricos
            if not isinstance(data['peso'], (int, float)) or not isinstance(data['espessura'], (int, float)):
                return jsonify({'error': 'Peso e espessura devem ser numéricos'}), 400

            # Verificar se o usuário existe
            usuario = Usuario.query.get(data['usuario_id'])
            if not usuario:
                return jsonify({'error': 'Usuário não encontrado'}), 400

            # Criação do produto
            produto = Produto(
                usuario_id=data['usuario_id'],
                tipo=data['tipo'],
                peso=data['peso'],
                espessura=data['espessura'],
                preco=data.get('preco', 0.0),  # Definir preço padrão como 0.0
                status=data.get('status', 'Pendente')
            )
            db.session.add(produto)
            db.session.commit()
            return jsonify({'message': 'Produto cadastrado com sucesso'}), 200
        except Exception as e:
            db.session.rollback()  # Rollback em caso de erro
            print(f"Erro: {e}")
            return jsonify({'error': f'O produto não foi cadastrado: {str(e)}'}), 400

    elif request.method == 'GET':
        try:
            produtos = Produto.query.all()
            return jsonify({'produtos': [produto.to_dict() for produto in produtos]})
        except Exception as e:
            return jsonify({'error': f'Não foi possível buscar produtos: {str(e)}'}), 400

    elif request.method == 'PUT':
        try:
            data = request.get_json()
            produto_id = data.get('codigo')  # Usar o campo 'codigo' para buscar o produto
            if not produto_id:
                return jsonify({'error': 'Código do produto não fornecido'}), 400

            produto = Produto.query.get(produto_id)
            if not produto:
                return jsonify({'error': 'Produto não encontrado'}), 404
            
            # Atualiza os campos fornecidos
            if 'preco' in data:
                produto.preco = data['preco']
            if 'status' in data:
                produto.status = data['status']

            # Comitar as mudanças no banco de dados
            db.session.commit()
            return jsonify({'message': 'Produto atualizado com sucesso'}), 200
        except Exception as e:
            db.session.rollback()  # Rollback em caso de erro
            return jsonify({'error': f'Erro ao atualizar o produto: {str(e)}'}), 400

    elif request.method == 'DELETE':
        try:
            data = request.get_json()
            produto_id = data['codigo']
            produto = Produto.query.get(produto_id)
            if not produto:
                return jsonify({'error': 'Produto não encontrado'}), 404
            
            db.session.delete(produto)
            db.session.commit()
            return jsonify({'message': 'Produto deletado com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': f'Erro ao deletar o produto: {str(e)}'}), 400
