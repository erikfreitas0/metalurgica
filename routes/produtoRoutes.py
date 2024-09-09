from controllers.produtoController import produto_controller

def produto(app):
    app.route('/produto', methods=['POST', 'GET', 'PUT', 'DELETE'])(produto_controller)