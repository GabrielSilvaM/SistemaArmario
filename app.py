import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from controllers.mainController import MainController

#Instanciando o app e definindo pasta de templates
app = Flask(__name__, template_folder=os.path.join('view','templates'))
app.config.from_object(Config)

#importando tudo no models
from models import *

db.init_app(app)

#Criando o banco de dados e preenchendo a tabela de referência caso não existam ainda
with app.app_context():
    db.create_all()
    if  not Disponibilidade.query.first():
        opcoes = [Disponibilidade(descricao='Disponível'), Disponibilidade(descricao='Em uso'),Disponibilidade(descricao='Reservado')]
        db.session.add_all(opcoes)
        db.session.commit()


app.add_url_rule('/', 'index', MainController.index)

if __name__  == '__main__':
    app.run(debug=True)