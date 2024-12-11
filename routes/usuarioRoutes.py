from controllers.usuarioController import usuario_controller
def usuario(app):
    app.route('/metalurgica/usuario', methods=['POST', 'GET', 'PUT', 'DELETE'])(usuario_controller)


