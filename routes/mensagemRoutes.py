from controllers.mensagemController import mensagem_controller

def mensagem(app):
    app.route('/metalurgica/mensagem', methods=['POST', 'GET', 'PUT', 'DELETE'])(mensagem_controller)