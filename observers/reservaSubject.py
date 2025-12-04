from observers.subject import Subject

class ReservaSubject(Subject):
    def nova_reserva(self, reserva):
        message = f"Nova reserva criada: ID {reserva.id}, Armário {reserva.armarioId}, Usuário {reserva.usuarioId}"
        self.notify(message)
