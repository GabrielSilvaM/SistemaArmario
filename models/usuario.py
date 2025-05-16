from flask_login import UserMixin
from models import db

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    nomeDeUsuario = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
