import datetime

from models.Entities import MaintenanceRequest, User

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

    def mark_completed(self, request_id: int, completed_time: datetime):  
        query = """
        UPDATE maintenance_requests
        SET status = 'Completed', resolved_date = %s, time_taken = TIMESTAMPDIFF(MINUTE, scheduled_date, %s)
        WHERE request_id = %s
        """
        self.execute(query, (completed_time, completed_time,request_id))

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
    
    def get_maintenance_requests_by_worker(self, user_id: int):
        query = """
        SELECT 
            r.request_id,
            r.tenant_id,
            r.apartment_id,
            r.description,
            r.priority,
            r.status,
            r.maintenance_notes,
            s.scheduled_start,
            r.resolved_date,
            r.time_taken,
            r.cost
        FROM maintenance_scheduling s
        JOIN maintenance_requests r ON s.request_id = r.request_id
        WHERE s.user_id = %s;
        """

        requests = self.fetch_all(query, (user_id,))
        maintenanceRequests = []

        for r in requests:
            maintenanceRequests.append(
                MaintenanceRequest(
                    r['request_id'],
                    r['tenant_id'],
                    r['apartment_id'],
                    r['description'],
                    r['priority'],
                    r['status'],
                    r['maintenance_notes'],
                    r['scheduled_start'],  # maps to scheduled_date
                    r.get('resolved_date'),
                    r.get('time_taken'),
                    r['cost']
                )
            )

        return maintenanceRequests
    
    def update_maintenance_notes(self, request_id: int, notes: str):
        query = """
        UPDATE maintenance_requests
        SET maintenance_notes = %s
        WHERE request_id = %s
        """
        self.execute(query, (notes, request_id))

    def update_maintenance_cost(self, request_id: int, cost: float):
        query = """
        UPDATE maintenance_requests
        SET cost = %s
        WHERE request_id = %s
        """
        self.execute(query, (cost, request_id))