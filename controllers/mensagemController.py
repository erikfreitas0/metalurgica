from flask import request, render_template
from database.db import db
from models.mensagem import Mensagem

def mensagem_controller():
        if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Mensagem(data['nome'], data['email'], data['telefone'], data['mensagem'])
                db.session.add(user)
                db.session.commit()
                return 'Mensagem criada com sucesso', 200
            except Exception as e:
                return 'A mensagem nao foi criada'.format(str(e)), 405
            
        elif request.method == 'GET':
            try:
                data = Mensagem.query.all()
                teste = {'mensagems': [mensagem.to_dict() for mensagem in data]}
                return teste
            except Exception as e:
                return 'Não foi possível buscar mensagems. Error: {}'.format(str(e)), 405
            
        elif request.method == "PUT":
            try:
                data = request.get_json()
                put_mensagem_id = data['id']
                put_mensagem = Mensagem.query.get(put_mensagem_id)
                if put_mensagem is None:
                    return {'error': 'mensagem nao encontrada'}, 404
                put_mensagem.nome = data.get('nome', put_mensagem.nome)
                put_mensagem.email = data.get('email', put_mensagem.email)
                put_mensagem.telefone = data.get('telefone', put_mensagem.telefone)
                put_mensagem.mensagem = data.get('mensagem', put_mensagem.mensagem)
                print(put_mensagem.nome, put_mensagem.email, put_mensagem.telefone, put_mensagem.mensagem)
                db.session.commit()
                return 'mensagem atualizada com sucesso', 200
            except Exception as e:
                return {'error': 'erro ao atualizar a mensagem. Erro {}'.format(e)}, 400
            
        elif request.method == "DELETE":
            try:
                data = request.get_json()
                delete_mensagem_id = data['id']
                delete_mensagem = Mensagem.query.get(delete_mensagem_id)
                if delete_mensagem is None:
                    return {'error': 'mensagem nao encontrada'}, 404
                db.session.delete(delete_mensagem)
                db.session.commit()
                return 'mensagem deletada com sucesso', 200
            except Exception as e:
                return {'error': 'erro ao atualizar a mensagem. Erro {}'.format(e)}, 400