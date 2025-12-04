from observers.observer import Observer
from flask_babel import _

class EmailLoggerObserver(Observer):
    def update(self, message):
        # Simula o envio de email logando no console
        print(f"[SIMULAÇÃO DE EMAIL] Notificação enviada: {message}")
