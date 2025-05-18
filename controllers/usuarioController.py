from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_user, login_required, logout_user
from bcrypt import hashpw, gensalt, checkpw
from flask_babel import _
#Importando o pacote de models e o db
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
        #Comparando os hashes das senhas e se o usuário existe
        if busca and checkpw(senha.encode('utf-8'), busca.senha):
            #Função de login do flask-login
            login_user(busca)
            return redirect(url_for('index'))

        else:
            flash(_("Usuário ou senha inválidos"),'fail')
            return redirect(url_for('usuario.login'))

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
            flash(_("Usuário já cadastrado"),'fail')
            return redirect(url_for('usuario.cadastro'))
        #Gerando salt e hash, usando 10 rounds por conta de performance, de 10 pra 12 deu ~200ms de diferença no tempo de resposta
        salt = gensalt(rounds=10)
        senhaHash = hashpw(senha.encode('utf-8'), salt)
        #Criando objeto e executando o sql
        novoUsuario = Usuario(nome=nome, nomeDeUsuario=username,senha=senhaHash)
        db.session.add(novoUsuario)
        db.session.commit()
        flash(_("Cadastro realizado com sucesso"),'success')
        return redirect(url_for('usuario.login'))

    else:
        return render_template('Cadastro.html')
    

@usuario_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash(_("Você foi desconectado."), 'info')
    return redirect(url_for('index'))


@usuario_bp.route('/admin', methods=['GET'])
@login_required
def admin():
    armarios = Armario.query.all()
    capacidades = sorted({a.capacidade for a in armarios})
    locais = sorted({a.localizacao for a in armarios})
    disponibilidades = Disponibilidade.query.order_by(Disponibilidade.id).all()
    reservas = Reserva.query.all()
    return render_template('PainelAdmin.html',admin=True, reservas=reservas, armarios=armarios, capacidades=capacidades, locais=locais, disponibilidades=disponibilidades)



@usuario_bp.route('/cancelar', methods=['POST'])
def cancelarReserva():
    pass