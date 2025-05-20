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
    
    #Configurações do agendador
    SCHEDULER_API_ENABLED = False
    SCHEDULER_TIMEZONE = 'America/Sao_Paulo'

    #Configurações para backup diário
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    INSTANCE_DIR = os.path.join(BASEDIR, 'instance')
    DATABASE_FILE = os.path.join(INSTANCE_DIR, 'armarios.db')
    BACKUP_DIR = os.path.join(INSTANCE_DIR, 'backups')