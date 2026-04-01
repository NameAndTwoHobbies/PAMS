from models.domain_models import Contract
from .base_repository import BaseRepository
from datetime import datetime


class ContractRepository(BaseRepository):

    def get_by_tenant(self, tenant_id: int):
        query = "SELECT * FROM contracts WHERE tenant_id = %s"
        return self.fetch_all(query, (tenant_id,))