from flask import Flask, render_template
from database.db import db
from flask_cors import CORS
from routes.index import default_routes

class App:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/metalurgica' 
        db.init_app(self.app)
        default_routes(self.app) 

    def run(self):
        return self.app.run(port=3000, host='localhost', debug=True)
    
def index():
    # Renderiza o template HTML e passa variáveis
    return render_template('index.html')

app = App()
app.run()
