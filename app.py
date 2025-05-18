import os
from flask import Flask, render_template
from flask_babel import Babel, _
from flask_login import LoginManager, current_user
from flask_apscheduler import APScheduler
import datetime
from bcrypt import gensalt, hashpw
from config import Config
from controllers.usuarioController import usuario_bp
from controllers.armarioController import armario_bp
from controllers.reservaController import reserva_bp

#Instanciando o app e definindo pasta de templates
app = Flask(__name__, template_folder=os.path.join('view','templates'))

#Aplicando as configurações do config.py
app.config.from_object(Config)
babel = Babel(app)

#Inicializando o gerenciador de logins
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = 'usuario.login'

#Inicializando o agendador 

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

#Definindo função de atualização de status
def atualizarStatus():
    with app.app_context():
        print(_("Iniciando atualização de status de reservas diária"))
        hoje = datetime.date.today()
        try:
            reservasIniciandoHoje = Reserva.query.filter(Reserva.inicio == hoje).all()
            for reserva in reservasIniciandoHoje:
                reserva.armario.disponibilidadeId = 2 
            reservasEncerrando = Reserva.query.filter(Reserva.fim < hoje).all()
            for reserva in reservasEncerrando:
                armarioId = reserva.armarioId
                #Checa se é a ultima reserva desse armário e o marca como disponível caso seja
                reservasRestantes = Reserva.query.filter(Reserva.armarioId == armarioId, Reserva.finalizada != True, Reserva.id != reserva.id).all()
                if len(reservasRestantes) ==0:
                    armarioDisponivel = db.session.get(Armario, armarioId)
                    armarioDisponivel.disponibilidadeId = 1
                reserva.finalizada = True

            db.session.commit()
            horario = datetime.datetime.now()
            print(_(f"Atualização realizada com sucesso às {horario.hour}:{horario.minute:02d}"))
        except Exception as e:
            print(_(f"Houve um erro na atualização diária: {e}"))

#Configurando para executar função em um horário determinado
scheduler.add_job(
    id='atualizarStatus', 
    func=atualizarStatus,      
    #Trigger para horário específico
    trigger='cron',
    #Horário em que será executado                    
    hour=3,                        
    minute=33,            
    #Substitui a tarefa caso ela já existir, para evitar bugs ao reiniciar o servidor   
    replace_existing=True     
)


#Função para carregar o usuário da sessão
@loginManager.user_loader
def load_user(userId):
    return Usuario.query.get(int(userId))

#Injeta variáveis no contexto de renderização dos templates
#Tudo que estiver dentro do dicionário será acessivel no template
#É chamado toda vez que um template é renderizado
@app.context_processor
def inject_user():
    return { 'usuarioAtual' : current_user } 
    

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

        #Adicionando usuário administrador para fins de teste, pode ser removido depois
        salt = gensalt(rounds=10)
        senhaHash = hashpw('admin'.encode('utf-8'), salt)
        admin = Usuario(nome='Administrador', admin=True, nomeDeUsuario='admin', senha=senhaHash)
        db.session.add(admin)

        db.session.commit()

#Rota da página inicial que renderiza o template html
@app.route('/')
def index():
    return render_template('PaginaInicial.html')

#Executa a aplicação flask caso o arquivo esteja sendo executado diretamente
if __name__  == '__main__':
    app.run(debug=True)