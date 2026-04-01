import datetime

from database.db_connection import DatabaseConnection
from repositories.maintenance_repository import MaintenanceRepository
from repositories.scheduling_repository import SchedulingRepository
from repositories.user_repository import UserRepository
from repositories.tenant_repository import TenantRepository

class MaintenanceService:
    def __init__(self):
        db_connection = DatabaseConnection()
        self.maintenance_repo = MaintenanceRepository(db_connection)
        self.scheduling_repo = SchedulingRepository(db_connection)
        self.user_repo = UserRepository(db_connection)
        self.tenant_repo = TenantRepository(db_connection)
    
    def get_pending_requests(self, current_user):
        return self.maintenance_repo.get_pending_requests_by_location(location_id=current_user.location_id)
    
    def get_request_details(self, request_id):
        return self.maintenance_repo.get_request_by_id(request_id)

    def get_available_workers(self, start, end, current_user):
        return self.user_repo.get_available_workers(location_id=current_user.location_id, start=start, end=end)

    def assign_worker_to_request(self, request_id, worker_id, start, end):

        self.scheduling_repo.create(
            request_id=request_id,
            user_id=worker_id,
            scheduled_start=start,
            scheduled_end=end
        )
        self.maintenance_repo.mark_scheduled(request_id)
        self.user_repo.mark_as_booked(worker_id)

        return
    
    def see_scheduled_requests(self, location_id):
        return self.maintenance_repo.get_scheduled_requests_by_location(location_id=location_id)
    
    def cancel_scheduled_request(self, request_id):
        self.scheduling_repo.delete_by_request_id(request_id)
        self.maintenance_repo.cancel_scheduled_request(request_id)

    def reshedule_request(self, request_id, worker_id, start, end):
        self.scheduling_repo.delete_by_request_id(request_id)
        self.maintenance_repo.mark_pending(request_id)
        self.scheduling_repo.create(
            request_id=request_id,
            user_id=worker_id,
            scheduled_start=start,
            scheduled_end=end
        )
        self.maintenance_repo.mark_scheduled(request_id)
        self.user_repo.mark_as_booked(worker_id)

    def get_maintenance_requests_by_worker(self, user_id):
        return self.maintenance_repo.get_maintenance_requests_by_worker(user_id)
    
    def complete_maintenance_request(self, request_id):
        completed_time = datetime.datetime.now()
        self.maintenance_repo.mark_completed(request_id, completed_time)
    
    def update_notes(self, request_id, notes):
        self.maintenance_repo.update_maintenance_notes(request_id, notes)

    def update_cost(self, request_id, cost):
        self.maintenance_repo.update_maintenance_cost(request_id, cost)

    def get_tenants(self):
        return self.tenant_repo.get_all()
