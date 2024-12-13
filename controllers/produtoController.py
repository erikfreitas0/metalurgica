from flask import Blueprint, request, jsonify
from database.db import db
from models.produto import Produto

def produto_controller():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print(data)
            # Criação do produto com `usuario_id`
            produto = Produto(
                usuario_id=data['usuario_id'],
                tipo=data['tipo'],
                peso=data['peso'],
                espessura=data['espessura'],
                preco=data.get('preco'),  # Pode ser None
                status=data.get('status', 'Pendente')  # Valor padrão se não fornecido
            )
            db.session.add(produto)
            db.session.commit()
            return jsonify({'message': 'Produto cadastrado com sucesso'}), 200
        except Exception as e:
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
            produto_id = data['codigo']
            produto = Produto.query.get(produto_id)
            if not produto:
                return jsonify({'error': 'Produto não encontrado'}), 404
            
            # Atualiza os campos fornecidos
            produto.usuario_id = data.get('usuario_id', produto.usuario_id)
            produto.tipo = data.get('tipo', produto.tipo)
            produto.peso = data.get('peso', produto.peso)
            produto.espessura = data.get('espessura', produto.espessura)
            produto.preco = data.get('preco', produto.preco)
            produto.status = data.get('status', produto.status)
            
            db.session.commit()
            return jsonify({'message': 'Produto atualizado com sucesso'}), 200
        except Exception as e:
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
