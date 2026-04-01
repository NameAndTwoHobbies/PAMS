from models.domain_models import Location
from .base_repository import BaseRepository

class LocationRepository(BaseRepository):

    def get_by_name(self, name: str):
        query = "SELECT * FROM locations WHERE location_name = %s"
        row = self.fetch_one(query, (name,))
        if not row:
            return None
        return Location(row["location_id"],
                        row["location_name"],
                        row["location_manager"])

    def get_all(self):
        query = "SELECT * FROM locations"
        rows = self.fetch_all(query)
        return [Location(r["location_id"],
                         r["location_name"],
                         r["location_manager"])
                for r in rows]