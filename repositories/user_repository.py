from models.domain_models import User, Location
from .base_repository import BaseRepository


class UserRepository(BaseRepository):

    def login_user(self, email, password_hash):
        query = "SELECT * FROM users WHERE email=%s AND password_hash=%s"
        row = self.fetch_one(query, (email, password_hash))
        if not row:
            return None

        location = Location(row["location_id"], "", "")
        return User(row["user_id"],
                    row["first_name"],
                    row["last_name"],
                    row["email"],
                    row["role"],
                    location)
    
    def login_maintenance_worker(self, email, password_hash):
        pass

    def get_available_workers(self, location_id, start, end):
        query = """
        SELECT u.*
        FROM users u
        JOIN worker_availability wa ON u.user_id = wa.user_id
        WHERE u.role = 'maintenance'
        AND u.location_id = %s
        AND wa.available_start <= %s
        AND wa.available_end >= %s
        AND wa.status = 'Available'
        """
        results = self.fetch_all(query, (location_id, start, end))
        return results or []
    
    def mark_as_booked(self, user_id):
        query = """
        UPDATE worker_availability
        SET status = 'Booked'
        WHERE user_id = %s
        """
        self.execute(query, (user_id,))