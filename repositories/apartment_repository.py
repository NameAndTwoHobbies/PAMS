from models.domain_models import Apartment, Location
from .base_repository import BaseRepository


class ApartmentRepository(BaseRepository):

    def get_by_location(self, location_id: int):
        query = "SELECT * FROM apartments WHERE location_id = %s"
        rows = self.fetch_all(query, (location_id,))
        apartments = []

        for r in rows:
            location = Location(location_id, "", "")
            apartments.append(
                Apartment(
                    r["apartment_id"],
                    location,
                    r["room_type"],
                    r["monthly_rent"],
                    r["bedrooms"],
                    r["bathrooms"],
                    r["occupancy_status"]
                )
            )
        return apartments

    def get_unoccupied(self, location_id: int):
        query = """
        SELECT * FROM apartments
        WHERE location_id = %s AND occupancy_status = 0
        """
        return self.fetch_all(query, (location_id,))