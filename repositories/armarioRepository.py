from repositories.baseRepository import BaseRepository
from models.armario import Armario

class ArmarioRepository(BaseRepository):
    def __init__(self):
        super().__init__(Armario)
