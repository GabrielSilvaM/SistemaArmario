from repositories.baseRepository import BaseRepository
from models.usuario import Usuario

class UsuarioRepository(BaseRepository):
    def __init__(self):
        super().__init__(Usuario)

    def get_by_username(self, username):
        return self.model.query.filter_by(nomeDeUsuario=username).first()
