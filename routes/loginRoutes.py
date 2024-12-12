from controllers.loginController import login_controller

def login(app):
    app.route('/metalurgica/login', methods=['POST'])(login_controller)
