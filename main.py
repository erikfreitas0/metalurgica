from flask import Flask, request, render_template
from database.db import db
from flask_cors import CORS
from routes.index import default_routes

class App:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app, resources={r"/*": {"origins": "*"}})
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/metalurgica' 
        db.init_app(self.app)
        default_routes(self.app)

        # Função para lidar com requisições OPTIONS
        @self.app.before_request
        def handle_options_requests():
            if request.method == 'OPTIONS':
                response = self.app.make_response('')
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
                response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
                return response

    def run(self):
        return self.app.run(port=3000, host='localhost', debug=True)
    
def index():
    # Renderiza o template HTML e passa variáveis
    return render_template('index.html')

app = App()
app.run()
