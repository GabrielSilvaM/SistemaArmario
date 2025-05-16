from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_required
from flask_babel import _
#Importante o pacote de models e o db
from models import *
from datetime import datetime
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
        #Checa se o armário foi encontrado
    
        armario.disponibilidadeId = 3
        db.session.commit()
        flash(_("Reserva feita com sucesso!"),'success')
        return redirect(url_for('armario.listarArmarios'))
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(_("Houve um problema com a sua reserva, tente novamente"),'fail')
        return redirect(url_for('armario.listarArmarios'))
        
    
