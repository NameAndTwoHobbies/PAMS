# DOMAIN MODELS
# buisness logic layer - domain models, these are the models used in the application, 
# they are not directly related to the database, but they can be used to transfer data between layers of the application. 
# They can also contain business logic and methods that operate on the data. 
# navigation properties - these are properties that reference other objects.

# object references 
# business rules
# calculations
# validation logic

from datetime import datetime
from typing import List, Optional

# Location
class Location:
    def __init__(self, location_id: int, name: str, manager: str):
        self.location_id = location_id
        self.name = name
        self.manager = manager
        self.apartments: List["Apartment"] = []
        self.staff: List["User"] = []

    def __repr__(self):
        return f"Location(id={self.location_id}, name='{self.name}', manager='{self.manager}')"

    def add_apartment(self, apartment: "Apartment"):
        self.apartments.append(apartment)

    def add_staff_member(self, user: "User"):
        self.staff.append(user)


# User (Staff / Workers / Admin)
class User:
    def __init__(self, user_id: int, first_name: str,
                 last_name: str, email: str,
                 role: str, location: Location):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role = role
        self.location = location
        self.availability: List["WorkerAvailability"] = []

    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.first_name} {self.last_name}', email='{self.email}', role='{self.role}', location='{self.location.name}')"

    def is_worker(self) -> bool:
        return self.role.lower() == "worker"

    def add_availability(self, availability: "WorkerAvailability"):
        self.availability.append(availability)


# Tenant
class Tenant:
    def __init__(self, tenant_id: int, first_name: str,
                 last_name: str, email: str, occupation = None, references = None):
        self.tenant_id = tenant_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.occupation = occupation
        self.references = references

        self.contracts: List["Contract"] = []
        self.maintenance_requests: List["MaintenanceRequest"] = []
        self.notifications: List["Notification"] = []

    def __repr__(self):
        return f"Tenant(id={self.tenant_id}, name='{self.first_name} {self.last_name}', email='{self.email}')"

    def get_active_contract(self) -> Optional["Contract"]:
        today = datetime.today().date()
        for contract in self.contracts:
            if contract.is_active(today):
                return contract
        return None

    def get_location(self) -> Optional["Location"]:
        active_contract = self.get_active_contract()
        if active_contract:
            return active_contract.apartment.location
        return None


# Apartment
class Apartment:
    def __init__(self, apartment_id: int, location: Location,
                 room_type: str, monthly_rent: float,
                 bedrooms: int, bathrooms: int,
                 occupied: bool):
        self.apartment_id = apartment_id
        self.location = location
        self.room_type = room_type
        self.monthly_rent = monthly_rent
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.occupied = occupied

        self.contracts: List["Contract"] = []
        self.maintenance_requests: List["MaintenanceRequest"] = []

    def __repr__(self):
        return f"Apartment(id={self.apartment_id}, location='{self.location.name}', room_type='{self.room_type}', monthly_rent={self.monthly_rent}, bedrooms={self.bedrooms}, bathrooms={self.bathrooms}, occupied={self.occupied})"

    def mark_occupied(self):
        self.occupied = True

    def mark_vacant(self):
        self.occupied = False


# Contract
class Contract:
    def __init__(self, contract_id: int,
                 apartment: Apartment,
                 tenant: Tenant,
                 start_date: datetime,
                 end_date: datetime,
                 payment_frequency: str,
                 early_leave: bool,
                 penalty_amount: float):

        self.contract_id = contract_id
        self.apartment = apartment
        self.tenant = tenant
        self.start_date = start_date
        self.end_date = end_date
        self.payment_frequency = payment_frequency
        self.early_leave = early_leave
        self.penalty_amount = penalty_amount

        self.payment_schedules: List["PaymentSchedule"] = []

    def __repr__(self):
        return f"Contract(id={self.contract_id}, apartment='{self.apartment.location.name} - {self.apartment.room_type}', tenant='{self.tenant.first_name} {self.tenant.last_name}', start_date='{self.start_date}', end_date='{self.end_date}', payment_frequency='{self.payment_frequency}', early_leave={self.early_leave}, penalty_amount={self.penalty_amount})"

    def is_active(self, today: datetime) -> bool:
        from datetime import datetime

        # Ensure start_date and end_date are datetime objects
        if isinstance(self.start_date, str):
            self.start_date = datetime.strptime(self.start_date, "%Y-%m-%d")
        if isinstance(self.end_date, str):
            self.end_date = datetime.strptime(self.end_date, "%Y-%m-%d")

        return self.start_date.date() <= today <= self.end_date.date()

    def calculate_penalty(self) -> float:
        if self.early_leave:
            return self.penalty_amount
        return 0.0


# Payment Schedule
class PaymentSchedule:
    def __init__(self, schedule_id: int,
                 contract: Contract,
                 due_date: datetime,
                 amount_due: float,
                 status: str):

        self.schedule_id = schedule_id
        self.contract = contract
        self.due_date = due_date
        self.amount_due = amount_due
        self.status = status

        self.payments: List["Payment"] = []
        self.invoice: Optional["Invoice"] = None

    def total_paid(self) -> float:
        return sum(payment.amount_paid for payment in self.payments)

    def is_fully_paid(self) -> bool:
        return self.total_paid() >= self.amount_due


# Payment
class Payment:
    def __init__(self, payment_id: int,
                 schedule: PaymentSchedule,
                 payment_date: datetime,
                 amount_paid: float,
                 payment_status: str,
                 method: str,
                 reference: str):

        self.payment_id = payment_id
        self.schedule = schedule
        self.payment_date = payment_date
        self.amount_paid = amount_paid
        self.payment_status = payment_status
        self.method = method
        self.reference = reference

    def is_successful(self) -> bool:
        return self.payment_status.lower() == "completed"


# Invoice
class Invoice:
    def __init__(self, invoice_id: int,
                 schedule: PaymentSchedule,
                 issued_date: datetime,
                 due_date: datetime,
                 amount: float,
                 status: str):

        self.invoice_id = invoice_id
        self.schedule = schedule
        self.issued_date = issued_date
        self.due_date = due_date
        self.amount = amount
        self.status = status

    def is_overdue(self) -> bool:
        return datetime.today() > self.due_date


# Maintenance Request
class MaintenanceRequest:
    def __init__(self, request_id: int,
                 tenant: Tenant,
                 apartment: Apartment,
                 description: str,
                 priority: str,
                 status: str,
                 scheduled_date: Optional[datetime],
                 resolved_date: Optional[datetime],
                 cost: float):

        self.request_id = request_id
        self.tenant = tenant
        self.apartment = apartment
        self.description = description
        self.priority = priority
        self.status = status
        self.scheduled_date = scheduled_date
        self.resolved_date = resolved_date
        self.cost = cost

        self.schedule: Optional["MaintenanceSchedule"] = None

    def is_resolved(self) -> bool:
        return self.status.lower() == "resolved"

    def resolution_time_hours(self) -> Optional[float]:
        if self.scheduled_date and self.resolved_date:
            delta = self.resolved_date - self.scheduled_date
            return delta.total_seconds() / 3600
        return None


# Maintenance Schedule
class MaintenanceSchedule:
    def __init__(self, schedule_id: int,
                 request: MaintenanceRequest,
                 assigned_worker: User,
                 scheduled_start: datetime,
                 scheduled_end: datetime):

        self.schedule_id = schedule_id
        self.request = request
        self.assigned_worker = assigned_worker
        self.scheduled_start = scheduled_start
        self.scheduled_end = scheduled_end

    def duration_hours(self) -> float:
        delta = self.scheduled_end - self.scheduled_start
        return delta.total_seconds() / 3600


# Worker Availability
class WorkerAvailability:
    def __init__(self, availability_id: int,
                 worker: User,
                 available_start: datetime,
                 available_end: datetime):

        self.availability_id = availability_id
        self.worker = worker
        self.available_start = available_start
        self.available_end = available_end

    def is_available_during(self, start: datetime, end: datetime) -> bool:
        return (self.available_start <= start and
                self.available_end >= end)


# Notification
class Notification:
    def __init__(self, notification_id: int,
                 tenant: Tenant,
                 type: str,
                 subject: str,
                 message: str,
                 is_read: bool,
                 created_at: datetime):

        self.notification_id = notification_id
        self.tenant = tenant
        self.type = type
        self.subject = subject
        self.message = message
        self.is_read = is_read
        self.created_at = created_at

    def mark_as_read(self):
        self.is_read = True

# Complaint
class Complaint:
    def __init__(self, complaint_id: int,
                 tenant: Tenant,
                 tenant_message: str,
                 created_at: datetime,
                 resolved_at: Optional[datetime]):

        self.complaint_id = complaint_id
        self.tenant = tenant
        self.tenant_message = tenant_message
        self.created_at = created_at
        self.resolved_at = resolved_at

    def is_resolved(self) -> bool:
        return self.resolved_at is not None