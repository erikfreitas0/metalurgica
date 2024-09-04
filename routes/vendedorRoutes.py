from controllers.vendedorController import vendedor_controller

def vendedor(app):
    app.route('/vendedor', methods=['POST', 'GET', 'PUT', 'DELETE'])(vendedor_controller)