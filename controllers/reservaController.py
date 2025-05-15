from flask import render_template, request, redirect, url_for, Blueprint
from flask_babel import _
#Importante o pacote de models e o db
from models import *
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

reserva_bp = Blueprint('reserva',__name__)

@reserva_bp.route('/reservar', methods=['POST'])
def reservarArmario():
    dataInicio = request.form.get('inicio')
    dataFim = request.form.get('fim')
    armarioId = request.form.get('armarioId')
    usuarioId = request.form.get('usuarioId')
    #Convertendo string para datas, passar no formato YYYY-MM-DD
    #tratando possíveis erros de formato
    try:    
        inicioDate = datetime.strptime(dataInicio, "%Y-%m-%d").date()
        fimDate = datetime.strptime(dataFim, "%Y-%m-%d").date()

    except ValueError as e:
        return render_template("ListarArmarios.html", fail=_("Data em formato inválido, contate o suporte"))
    


    reservasConflitantes = Reserva.query.filter(
                                                    Reserva.armarioId == armarioId,
                                                    Reserva.inicio <= fimDate,
                                                    Reserva.fim >= inicioDate
                                                ).all()

    if reservasConflitantes:
        datasConflitantes = [f"{r.inicio} até {r.fim}" for r in reservasConflitantes]
        textoConflitos = "<br>".join(datasConflitantes)

        fail = _(f"Existem uma ou mais reservas conflitantes com o período desejado:<br>{textoConflitos}")

        return render_template("ListarArmarios.html", fail=fail)
    
    #Instanciando um objeto para inserir a reserva
    novaReserva = Reserva(inicio=inicioDate, fim=fimDate, armarioId= armarioId, usuarioId=usuarioId)
    #Try Except para garantir que as alterações não sejam feitas pela metade, com um rollback em caso de erros do SQLAlchemy
    try:
        db.session.add(novaReserva)
        armario = Armario.query.get(armarioId)
        #Checa se o armário foi encontrado
        if armario:
            armario.disponibilidadeId = 3
        else:
            raise SQLAlchemyError(_("Armário não encontrado"))
        db.session.commit()
        return render_template("ListarArmarios.html", success=_("Reserva feita com sucesso!"))
    except SQLAlchemyError as e:
        db.session.rollback()
        return render_template("ListarArmarios.html", fail=e)
        
    
