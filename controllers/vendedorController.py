from flask import request, render_template
from database.db import db
from models.vendedor import Vendedor

def vendedor_controller():
        if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Vendedor(data['nome'], data['login'], data['senha'])
                db.session.add(user)
                db.session.commit()
                return 'vendedor criado com sucesso', 200
            except Exception as e:
                return 'O vendedor nao foi criado'.format(str(e)), 405
            
        elif request.method == 'GET':
            try:
                data = Vendedor.query.all()
                teste = {'vendedores': [vendedor.to_dict() for vendedor in data]}
                return teste
            except Exception as e:
                return 'Não foi possível buscar vendedores. Error: {}'.format(str(e)), 405
            
        elif request.method == "PUT":
            try:
                data = request.get_json()
                put_vendedor_id = data['id']
                put_vendedor = Vendedor.query.get(put_vendedor_id)
                if put_vendedor is None:
                    return {'error': 'vendedor nao encontrado'}, 404
                put_vendedor.nome = data.get('nome', put_vendedor.nome)
                put_vendedor.cpf = data.get('cpf', put_vendedor.cpf)
                put_vendedor.email = data.get('email', put_vendedor.email)
                put_vendedor.telefone = data.get('telefone', put_vendedor.telefone)
                put_vendedor.login = data.get('login', put_vendedor.login)
                put_vendedor.senha = data.get('senha', put_vendedor.senha)
                print(put_vendedor.nome, put_vendedor.email, put_vendedor.login, put_vendedor.senha)
                db.session.commit()
                return 'vendedor atualizado com sucesso', 200
            except Exception as e:
                return {'error': 'erro ao atualizar o vendedor. Erro {}'.format(e)}, 400
            
        elif request.method == "DELETE":
            try:
                data = request.get_json()
                delete_vendedor_id = data['id']
                delete_vendedor = Vendedor.query.get(delete_vendedor_id)
                if delete_vendedor is None:
                    return {'error': 'vendedor nao encontrado'}, 404
                db.session.delete(delete_vendedor)
                db.session.commit()
                return 'vendedor deletado com sucesso', 200
            except Exception as e:
                return {'error': 'erro ao atualizar o vendedor. Erro {}'.format(e)}, 400