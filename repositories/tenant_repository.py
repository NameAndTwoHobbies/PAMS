from models.Entities import *
from models.db_models import TenantDTO
from .base_repository import BaseRepository


class TenantRepository(BaseRepository):

    def get_all(self):
        records = self.fetch_all("SELECT * FROM tenants")
        tenants = []
        for record in records:
            tenants.append(TenantDTO(
                record["tenant_id"],
                record["first_name"],
                record["last_name"],
                record["national_insurance"],
                record["email"],
                record["password"],
                record["phone_number"],
                record["occupation"],
                record["references"]
            ))
        return tenants

    def get_by_email(self, email: str):
        query = "SELECT * FROM tenants WHERE email = %s"
        row = self.fetch_one(query, (email,))
        if not row:
            return None
        return Tenant(row["tenant_id"],
                      row["first_name"],
                      row["last_name"],
                      row["email"])

    def create(self, tenant):
        query = """
        INSERT INTO tenants
        (first_name, last_name, national_insurance,
         email, password_hash, phone_number, occupation)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        self.execute(query, (
            tenant.first_name,
            tenant.last_name,
            tenant.national_insurance,
            tenant.email,
            tenant.password_hash,
            tenant.phone_number,
            tenant.occupation
        ))