from flask import request, render_template
from database.db import db
from models.usuario import usuario

def usuario_controller():
        if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = usuario(data['nome'], data['login'], data['senha'])
                db.session.add(user)
                db.session.commit()
                return 'Usuário criado com sucesso', 200
            except Exception as e:
                return 'O usuário nao foi criado'.format(str(e)), 405
            
        elif request.method == 'GET':
            try:
                data = usuario.query.all()
                teste = {'usuarios': [usuario.to_dict() for usuario in data]}
                return teste
            except Exception as e:
                return 'Não foi possível buscar usuarios. Error: {}'.format(str(e)), 405
            
        elif request.method == "PUT":
            try:
                data = request.get_json()
                put_usuario_id = data['id']
                put_usuario = usuario.query.get(put_usuario_id)
                if put_usuario is None:
                    return {'error': 'usuario nao encontrado'}, 404
                put_usuario.nome = data.get('nome', put_usuario.nome)
                put_usuario.email = data.get('email', put_usuario.email)
                put_usuario.login = data.get('login', put_usuario.login)
                put_usuario.senha = data.get('senha', put_usuario.senha)
                print(put_usuario.nome, put_usuario.email, put_usuario.login, put_usuario.senha)
                db.session.commit()
                return 'usuario atualizado com sucesso', 200
            except Exception as e:
                return {'error': 'erro ao atualizar o usuario. Erro {}'.format(e)}, 400
            
        elif request.method == "DELETE":
            try:
                data = request.get_json()
                delete_usuario_id = data['id']
                delete_usuario = usuario.query.get(delete_usuario_id)
                if delete_usuario is None:
                    return {'error': 'usuario nao encontrado'}, 404
                db.session.delete(delete_usuario)
                db.session.commit()
                return 'usuario deletado com sucesso', 200
            except Exception as e:
                return {'error': 'erro ao atualizar o usuario. Erro {}'.format(e)}, 400