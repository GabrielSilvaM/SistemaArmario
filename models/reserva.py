from flask_sqlalchemy import SQLAlchemy
from models import db

class Reserva(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    inicio = db.Column(db.Date, nullable=False)
    fim = db.Column(db.Date, nullable=False)
    armarioId = db.Column(db.Integer,db.ForeignKey('armario.id'), nullable=False)
    usuarioId = db.Column(db.Integer,db.ForeignKey('usuario.id'), nullable=False)

    armario = db.relationship('Armario', backref='reserva',lazy=True)
    usuario = db.relationship('Usuario', backref='reserva',lazy=True)