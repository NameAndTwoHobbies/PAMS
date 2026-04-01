from .base_repository import BaseRepository


class PaymentRepository(BaseRepository):

    def get_by_schedule(self, schedule_id: int):
        query = "SELECT * FROM payments WHERE schedule_id = %s"
        return self.fetch_all(query, (schedule_id,))