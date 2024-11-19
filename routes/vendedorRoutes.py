from controllers.vendedorController import vendedor_controller

def vendedor(app):
    app.route('/metalurgica/vendedor', methods=['POST', 'GET', 'PUT', 'DELETE'])(vendedor_controller)