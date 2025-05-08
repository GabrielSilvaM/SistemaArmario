from flask_sqlalchemy import SQLAlchemy
from models import db

class Disponibilidade(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    descricao = db.Column(db.String(20), nullable=False)
