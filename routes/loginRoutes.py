from controllers.loginController import login_usuario


def login(app):
    app.route('/metalurgica/login', methods=['POST'])(login_usuario)
