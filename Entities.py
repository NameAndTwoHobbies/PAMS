class IEntity:
    def __init__(self, id : str):
        self.id = id
    def GetID(self):
        return self.id
    def GetDataBaseFormat(self):
        pass
    def NumberOfFields(self):
        pass

#region Apartment
class Apartment(IEntity):
    def __init__(self, id : str, location_id : str, room_type : str, monthly_rent : str, bedrooms : str, bathrooms: str,occupancy_status : bool):
        super().__init__(id)
        self.location_id = location_id
        self.room_type = room_type
        self.monthly_rent = monthly_rent
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.occupancy_status = occupancy_status
        self.location_id = location_id
        self.room_type = room_type
        self.monthly_rent = monthly_rent
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.occupancy_status = occupancy_status

    def GetDataBaseFormat(self):
        return (self.id,self.location_id, self.room_type, self.monthly_rent, self.bedrooms, self.bathrooms, self.occupancy_status)
    def NumberOfFields(self):
        return 7
#endregion

#region Location
class Location(IEntity):
    def __init__(self, id : str, location_name : str, location_manager : str):
        super().__init__(id)
        self.location_name = location_name
        self.location_manager = location_manager
    
    def GetDataBaseFormat(self):
        return (self.id,self.location_name, self.location_manager)
    def NumberOfFields(self):
        return 3

#endregion

#region Complaint
class Complaint(IEntity):
    def __init__(self, id : str, tenant_id : str, tenant_message : str, created_at : str, resolved_at : str):
        super().__init__(id)
        self.tenant_id = tenant_id
        self.tenant_message = tenant_message
        self.creationDate = created_at
        self.resolveDate = resolved_at

    def GetDataBaseFormat(self):
        return (self.id, self.tenant_id, self.tenant_message, self.creationDate, self.resolveDate)
    def NumberOfFields(self):
        return 5
#endregion

#region Contract
class Contract(IEntity):
    def __init__(self, id : str, apartment_id : str, tenant_id : str, start_date :str, end_date : str, payment_frequency : str, early_leave : bool, penalty_amount : str):
        super().__init__(id)
        self.apartment_id = apartment_id
        self.tenant_id = tenant_id
        self.start_date = start_date
        self.end_date = end_date
        self.payment_frequency = payment_frequency
        self.early_leave = early_leave
        self.penalty_amount = penalty_amount

    def GetDataBaseFormat(self):
        return (self.id, self.apartment_id, self.tenant_id, self.start_date, self.end_date, self.payment_frequency, self.early_leave, self.penalty_amount)
    def NumberOfFields(self):
        return 8
#endregion

#region Invoice
class Invoice(IEntity):
    def __init__(self, id : str, contract_id : str, schedule_id : str, issued_date : str , due_date : str,  amount : str, status : str):
        super().__init__(id)
        self.contract_id = contract_id
        self.schedule_id = schedule_id
        self.issued_date = issued_date
        self.due_date = due_date
        self.amount = amount
        self.status = status

    def GetDataBaseFormat(self):
        return (self.id, self.contract_id, self.schedule_id, self.issued_date, self.due_date, self.amount, self.status)
    
    def NumberOfFields(self):
        return 7
#endregion

#region MaintenanceRequest
class MaintenanceRequest(IEntity):
    def __init__(self, id : str, tenant_id : str, apartment_id : str, description : str, priority : str, status : str, maintenance_notes : str, scheduled_date : str, resolved_date : str, time_taken :str, cost : str):
        super().__init__(id)
        self.tenant_id = tenant_id
        self.apartment_id = apartment_id
        self.description = description
        self.priority = priority
        self.status = status
        self.maintenance_notes = maintenance_notes
        self.scheduled_date = scheduled_date
        self.resolved_date = resolved_date
        self.time_taken = time_taken
        self.cost = cost
    def GetDataBaseFormat(self):
        return (self.id, self.tenant_id, self.apartment_id, self.description, self.priority, self.status, self.maintenance_notes, self.scheduled_date, self.resolved_date, self.time_taken, self.cost)
    def NumberOfFields(self):
        return 11
#endregion

#region MaintanenceSchedule
class MaintanenceSchedule(IEntity):
    def __init__(self, id : str, request_id : str, user_id : str, scheduled_start : str, scheduled_end : str):
        super().__init__(id)
        self.request_id = request_id
        self.user_id = user_id
        self.scheduled_start = scheduled_start
        self.scheduled_end = scheduled_end
    def GetDataBaseFormat(self):
        return (self.id, self.request_id, self.user_id, self.scheduled_start, self.scheduled_end)
    def NumberOfFields(self):
        return 5
#endregion



#region Notification
class Notification(IEntity):
    def __init__(self, id : str, tenant_id : str, type : str, message : str, is_read : bool, created_at : str):
        super().__init__(id)
        self.tenant_id = tenant_id
        self.type = type
        self.message = message
        self.is_read = is_read
        self.created_at = created_at

    def GetDataBaseFormat(self):
        return (self.id, self.tenant_id, self.type, self.message, self.is_read, self.created_at)
    
    def NumberOfFields(self):
        return 6
#endregion

#region Payment

class Payment(IEntity):
    def __init__(self, id : str, schedule_id : str, tenant_id : str, location_id :str , payment_date : str, amount_paid : str, payment_status : str, method : str, reference : str):
        super().__init__(id)
        self.schedule_id = schedule_id
        self.tenant_id = tenant_id
        self.location_id = location_id
        self.payment_date = payment_date
        self.amount_paid = amount_paid
        self.payment_status = payment_status
        self.method = method
        self.reference = reference

    def GetDataBaseFormat(self):
        return (self.id, self.schedule_id,self.tenant_id,self.location_id, self.payment_date, self.amount_paid, self.payment_status, self.method, self.reference)
    def NumberOfFields(self):
        return 7
#endregion



#region Tenant
class Tenant(IEntity):
    def __init__(self, id : str, first_name : str, last_name : str, national_insurance : str, email : str, password : str, phone_number : str, occupation : str, references : str):
        super().__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.national_insurance = national_insurance
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.occupation = occupation
        self.references = references
    
    def GetDataBaseFormat(self):
        return (self.id,self.first_name, self.last_name, self.email, self.password, self.national_insurance, self.phone_number, self.occupation , self.references)
    def NumberOfFields(self):
        return 9
#endregion

#region User
class User(IEntity):
    def __init__(self, id : str, firstName : str, lastName : str, email : str, password : str, role : str, location_id : str):
        super().__init__(id)
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.role = role
        self.location_id = location_id
        
    def GetDataBaseFormat(self):
        return (self.id, self.firstName, self.lastName, self.email, self.password, self.role, self.location_id)
    def NumberOfFields(self):
        return 7
#endregion

