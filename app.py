import os
from flask import Flask, render_template
from flask_babel import Babel, _
from config import Config
from controllers.usuarioController import usuario_bp
from controllers.armarioController import armario_bp
from controllers.reservaController import reserva_bp

#Instanciando o app e definindo pasta de templates
app = Flask(__name__, template_folder=os.path.join('view','templates'))

#Aplicando as configurações do config.py
app.config.from_object(Config)
babel = Babel(app)

#Aplicando os bps de rotas dos controllers
app.register_blueprint(usuario_bp)
app.register_blueprint(armario_bp)
app.register_blueprint(reserva_bp)

#importando tudo no models e incluindo o db no app
from models import *
db.init_app(app)

#Criando o banco de dados e preenchendo a tabela de referência caso não existam ainda
with app.app_context():
    db.create_all()
    if  not Disponibilidade.query.first():
        opcoes = [Disponibilidade(descricao=_('Disponível')), Disponibilidade(descricao=_('Em uso')),Disponibilidade(descricao=_('Reservado'))]
        db.session.add_all(opcoes)
        db.session.commit()

#Rota da página inicial que renderiza o template html
@app.route('/')
def index():
    return render_template('PaginaInicial.html')

#Executa a aplicação flask caso o arquivo esteja sendo executado diretamente
if __name__  == '__main__':
    app.run(debug=True)