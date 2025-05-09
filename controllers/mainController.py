from flask import render_template

class MainController:
    @staticmethod
    def index():
        return render_template('PaginaInicial.html')