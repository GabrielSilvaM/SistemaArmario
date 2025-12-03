from models.usuario import Usuario
from bcrypt import hashpw, gensalt

class UsuarioFactory:
    @staticmethod
    def create_usuario(nome, username, senha, admin=False):
        salt = gensalt(rounds=10)
        senhaHash = hashpw(senha.encode('utf-8'), salt)
        return Usuario(nome=nome, nomeDeUsuario=username, senha=senhaHash, admin=admin)
