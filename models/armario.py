from flask_sqlalchemy import SQLAlchemy
from models import db

class Armario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    localizacao = db.Column(db.String(50), nullable=False)
    capacidade = db.Column(db.String(15), nullable=False)
    disponibilidadeId = db.Column(db.Integer, db.ForeignKey('disponibilidade.id'), nullable=False, default=1)

    disponibilidade = db.relationship('Disponibilidade', backref='armario',lazy=True)
