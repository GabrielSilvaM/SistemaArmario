from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_required, current_user
from flask_babel import _
#Importando o pacote de models e o db
from models import *
from datetime import datetime, date
from sqlalchemy.exc import SQLAlchemyError

reserva_bp = Blueprint('reserva',__name__)

@reserva_bp.route('/reservar', methods=['POST'])
@login_required
def reservarArmario():
    dataInicio = request.form.get('inicio')
    dataFim = request.form.get('fim')
    armarioId = request.form.get('armarioId')
    usuarioId = request.form.get('usuarioId')
    #Verifica se ha algum valor em todos os campos
    if not armarioId or not usuarioId or not dataInicio or not dataFim:
        flash(_("Houve um problema com a sua reserva, verifique os campos e tente novamente"),'fail')
        return redirect(url_for('armario.listarArmarios'))

    #Para previnir problemas com não administradores fazendo reservas para outros usuários
    if int(usuarioId) != current_user.id and current_user.admin == False:
        flash(_("Você só pode fazer reservas para o seu usuário"),'fail')
        return redirect(url_for('armario.listarArmarios'))


    #Convertendo string para datas, passar no formato YYYY-MM-DD
    #Tratando possíveis erros de formato
    try:    
        inicioDate = datetime.strptime(dataInicio, "%Y-%m-%d").date()
        fimDate = datetime.strptime(dataFim, "%Y-%m-%d").date()
        if inicioDate > fimDate:
            flash(_("A data de início deve vir antes, selecione novamente as datas"),'fail')
            return redirect(url_for('armario.listarArmarios'))

    except ValueError as e:
        flash(_(f"Erro na conversão de datas {e}"),'fail')
        return redirect(url_for('armario.listarArmarios'))
    


    reservasConflitantes = Reserva.query.filter(
                                                    Reserva.armarioId == armarioId,
                                                    Reserva.inicio <= fimDate,
                                                    Reserva.fim >= inicioDate
                                                ).all()

    if reservasConflitantes:
        datasConflitantes = [f"{r.inicio} até {r.fim}" for r in reservasConflitantes]
        textoConflitos = "<br>".join(datasConflitantes)

        fail = _(f"Existem uma ou mais reservas conflitantes com o período desejado:<br>{textoConflitos}")

        flash(fail,'fail')
        return redirect(url_for('armario.listarArmarios'))

    #Instanciando um objeto para inserir a reserva
    novaReserva = Reserva(inicio=inicioDate, fim=fimDate, armarioId= armarioId, usuarioId=usuarioId)
    #Try Except para garantir que as alterações não sejam feitas pela metade, com um rollback em caso de erros do SQLAlchemy
    try:
        db.session.add(novaReserva)
        armario = Armario.query.get(armarioId)
        
        #Checa se a reserva ja inicia no dia que foi feita e muda o status do armário
        if inicioDate == date.today():
            armario.disponibilidadeId=2
        #Verifica se o armário está disponível no dia, para não marcar como reservado acidentalmente
        elif armario.disponibilidadeId == 1:
            armario.disponibilidadeId = 3
            
        db.session.commit()
        flash(_("Reserva feita com sucesso!"),'success')
        return redirect(url_for('armario.listarArmarios'))
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(_(f"Houve um problema com a sua reserva, tente novamente :{e}"),'fail')
        return redirect(url_for('armario.listarArmarios'))
        
    
@reserva_bp.route('/reservas')
@login_required
def listarReservas():
    reservas = Reserva.query.filter(Reserva.usuarioId == current_user.id, Reserva.finalizada == False).all()
    return render_template('Reservas.html', reservas=reservas)

@reserva_bp.route('/editar', methods=['POST'])
@login_required
def editarReserva():
    reservaId = request.form.get('reservaId')
    reserva = db.session.get(Reserva, reservaId)
    #Para previnir problemas com não administradores editando reservas de outros usuários
    if reserva.usuario.id != current_user.id and current_user.admin == False:
        flash(_("Você só pode alterar reservas feitas por você"),'fail')
        return redirect(url_for('reserva.listarReservas'))

    if request.form.get('opcao') == 'cancelar':
        #Buscando a reserva pelo id do formulário e deletando do banco
        armarioId = reserva.armarioId
        #Checa se é a ultima reserva desse armário e o marca como disponível caso seja
        reservasRestantes = Reserva.query.filter(Reserva.armarioId == armarioId, Reserva.finalizada == False).all()
        if len(reservasRestantes) <= 1:
            armarioDisponivel = db.session.get(Armario, armarioId)
            armarioDisponivel.disponibilidadeId = 1

        reserva.finalizada = True
        db.session.commit()

        flash(_("Sua reserva foi cancelada com sucesso"),'success')
        return redirect(url_for('reserva.listarReservas'))
    elif request.form.get('opcao') == 'editar':
        #Atribuindo novos valores ao inicio e fim da reserva
        inicio = request.form.get('inicio')
        fim = request.form.get('fim')
        try:    
            inicioDate = datetime.strptime(inicio, "%Y-%m-%d").date()
            fimDate = datetime.strptime(fim, "%Y-%m-%d").date()
            if inicioDate > fimDate:
                flash(_("A data de início deve vir antes, selecione novamente as datas"),'fail')
                return redirect(url_for('reserva.reservas'))

        except ValueError as e:
            flash(_(f"Erro na conversão de datas {e}"),'fail')
            return redirect(url_for('reserva.reservas'))

        reserva.inicio = inicioDate
        reserva.fim = fimDate

        db.session.commit()

        flash(_("Sua reserva foi alterada com sucesso"),'success')
        return redirect(url_for('reserva.listarReservas'))
    else:
        flash(_("Requisição inválida"),'fail')
        return redirect(url_for('reserva.listarReservas'))