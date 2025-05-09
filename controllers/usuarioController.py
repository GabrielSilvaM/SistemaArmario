from flask import render_template, request, redirect, url_for

class UsuarioController:
    @staticmethod
    def login():
        return render_template('PainelPrincipal.html')

    @staticmethod
    def cadastro():
        return render_template('VisualizacaoDeArmario.html')