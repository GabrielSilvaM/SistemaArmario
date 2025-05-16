from dotenv import load_dotenv
import os

class Config:
    #Arquivo do SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///armarios.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #Linguagem padrão do Babel
    BABEL_DEFAULT_LOCALE = 'pt_BR'
    #Permite que outras linguagens suportadas sejam adicionadas facilmente
    LANGUAGES = ['pt_BR'] 


    load_dotenv()
    SECRET_KEY = os.environ.get("SECRET_KEY")

    if not SECRET_KEY:
        raise ValueError("Chave secreta faltando! Verifique o .env")
