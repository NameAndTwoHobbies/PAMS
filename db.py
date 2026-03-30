import sys
import random

import mysql.connector
from mysql.connector import errorcode
from dbSecrets import *
from Entities import *



isUsingDev = False


# Gets the connection to the database.
def GetConnection():
    print(prodHost)
    if isUsingDev:
        host = devHost
        user = devUser
        password = devPassword
    else: 
        host = prodHost
        user = prodUser
        password = prodPassword

    try:
        conn = mysql.connector.connect(host = host, user = user, password =password)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('User name or password is not working')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        if conn.is_connected():
            print('MySQL Connection is established')
            return conn

#This function assumes that you have already checked that the location does not already exist
def AddLocation(location : Location):
    query = "INSERT INTO locations (location_name) VALUES (%s);"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database") 
    print("Purpose: Adding new location " + location.location_name)

    dbcursor.execute(query, (location.location_name,))
    conn.commit()
    dbcursor.close()
    conn.close()
    print("Database Closed")
    print("------------------")

def AddStaff(user : User):
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database") 
    print("Purpose: Checking if a user exists")

    dbcursor.execute(query , (user.email, user.password,))

    users =  dbcursor.fetchone()

    if users is not None:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        print("------------------")
        return False
    else:
        query = "INSERT INTO users (firstName, lastName, email, password, role, location_id) VALUES (%s,%s,%s,%s,%s,%s)"
        print(user.GetDataBaseFormat())
        print(user.GetDataBaseFormat()[1:])
        dbcursor.execute(query, (user.GetDataBaseFormat()[1:])) # removes the id from the user tuple as to prevent sql errors
        conn.commit()

        if user.role == "Manager":
            query = "SELECT user_id FROM users WHERE email = %s AND password = %s"
            conn = GetConnection()
            dbcursor = conn.cursor()    #Creating cursor object
            dbcursor.execute('USE {};'.format(prodName)) #use database'
            print("------------------")
            print("Entered Database") 
            print("Purpose: Checking if a user exists")

            dbcursor.execute(query , (user.email, user.password,))

            dbUser =  dbcursor.fetchone()


            query = "UPDATE locations SET location_manager = %s WHERE location_id = %s;"
            dbcursor.execute(query, (dbUser[0],int(user.location_id),)) # removes the id from the user tuple as to prevent sql errors
            conn.commit()
        dbcursor.close()
        conn.close()
        print("Database Closed")
        print("------------------")
        return True
def GetApartment(apartment_id : str):
    query = "SELECT * FROM apartments WHERE apartment_id = %s"
    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database") 
    print("Purpose: Retriving apartment")

    dbcursor.execute(query, (apartment_id,))

    dbApartment = dbcursor.fetchone()

    return Apartment(dbApartment[0],dbApartment[1],dbApartment[2],dbApartment[3],dbApartment[4],dbApartment[5],dbApartment[6])
def AddApartment(apartment : Apartment):
    query = "INSERT INTO apartments (location_id,room_type, monthly_rent, bedrooms,bathrooms) VALUES (%s,%s,%s,%s,%s)"
    
    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database") 
    print("Purpose: Adding Apartment to Location " + str(apartment.location_id))

    dbcursor.execute(query, (int(apartment.location_id), apartment.room_type, float(apartment.monthly_rent), apartment.bedrooms, apartment.bathrooms ,))

    conn.commit()
    dbcursor.close()
    conn.close()
    print("Database Closed")
    print("------------------")

#region Database to Objects

#region Location functions

def GetLocationFromID(locationID : str):
    query = "SELECT * FROM locations WHERE locations.location_id = %s;"

    conn = GetConnection()    
    
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database") 
    print("Purpose: Retrieve all locations that match the ID " + str(locationID))

    dbcursor.execute(query, (locationID,))
    location = dbcursor.fetchone()
    if(location is None):
        dbcursor.close()
        conn.close()
        print("Database Closed")
        print("------------------")
        return None
    else:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        print("------------------")
        return Location(location[0], location[1], location[2])
# Searches the database for a location with the matching name and returns a location object if found, otherwise returns None
def GetLocation(locationName: str):
    query = "SELECT * FROM locations WHERE locations.location_name = %s;"

    conn = GetConnection()    
    
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database") 
    print("Purpose: Retrieve all locations that match the name " + locationName)

    dbcursor.execute(query, (locationName,))
    location = dbcursor.fetchone()
    if(location is None):
        dbcursor.close()
        conn.close()
        print("Database Closed")
        print("------------------")
        return None
    else:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        print("------------------")
        return Location(location[0], location[1], location[2])

# Returns a list of all locations in the databases as Location objects. If there are no locations it returns None
def GetLocations():

    query = "SELECT * FROM locations"

    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database") 
    print("Purpose : Retrieve all locations from the database")  
    dbcursor.execute(query)
    records = dbcursor.fetchall()
    conn.commit()

    conn.close()
    dbcursor.close()
    print("Closed Database")
    print("------------------")

    locations = []
    for record in records:
        locations.append(Location(record[0],record[1],record[2]))
    return locations

#endregion


#region Apartment Functions
# Returns a list of apartment objects that are in a location matching an ID. If there are no apartments it returns None
def GetApartmentsFromLocation(Id : str):
    query2 = "SELECT * from apartments WHERE location_id = %s"
    
    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database") 
    print("Purpose : Retrieve all apartments in a given location")
    
    dbcursor.execute(query2, (Id,))
    apartments = dbcursor.fetchall()

    dbcursor.close()
    conn.close()
    print("Database Closed")
    print("------------------")

    if apartments is None:
        return None
    else: 
        building : list[Apartment] = []
        for apartment in apartments:
            building.append(Apartment(apartment[0],apartment[1],apartment[2],apartment[3],apartment[4],apartment[5],apartment[6]))
        return building

#endregion

#region Tenant Functions

# Returns a list of all tenants in the databases as Tenant objects. If there are no tenants it returns None
def GetTenants():

    query = "SELECT * FROM tenants"

    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")   
    print("Retrieve all the tenants from the database")
    dbcursor.execute(query)
    records = dbcursor.fetchall()
    conn.commit()

    conn.close()
    dbcursor.close()
    print("Closed Database")
    print("------------------")
    tenants = []
    for record in records:
        tenants.append(Tenant(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]))
    return tenants
#endregion

# Gets all the headers from a table in the database
def GetHeaders(table : str):
    query = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema = DATABASE() AND table_name = %s;"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")
    print("Purpose: Return the headers from the table " + table)
    dbcursor.execute(query, (table,))
    headers = dbcursor.fetchall()
    dbcursor.close()
    conn.close()
    print("Closed Database")
    print("------------------")
    return headers

#endregion


#region Signin and SignUp Functions
# Checks an email to see if a tenant already exists with that email. If there is a tenant with that email it returns False, otherwise it returns True
def CheckEmailIsValid(email : str):
    query = "SELECT * FROM tenants WHERE email = %s"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")
    print("Purpose: Check if a tenant with email" + email + " exists")
    dbcursor.execute(query, (email,))
    user = dbcursor.fetchone()
    if user is None:
        return True
    else:
        return False
    

# This function inserts a new tenant into the database. It assumes that the email has already been checked for validity.
def SignUpTenant(tenant : Tenant):
    #TODO do SQL injection protection
    query = "INSERT INTO tenants (first_name,last_name,national_insurance, email,password,phone_number,occupation) VALUES (%s,%s,%s,%s,%s,%s,%s);"
    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")   
    print("Purpose : Inserting the a new tenant into the database")
    dbcursor.execute(query, (tenant.first_name,tenant.last_name,tenant.national_insurance,tenant.email,tenant.password,tenant.phone_number,tenant.occupation,))
    conn.commit()


    conn.close()
    dbcursor.close()
    print("Closed Database")
    print("------------------")
    return None

# This function checks the credentials of a user trying to log in. If the credentials are valid it returns a tenant object, otherwise it returns None
#TODO make the checking of email and password seperate
def LoginTenant(email : str, hashedPassword : str):
    query = "SELECT * FROM tenants WHERE email = %s AND password =%s;"
    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")   
    print("Purpose: Checking the database to see if the email and password match a tenant")
    dbcursor.execute(query, (email, hashedPassword ,))
    tenant = dbcursor.fetchone()
    if tenant is None:
        dbcursor.close()
        conn.close()
        print("Closed Database")
        print("------------------")
        return None
    else:
        tenantUser =Tenant(tenant[0],tenant[1],tenant[2],tenant[3],tenant[4],tenant[5],tenant[6],tenant[7],tenant[8])

    dbcursor.close()
    conn.close()
    print("Closed Database")
    print("------------------")
    return tenantUser




def LoginUser(email : str, hashedPassword : str):
    query = "SELECT * FROM users WHERE email = %s AND password = %s ;"
    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")   
    print("Purpose: Checking the database to see if the email and password match a user")
    dbcursor.execute(query, (email, hashedPassword ,))
    dbUser = dbcursor.fetchone()
    if dbUser is None:
        dbcursor.close()
        conn.close()
        print("Closed Database")
        print("------------------")
        return None
    else:
        user = User(dbUser[0],dbUser[1],dbUser[2],dbUser[3],"Blocked", dbUser[5],dbUser[6])

    dbcursor.close()
    conn.close()
    print("Closed Database")
    print("------------------")
    return user
#endregion

#region Report Functionaility
# Returns the ids of the unoccupied apartments in a location matching an ID.

# def GetPaymentInsights(locationName : str):
#     id = GetLocation(locationName)


# Returns a list of all maintanence requests for apartments in a location matching an ID. If there are no requests it returns an empty list
def GetMainanenceRequestsForLocation(locationID : str):
    query3 = "SELECT * from maintenance_requests WHERE apartment_id = %s;"

    apartments = GetApartmentsFromLocation(locationID)
    if apartments is None:
        return None
    else:
        conn = GetConnection()
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(prodName)) #use database'
        print("------------------")
        print("Entered Database")
        print("Reason: Gather Maintanence requests by Apartment Id")
        
        requests = []
        for apartment in apartments:
            dbcursor.execute(query3, (apartment.id,))
            request = dbcursor.fetchone()
            if request is not None:
                requests.append(request)
        
        conn.close()
        dbcursor.close()
        print("Closed Database")
        print("------------------")
        return requests                
#endregion

def GetUsersFromLocation(locationName: str):
    location = GetLocation(locationName)

    if location is not None:
        query = "SELECT users.user_id,users.firstName,users.lastName, users.email, users.role FROM users WHERE users.location_id = %s;"

        conn = GetConnection()
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(prodName)) #use database'
        print("------------------")
        print("Entered Database")
        print("Purpose: Get users from location " + locationName)

        dbcursor.execute(query, (location.id,))

        users = []
        for user in dbcursor.fetchall():
            users.append(User(user[0],user[1],user[2],user[3],"Blocked",user[4], location.id))
        dbcursor.close()
        conn.close()
        print("Closed Database")

        return users
    else:
        dbcursor.close()
        conn.close()
        print("Closed Database")
        return None


#TODO not finished and ineffcient due to database
def GetTenantsFromLocation(locationName : str):
    
    location = GetLocation(locationName)
    locationID = location.GetID()
    query = "SELECT tenants.* FROM tenants INNER JOIN contracts ON contracts.tenant_id = tenants.tenant_id INNER JOIN apartments ON contracts.apartment_id = apartments.apartment_id WHERE apartments.location_id = %s"
    
    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")
    print("Purpose: Gather all the tenants for a given location")

    dbcursor.execute(query , (locationID, ))

    dbTenants = dbcursor.fetchall()
    tenants = []
    for dbTenant in dbTenants:
        tenants.append(Tenant(dbTenant[0],dbTenant[1],dbTenant[2],dbTenant[3],dbTenant[4],"Blocked",dbTenant[6],dbTenant[7],dbTenant[8]))

    dbcursor.close()
    conn.close()
    print("Closed Database")
    return tenants

#Retrieving the tenants payment history 
def GetTenantPaymentHistory(tenantID : str):
    query = "SELECT payments.* from payments INNER JOIN contracts on payments.contract_id = contracts.contract_id WHERE contracts.tenant_id = %s"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")
    print("Purpose: Get Payment History of tenant " + str(tenantID))

    dbcursor.execute(query, (tenantID,))

    dbPayments = dbcursor.fetchall()

    payments : list[Payment]= []
    for dbPayment in dbPayments:
        payment = Payment(dbPayment[0],dbPayment[1],dbPayment[2],dbPayment[3],dbPayment[4],dbPayment[5],dbPayment[6],dbPayment[7])
        payments.append(payment)
    dbcursor.close()
    conn.close()
    print("Closed Database")
    return payments

def GetAllPaymentsFromLocation(locationID : str):
    query = "SELECT payments.* FROM payments INNER JOIN contracts ON payments.contract_id = contracts.contract_id INNER JOIN apartments ON contracts.apartment_id = apartments.apartment_id WHERE apartments.location_id = %s" # Gets all the payments from the location through the contract of the payments

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")
    print("Purpose: Get Payment History of location " + str(locationID))

    dbcursor.execute(query, (locationID,))

    dbPayments = dbcursor.fetchall()

    payments : list[Payment] = []  
    for dbPayment in dbPayments:
        payments.append(Payment(dbPayment[0],dbPayment[1],dbPayment[2], dbPayment[3], dbPayment[4],dbPayment[5],dbPayment[6],dbPayment[7]))
    dbcursor.close()
    conn.close()
    print("Closed Database")
    return payments    

def GetContract(tenant_id : str):
    query = "SELECT * FROM contracts WHERE tenant_id = %s AND end_date > CURRENT_TIMESTAMP()"
    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")
    print("Purpose: Retreive the contract for a given tenant")

    dbcursor.execute(query ,(tenant_id,))

    contract =  dbcursor.fetchone()

    if contract is not None:
        return Contract(contract[0],contract[1],contract[2],contract[3],contract[4],contract[5],contract[6])
       
    else:
        dbcursor.close()
        conn.close()
        print("Closed Database")
        return None

def GetRentPayments(contract : Contract):
        if contract is not None:
            conn = GetConnection()
            dbcursor = conn.cursor()    #Creating cursor object
            dbcursor.execute('USE {};'.format(prodName)) #use database'
            print("------------------")
            print("Entered Database")
            print("Purpose: Retreive the most recent rent payment for the tenant")

            query = "SELECT * FROM payments WHERE reference = 'Rent' AND payment_status = 'Unpaid' AND contract_id = %s"
            dbcursor.execute(query, (contract.id,))

            rentPayments = dbcursor.fetchall()
            dbcursor.close()
            conn.close()
            print("Closed Database")
            if rentPayments is not None:
                payments : list[Payment] = []
                for payment in rentPayments:
                    payments.append(Payment(payment[0],payment[1],payment[2],payment[3],payment[4],payment[5],payment[6],payment[7],))
                return payments
            else:
                return None 
        

def AddRequirements(reqs : Requirements):
    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")
    print("Purpose: Checking if a tenant has a previous requirement")

    query = "SELECT requirements_id FROM requirements WHERE tenant_id = %s;"
    dbcursor.execute(query , (reqs.tenant_id,))

    dbReqs = dbcursor.fetchone()

    if dbReqs is not None:
        print(dbReqs)
        query = "UPDATE requirements SET location_id = %s, tenant_id= %s, room_type = %s , monthly_rent = %s, bedrooms = %s, bathrooms = %s WHERE requirements_id = %s"
        reqs.id = dbReqs[0]
        dbcursor.execute(query,(int(reqs.location_id),int(reqs.tenant_id),reqs.room_type, float(reqs.monthly_rent),reqs.bedrooms,reqs.bathrooms , reqs.id))
    else:
        query = "INSERT INTO requirements (location_id, tenant_id,room_type,monthly_rent,bedrooms,bathrooms) VALUES (%s,%s,%s,%s,%s,%s)"
        dbcursor.execute(query,(int(reqs.location_id),int(reqs.tenant_id),reqs.room_type, float(reqs.monthly_rent),reqs.bedrooms,reqs.bathrooms ,))
    
    conn.commit()
    dbcursor.close()
    conn.close()
    print("Closed Database")

    
def CreateInvoice(invoice :Payment):
    query = "INSERT INTO payments (contract_id, due_date,amount,payment_status,reference) VALUES (%s,%s,%s,%s,%s)"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")
    print("Purpose: Issue invoice")

    dbcursor.execute(query, (invoice.contract_id,invoice.dueDate,invoice.amount_paid,invoice.payment_status,invoice.reference,))

    conn.commit()
    dbcursor.close()
    conn.close()
    print("Closed Database")

def IssueRentPayments(location_id : str):
    query = "SELECT * FROM apartments WHERE location_id = %s AND occupancy_status = 1"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")
    print("Purpose: Gather all occupied apartments")

    dbcursor.execute(query, (location_id,))

    dbApartments= dbcursor.fetchall()
    dbcursor.close()
    conn.close()
    print("Closed Database")
    for apartment in dbApartments :
        conn = GetConnection()
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(prodName)) #use database'
        print("------------------")
        print("Entered Database")
        print("Purpose: Checking if there is already a monthly payment")

        query = "SELECT contract_id FROM contracts WHERE apartment_id = %s AND end_date > CURRENT_TIMESTAMP()" # contracts from appartments stillbeing run

        dbcursor.execute(query, (apartment[0],))

        dbTenant = dbcursor.fetchone()
        if dbTenant is not None:
            dbContract_id = dbTenant[0]
            query = "SELECT * FROM payments WHERE contract_id = %s AND due_date > CURRENT_TIMESTAMP() AND reference = 'Rent'" # Checks if there is already a rent invoice for this month in the payments table for the tenant
            dbcursor.execute(query, (dbContract_id,))
            payments = dbcursor.fetchall()
            dbcursor.execute("SELECT LAST_DAY(CURRENT_TIMESTAMP())")
            lastDay = dbcursor.fetchone()  
            dbcursor.close()
            conn.close()
            print("Closed Database")
            if payments == []:
                print("isNull")
                CreateInvoice(Payment("", dbContract_id, 'NULL' , lastDay[0],apartment[3],"Unpaid","", "Rent"))
        else:
            dbcursor.close()
            conn.close()
            print("Closed Database")

def UpdateTenant(tenant : Tenant):
    db = tenant.GetDataBaseFormat()
    #TODO check if the user exits
    query = "UPDATE tenants SET first_name = %s, last_name = %s, national_insurance = %s, email = %s, tenants.password= %s, phone_number = %s, occupation= %s, tenants.references = %s WHERE tenant_id = %s"
    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(prodName)) #use database'
    print("------------------")
    print("Entered Database")
    print("Purpose: Update Tenants Details")

    dbcursor.execute(query, (tenant.first_name,tenant.last_name,tenant.national_insurance,tenant.email,tenant.password,tenant.phone_number,tenant.occupation,tenant.references , tenant.id,))

    conn.commit()
    dbcursor.close()
    conn.close()
    print("Closed Database")

def MakePayment(contract : Contract):
    #TODO CHECK WITH THE UPDATING PAYMENT HISTORY TABLE AND USE THAT TO PUT INTO THE CURRENT DUE
    if contract is not None:
        query = "SELECT * FROM payments WHERE payment_status = 'Unpaid' AND contract_id = %s"
        conn = GetConnection()
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(prodName)) #use database'
        print("------------------")
        print("Entered Database")
        print("Purpose: Paying all outstanding payments")

        dbcursor.execute(query,(contract.id,))

        dbPayments = dbcursor.fetchall()
        if dbPayments is not None:
            for payment in dbPayments:
                query = "UPDATE payments SET payment_date = CURRENT_TIMESTAMP() , payment_status = 'Paid', method = 'BankTransfer' WHERE payment_id = %s"

                dbcursor.execute(query,(payment[0],))
            conn.commit()

        dbcursor.close()
        conn.close()
        print("Closed Database")
        
