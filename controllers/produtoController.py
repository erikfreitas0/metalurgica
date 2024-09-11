from flask import request, render_template
from database.db import db
from models.produto import Produto

def produto_controller():
        if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = produto(data['tipo'], data['peso'], data['espessura'], data['durabilidade'], data['preco'])
                db.session.add(user)
                db.session.commit()
                return 'Produto cadastrado com sucesso', 200
            except Exception as e:
                return 'O produto nao foi cadastrado {}'.format(e), 405
            
        elif request.method == 'GET':
            try:
                data = produto.query.all()
                teste = {'produtos': [produto.to_dict() for produto in data]}
                return teste
            except Exception as e:
                return 'Não foi possível buscar produtos. Error: {}'.format(str(e)), 405
            
        elif request.method == "PUT":
            try:
                data = request.get_json()
                put_produto_codigo = data['codigo']
                put_produto = produto.query.get(put_produto_codigo)
                if put_produto is None:
                    return {'error': 'produto nao encontrado. Erro {}'.format(e)}, 404
                put_produto.tipo = data.get('tipo', put_produto.tipo)
                put_produto.peso = data.get('peso', put_produto.peso)
                put_produto.espessura = data.get('espessura', put_produto.espessura)
                put_produto.durabilidade = data.get('durabilidade', put_produto.durabilidade)
                put_produto.preco = data.get('preco', put_produto.preco)
                print(put_produto.tipo, put_produto.peso, put_produto.espessura, put_produto.durabilidade, put_produto.preco)
                db.session.commit()
                return 'produto atualizado com sucesso', 200
            except Exception as e:
                return {'error': 'erro ao atualizar o produto. Erro {}'.format(e)}, 400
            
        elif request.method == "DELETE":
            try:
                data = request.get_json()
                delete_produto_codigo = data['codigo']
                delete_produto = produto.query.get(delete_produto_codigo)
                if delete_produto is None:
                    return {'error': 'produto nao encontrado'}, 404
                db.session.delete(delete_produto)
                db.session.commit()
                return 'produto deletado com sucesso', 200
            except Exception as e:
                return {'error': 'erro ao atualizar o produto. Erro {}'.format(e)}, 400