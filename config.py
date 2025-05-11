class Config:
    #Arquivo do SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///armarios.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #Linguagem padrão do Babel
    BABEL_DEFAULT_LOCALE = 'pt_BR'
    #Permite que outras linguagens suportadas sejam adicionadas facilmente
    LANGUAGES = ['pt_BR'] 
