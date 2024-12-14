from flask import Blueprint, request, jsonify
from database.db import db
from models.produto import Produto
from models.usuario import Usuario

from flask import request, jsonify

def atualizar_produto(produto_id):
    """
    Atualiza os campos de um produto com base no ID e nos dados fornecidos.
    """
    try:
        # Pega os dados do corpo da requisição
        data = request.get_json()

        produto = Produto.query.get(produto_id)
        if not produto:
            return jsonify({'error': 'Produto não encontrado'}), 404

        # Atualiza os campos fornecidos
        if 'preco' in data:
            if not isinstance(data['preco'], (int, float)):
                return jsonify({'error': 'O preço deve ser um valor numérico válido.'}), 400
            produto.preco = data['preco']

        if 'status' in data:
            if not isinstance(data['status'], str):
                return jsonify({'error': 'O status deve ser um texto válido.'}), 400
            produto.status = data['status']

        # Commit das alterações
        db.session.commit()
        return jsonify({'message': 'Produto atualizado com sucesso'}), 200

    except Exception as e:
        db.session.rollback()  # Rollback em caso de erro
        print(f"Erro ao atualizar produto: {str(e)}")  # Log para depuração
        return jsonify({'error': f'Erro ao atualizar o produto: {str(e)}'}), 500


def produto_controller():
    if request.method == 'POST':
        try:
            data = request.get_json()

            # Validação de campos obrigatórios
            if not all(k in data for k in ('usuario_id', 'tipo', 'peso', 'espessura')):
                return jsonify({'error': 'Campos obrigatórios faltando: usuario_id, tipo, peso, espessura'}), 400

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
                preco=data.get('preco', 0.0),  # Preço padrão 0.0
                status=data.get('status', 'Pendente')
            )
            db.session.add(produto)
            db.session.commit()
            return jsonify({'message': 'Produto cadastrado com sucesso'}), 200
        except Exception as e:
            db.session.rollback()
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
            # Obtém o ID do produto da query string
            produto_id = request.args.get('produto_id', type=int)
            if not produto_id:
                return jsonify({'error': 'ID do produto não fornecido na URL'}), 400

            # Obtém os dados do corpo da requisição
            data = request.get_json()
            if not isinstance(data, dict):
                return jsonify({'error': 'Dados enviados no formato incorreto. Deve ser um JSON válido.'}), 400

            # Chama a função de atualização
            return atualizar_produto(produto_id, data)

        except Exception as e:
            print(f"Erro ao processar PUT: {str(e)}")
            return jsonify({'error': f'Erro ao processar a solicitação: {str(e)}'}), 500

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
            print(f"Erro ao deletar produto: {str(e)}")
            return jsonify({'error': f'Erro ao deletar o produto: {str(e)}'}), 400
