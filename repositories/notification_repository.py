from .base_repository import BaseRepository

class NotificationRepository(BaseRepository):

    def get_by_tenant(self, tenant_id: int):
        query = """
        SELECT * FROM notifications
        WHERE tenant_id = %s
        ORDER BY created_at DESC
        """
        return self.fetch_all(query, (tenant_id,))
    
    def fetch_notifications(self, tenant_id: int = None, location_id: int = None):
        query = """
        SELECT notification_id, subject, message, is_read, created_at
        FROM notifications
        """

        conditions = []
        params = []

        if tenant_id:
            conditions.append("tenant_id = %s")
            params.append(tenant_id)

        if location_id:
            conditions.append("location_id = %s")
            params.append(location_id)

        if conditions:
            query += " WHERE " + " OR ".join(conditions)
        else:
            return []

        query += " ORDER BY created_at DESC LIMIT 50"

        results = self.fetch_all(query, tuple(params))

        return results

    def mark_as_read(self, notification_id: int):
        query = """
        UPDATE notifications
        SET is_read = 1
        WHERE notification_id = %s
        """
        self.execute(query, (notification_id,))