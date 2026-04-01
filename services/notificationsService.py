from repositories.notification_repository import NotificationRepository
from database.db_connection import DatabaseConnection
from repositories.tenant_repository import TenantRepository
from repositories.user_repository import UserRepository

class NotificationService:

    def __init__(self, tenant_id, location_id):
        self.tenant_id = tenant_id
        self.location_id = location_id
        self.last_notification_id = 0
        db_connection = DatabaseConnection()
        self.notification_repo = NotificationRepository(db_connection)
        self.tenant_repo = TenantRepository(db_connection)
        self.user_repo = UserRepository(db_connection)

    def get_notifications(self, personal, public):

        tenant = self.tenant_id if personal else None
        location = self.location_id if public else None

        notifications = self.notification_repo.fetch_notifications(tenant, location)

        return notifications

    def mark_as_read(self, notification_id):
        self.notification_repo.mark_as_read(notification_id)

    def send_notification(self, tenant_id, notif_type, message, is_read, created_at, location_id, subject):
        self.notification_repo.create(tenant_id, notif_type, message, is_read, created_at, location_id, subject)
    
    def get_tenants_by_location(self, location_id):
        return self.tenant_repo.get_by_location_for_notifs(location_id)
    
    def send_notification(self, tenant_id, notif_type, message, is_read, created_at, location_id, subject):
        return self.notification_repo.create(tenant_id, notif_type, message, is_read, created_at, location_id, subject)
    
    def get_location_name(self, location_id):
        return self.user_repo.get_location_name_from_id(location_id)