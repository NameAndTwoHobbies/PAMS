from .base_repository import BaseRepository


class MaintenanceRepository(BaseRepository):

    def get_request_by_id(self, request_id: int):
        query = "SELECT * FROM maintenance_requests WHERE request_id = %s"
        return self.fetch_one(query, (request_id,))
    
    def get_pending_requests_by_location(self, location_id: int):
        query = """
        SELECT *
        FROM maintenance_requests
        WHERE status = 'pending' 
        AND apartment_id IN (
            SELECT apartment_id
            FROM apartments
            WHERE location_id = %s
        )
        ORDER BY priority DESC
        """
        return self.fetch_all(query, (location_id,))
    
    
    def create_request(self, tenant_id: int, apartment_id: int, description: str, priority: str, status: str = "Pending"):
        query = """
        INSERT INTO maintenance_requests (tenant_id, apartment_id, description, priority, status)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.execute(query, (tenant_id, apartment_id, description, priority, status))

    def mark_scheduled(self, request_id: int):
        query = """
        UPDATE maintenance_requests
        SET status = 'Scheduled'
        WHERE request_id = %s
        """
        self.execute(query, (request_id,))

    def mark_pending(self, request_id: int):
        query = """
        UPDATE maintenance_requests
        SET status = 'Pending'
        WHERE request_id = %s
        """
        self.execute(query, (request_id,))

    def mark_completed(self, request_id: int):  
        pass

    def cancel_scheduled_request(self, request_id: int):
        query = """
        DeletE FROM maintenance_requests
        WHERE request_id = %s
        """
        self.execute(query, (request_id,))


    def get_scheduled_requests_by_location(self, location_id: int):
        query = """
        SELECT 
            mr.request_id,
            mr.description,
            mr.priority,
            mr.status,
            ms.scheduled_start,
            ms.scheduled_end,
            u.firstName,
            u.lastName
        FROM maintenance_requests mr
        JOIN maintenance_scheduling ms 
            ON ms.request_id = mr.request_id
        JOIN users u 
            ON ms.user_id = u.user_id
        JOIN apartments a 
            ON mr.apartment_id = a.apartment_id
        WHERE mr.status = 'Scheduled'
        AND a.location_id = %s
        ORDER BY mr.priority DESC;
        """
        return self.fetch_all(query, (location_id,))