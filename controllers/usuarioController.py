from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_user, login_required, logout_user
from bcrypt import checkpw
from flask_babel import _
from models import *
from repositories.usuarioRepository import UsuarioRepository
from repositories.armarioRepository import ArmarioRepository
from repositories.reservaRepository import ReservaRepository
from repositories.baseRepository import BaseRepository
from factories.usuarioFactory import UsuarioFactory

usuario_repository = UsuarioRepository()
armario_repository = ArmarioRepository()
reserva_repository = ReservaRepository()
disponibilidade_repository = BaseRepository(Disponibilidade)

usuario_bp = Blueprint('usuario',__name__)


@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Pegando os dados do formulário
        username = request.form.get('username')
        senha = request.form.get('senha')
        #Verificando se o usuário está cadastrado
        busca = usuario_repository.get_by_username(username)
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
        if usuario_repository.get_by_username(username):
            flash(_("Usuário já cadastrado"),'fail')
            return redirect(url_for('usuario.cadastro'))
        
        #Criando objeto usando Factory
        novoUsuario = UsuarioFactory.create_usuario(nome, username, senha)
        usuario_repository.add(novoUsuario)
        
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
    armarios = armario_repository.get_all()
    capacidades = sorted({a.capacidade for a in armarios})
    locais = sorted({a.localizacao for a in armarios})
    disponibilidades = disponibilidade_repository.get_all()
    reservas = reserva_repository.get_active_reservations()
    return render_template('PainelAdmin.html',admin=True, reservas=reservas, armarios=armarios, capacidades=capacidades, locais=locais, disponibilidades=disponibilidades)



@usuario_bp.route('/cancelar', methods=['POST'])
def cancelarReserva():
    pass