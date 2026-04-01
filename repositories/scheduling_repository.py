from .base_repository import BaseRepository

class SchedulingRepository(BaseRepository):

    def create(self, request_id, user_id, scheduled_start, scheduled_end):
        query = """
        INSERT INTO maintenance_scheduling (request_id, user_id, scheduled_start, scheduled_end)
        VALUES (%s, %s, %s, %s)
        """
        self.execute(query, (request_id, user_id, scheduled_start, scheduled_end))

    def get_by_request_id(self, request_id):
        query = """
        SELECT * FROM maintenance_scheduling
        WHERE request_id = %s
        """
        return self.fetch_one(query, (request_id,))
    
    def get_available_workers(self, location_id, start, end):

        query = """
        SELECT u.user_id, u.firstName, u.lastName
        FROM users u
        JOIN worker_availability wa ON u.user_id = wa.user_id
        WHERE u.role = 'maintenance'
        AND u.location_id = %s

        -- availability window
        AND wa.available_start <= %s
        AND wa.available_end >= %s

        -- prevent overlapping jobs
        AND NOT EXISTS (
            SELECT 1
            FROM maintenance_scheduling ms
            WHERE ms.user_id = u.user_id
            AND (
                ms.scheduled_start < %s
                AND ms.scheduled_end > %s
            )
        )
        """

        return self.fetch_all(query, (location_id, start, end, start, end))
    
    def delete_by_request_id(self, request_id):
        query = """
        DELETE FROM maintenance_scheduling
        WHERE request_id = %s
        """
        self.execute(query, (request_id,))
