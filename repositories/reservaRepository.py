from repositories.baseRepository import BaseRepository
from models.reserva import Reserva

class ReservaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Reserva)

    def get_active_reservations(self):
        return self.model.query.filter(self.model.finalizada == False).all()
    
    def get_by_armario_id_and_active(self, armario_id):
        return self.model.query.filter(self.model.armarioId == armario_id, self.model.finalizada != True).all()

    def get_starting_today(self, date):
        return self.model.query.filter(self.model.inicio == date).all()

    def get_ending_before(self, date):
        return self.model.query.filter(self.model.fim < date).all()

    def get_conflicting_reservations(self, armario_id, start_date, end_date):
        return self.model.query.filter(
            self.model.armarioId == armario_id,
            self.model.inicio <= end_date,
            self.model.fim >= start_date
        ).all()

    def get_by_user_id_active(self, user_id):
        return self.model.query.filter(self.model.usuarioId == user_id, self.model.finalizada == False).all()
