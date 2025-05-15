from flask import render_template, request, redirect, url_for, Blueprint
from bcrypt import hashpw, gensalt, checkpw
from flask_babel import _
#Importante o pacote de models e o db
from models import *

usuario_bp = Blueprint('usuario',__name__)


@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Pegando os dados do formulário
        username = request.form.get('username')
        senha = request.form.get('senha')
        #Verificando se o usuário está cadastrado
        busca = Usuario.query.filter_by(nomeDeUsuario=username).first()
        if busca:
            #Comparando os hashes das senhas
            if checkpw(senha.encode('utf-8'), busca.senha):
                return redirect(url_for('index'))
            else:
                return render_template('Login.html',fail=_("Usuário ou senha inválidos"))
        else:
            return render_template('Login.html',fail=_("Usuário ou senha inválidos"))
        
    else:    
        return render_template('Login.html')


@usuario_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        #Pegando dados do formulário do front 
        nome = request.form.get('nome')
        username = request.form.get('username')
        senha = request.form.get('senha')
        #Verificando se o usuário ja existe e retorna que o usuário ja está cadastrado
        if Usuario.query.filter_by(nomeDeUsuario=username).first():
            return render_template('Cadastro.html', fail=_("Usuário ja cadastrado"))
        #Gerando salt e hash, usando 10 rounds por conta de performance, de 10 pra 12 deu ~200ms de diferença no tempo de resposta
        salt = gensalt(rounds=10)
        senhaHash = hashpw(senha.encode('utf-8'), salt)
        #Criando objeto e executando o sql
        novoUsuario = Usuario(nome=nome, nomeDeUsuario=username,senha=senhaHash)
        db.session.add(novoUsuario)
        db.session.commit()
        return render_template('Login.html', success=_("Cadastro realizado com sucesso"))

    else:
        return render_template('Cadastro.html')
    

@usuario_bp.route('/admin', methods=['GET'])
def admin():
    return render_template('PainelAdmin.html')



@usuario_bp.route('/cancelar', methods=['POST'])
def cancelarReserva():
    pass