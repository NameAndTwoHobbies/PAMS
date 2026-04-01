# DATABASE MODELS
# database layer - data models for each table in the database, 
# dto - data transfer object, used to transfer data between layers of the application.
# to_tuple method replaces the GetDataBaseFormat method.

# Users
class UserDTO:
    def __init__(self, user_id: int, first_name: str, last_name: str,
                 email: str, password_hash: str, role: str, location_id: int):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.location_id = location_id

    def to_tuple(self):
        return (self.user_id, self.first_name, self.last_name,
                self.email, self.password_hash, self.role, self.location_id)


# Tenants
class TenantDTO:
    def __init__(self, tenant_id: int, first_name: str, last_name: str,
                 national_insurance: str, email: str,
                 password_hash: str, phone_number: str, occupation: str, refererences: str):
        self.tenant_id = tenant_id
        self.first_name = first_name
        self.last_name = last_name
        self.national_insurance = national_insurance
        self.email = email
        self.password_hash = password_hash
        self.phone_number = phone_number
        self.occupation = occupation
        self.refererences = refererences

    def to_tuple(self):
        return (self.tenant_id, self.first_name, self.last_name,
                self.national_insurance, self.email,
                self.password_hash, self.phone_number, self.occupation)
    
    def GetID(self):
        return self.tenant_id


# Locations
class LocationDTO:
    def __init__(self, location_id: int, location_name: str, location_manager: str):
        self.location_id = location_id
        self.location_name = location_name
        self.location_manager = location_manager

    def to_tuple(self):
        return (self.location_id, self.location_name, self.location_manager)


# Apartments
class ApartmentDTO:
    def __init__(self, apartment_id: int, location_id: int,
                 room_type: str, monthly_rent: float,
                 bedrooms: int, bathrooms: int,
                 occupancy_status: bool):
        self.apartment_id = apartment_id
        self.location_id = location_id
        self.room_type = room_type
        self.monthly_rent = monthly_rent
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.occupancy_status = occupancy_status

    def to_tuple(self):
        return (self.apartment_id, self.location_id,
                self.room_type, self.monthly_rent,
                self.bedrooms, self.bathrooms,
                self.occupancy_status)


# Contracts
class ContractDTO:
    def __init__(self, contract_id: int, apartment_id: int, tenant_id: int,
                 start_date: str, end_date: str,
                 payment_frequency: str,
                 early_leave: bool, penalty_amount: float):
        self.contract_id = contract_id
        self.apartment_id = apartment_id
        self.tenant_id = tenant_id
        self.start_date = start_date
        self.end_date = end_date
        self.payment_frequency = payment_frequency
        self.early_leave = early_leave
        self.penalty_amount = penalty_amount

    def to_tuple(self):
        return (self.contract_id, self.apartment_id, self.tenant_id,
                self.start_date, self.end_date,
                self.payment_frequency,
                self.early_leave, self.penalty_amount)


# Payment Schedules
class PaymentScheduleDTO:
    def __init__(self, schedule_id: int, contract_id: int,
                 due_date: str, amount_due: float, status: str):
        self.schedule_id = schedule_id
        self.contract_id = contract_id
        self.due_date = due_date
        self.amount_due = amount_due
        self.status = status

    def to_tuple(self):
        return (self.schedule_id, self.contract_id,
                self.due_date, self.amount_due, self.status)


# Payments
class PaymentDTO:
    def __init__(self, payment_id: int, schedule_id: int,
                 tenant_id: int, location_id: int,
                 payment_date: str, amount_paid: float,
                 payment_status: str, method: str, reference: str):
        self.payment_id = payment_id
        self.schedule_id = schedule_id
        self.tenant_id = tenant_id
        self.location_id = location_id
        self.payment_date = payment_date
        self.amount_paid = amount_paid
        self.payment_status = payment_status
        self.method = method
        self.reference = reference

    def to_tuple(self):
        return (self.payment_id, self.schedule_id,
                self.tenant_id, self.location_id,
                self.payment_date, self.amount_paid,
                self.payment_status, self.method, self.reference)


# Invoices
class InvoiceDTO:
    def __init__(self, invoice_id: int,
                 contract_id: int, schedule_id: int,
                 issued_date: str, due_date: str,
                 amount: float, status: str):
        self.invoice_id = invoice_id
        self.contract_id = contract_id
        self.schedule_id = schedule_id
        self.issued_date = issued_date
        self.due_date = due_date
        self.amount = amount
        self.status = status

    def to_tuple(self):
        return (self.invoice_id, self.contract_id, self.schedule_id,
                self.issued_date, self.due_date,
                self.amount, self.status)


# Maintenance Requests
class MaintenanceRequestDTO:
    def __init__(self, request_id: int, tenant_id: int,
                 apartment_id: int, description: str,
                 priority: str, status: str,
                 maintenance_notes: str,
                 scheduled_date: str, resolved_date: str,
                 cost: float):
        self.request_id = request_id
        self.tenant_id = tenant_id
        self.apartment_id = apartment_id
        self.description = description
        self.priority = priority
        self.status = status
        self.maintenance_notes = maintenance_notes
        self.scheduled_date = scheduled_date
        self.resolved_date = resolved_date
        self.cost = cost

    def to_tuple(self):
        return (self.request_id, self.tenant_id,
                self.apartment_id, self.description,
                self.priority, self.status,
                self.maintenance_notes,
                self.scheduled_date,
                self.resolved_date, self.cost)


# Maintenance Schedules
class MaintenanceScheduleDTO:
    def __init__(self, schedule_id: int, request_id: int,
                 user_id: int, scheduled_start: str, scheduled_end: str):
        self.schedule_id = schedule_id
        self.request_id = request_id
        self.user_id = user_id
        self.scheduled_start = scheduled_start
        self.scheduled_end = scheduled_end

    def to_tuple(self):
        return (self.schedule_id, self.request_id,
                self.user_id, self.scheduled_start,
                self.scheduled_end)


# Worker Availability
class WorkerAvailabilityDTO:
    def __init__(self, availability_id: int, user_id: int,
                 available_start: str, available_end: str):
        self.availability_id = availability_id
        self.user_id = user_id
        self.available_start = available_start
        self.available_end = available_end

    def to_tuple(self):
        return (self.availability_id, self.user_id,
                self.available_start, self.available_end)


# Notifications
class NotificationDTO:
    def __init__(self, notification_id: int, tenant_id: int,
                 type: str, subject: str,
                 message: str, is_read: bool,
                 created_at: str):
        self.notification_id = notification_id
        self.tenant_id = tenant_id
        self.type = type
        self.subject = subject
        self.message = message
        self.is_read = is_read
        self.created_at = created_at

    def to_tuple(self):
        return (self.notification_id, self.tenant_id,
                self.type, self.subject,
                self.message, self.is_read,
                self.created_at)

# Complaints
class ComplaintDTO:
    def __init__(self, complaint_id: int, tenant_id: int,
                tenant_message: str, created_at: str, resolved_at: str):
        self.complaint_id = complaint_id
        self.tenant_id = tenant_id
        self.tenant_message = tenant_message
        self.created_at = created_at
        self.resolved_at = resolved_at

    def to_tuple(self):
        return (self.complaint_id, self.tenant_id,
                self.apartment_id, self.description,
                self.status, self.resolution_notes,
                self.created_at, self.resolved_at)