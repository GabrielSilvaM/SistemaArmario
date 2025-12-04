from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_babel import _
from flask_login import login_required
from models import *
from repositories.armarioRepository import ArmarioRepository
from repositories.baseRepository import BaseRepository

armario_bp = Blueprint('armario',__name__)

armario_repository = ArmarioRepository()
disponibilidade_repository = BaseRepository(Disponibilidade)

@armario_bp.route('/add', methods=['POST'])
@login_required
def adicionarArmario():
    capacidade = request.form.get('capacidade')
    localizacao = request.form.get('localizacao')
    armario_repository.add(Armario(capacidade=capacidade,localizacao=localizacao))
    flash(_("Armário cadastrado com sucesso"), 'success')
    return redirect(url_for('usuario.admin'))

@armario_bp.route('/editararmario', methods=['POST'])
@login_required
def editarArmario():
    pass

@armario_bp.route('/list')
@login_required
def listarArmarios():
    armarios = armario_repository.get_all()
    capacidades = sorted({a.capacidade for a in armarios})
    locais = sorted({a.localizacao for a in armarios})
    disponibilidades = disponibilidade_repository.get_all()
    return render_template('ListarArmarios.html', armarios=armarios,
                           capacidades=capacidades,
                           locais=locais,
                           disponibilidades=disponibilidades)