from flask import Flask, request, render_template
from database.db import db
from flask_cors import CORS
from routes.index import default_routes

class App:
    def __init__(self):
        self.app = Flask(__name__)

        # Configuração global do CORS
        CORS(self.app, resources={r"/*": {"origins": "*"}})
        
        # Configuração do banco de dados
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/metalurgica'
        db.init_app(self.app)
        
        # Registrar rotas
        default_routes(self.app)

        # Lidar com requisições OPTIONS antes do processamento
        @self.app.before_request
        def handle_options_requests():
            if request.method == 'OPTIONS':
                response = self.app.make_response('')
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
                response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
                return response

        # Garantir que os cabeçalhos CORS sejam adicionados a todas as respostas
        @self.app.after_request
        def add_cors_headers(response):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            return response

    def run(self):
        return self.app.run(port=3000, host='localhost', debug=True)

# Rota de exemplo para renderizar index.html
def index():
    return render_template('index.html')

# Inicializar a aplicação
app = App()
app.run()
