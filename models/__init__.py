from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .armario import Armario
from .disponibilidade import Disponibilidade
from .reserva import Reserva
from .usuario import Usuario

