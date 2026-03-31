import sys
import random

import mysql.connector
from mysql.connector import errorcode
from security.dbSecrets import *
from models.Entities import *



isUsingDev = True

host = ""
user = ""
password = ""
dbName = ""

# Gets the connection to the database.
def GetConnection():
    if isUsingDev:
        host = devHost
        user = devUser
        password = devPassword
        dbName = devName
    else: 
        host = prodHost
        user = prodUser
        password = prodPassword
        dbName = prodName

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

#region Database to Objects

#region Location functions
# Searches the database for a location with the matching name and returns a location object if found, otherwise returns None
def GetLocation(locationName: str):
    query = "SELECT * FROM locations WHERE locations.location_name = %s;"

    conn = GetConnection()    
    
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
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
    dbcursor.execute('USE {};'.format(devName)) #use database'
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
    dbcursor.execute('USE {};'.format(devName)) #use database'
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
        building = []
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
    dbcursor.execute('USE {};'.format(devName)) #use database'
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
    query = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = %s;"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
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
    dbcursor.execute('USE {};'.format(devName)) #use database'
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
    dbcursor.execute('USE {};'.format(devName)) #use database'
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
    dbcursor.execute('USE {};'.format(devName)) #use database'
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
    dbcursor.execute('USE {};'.format(devName)) #use database'
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
def GetUnoccupiedApartmentsForLocation(locationID : int):
    query = "SELECT * from apartments WHERE location_id = %s AND occupancy_status = 0;"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("------------------")
    print("Entered Database") 
    print("Purpose: Retrieve all empty apartments in the location")
    dbcursor.execute(query, (locationID,))
    unoccupiedApartments = []

    for apartment in dbcursor.fetchall():
        unoccupiedApartments.append(Apartment(apartment[0],apartment[1],apartment[2],apartment[3],apartment[4],apartment[5],apartment[6]))
    
    return unoccupiedApartments

# def GetPaymentInsights(locationName : str):
#     id = GetLocation(locationName)


# Returns a list of all maintenance requests for apartments in a location matching an ID. If there are no requests it returns an empty list
def GetMaintenanceRequestsForLocation(locationID : str):
    query3 = "SELECT * from maintenance_requests WHERE apartment_id = %s;"

    apartments = GetApartmentsFromLocation(locationID)
    if apartments is None:
        return None
    else:
        conn = GetConnection()
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(devName)) #use database'
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
        dbcursor.execute('USE {};'.format(devName)) #use database'
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
    return None
    # location = GetLocation(locationName)

    # if location is not None:
    #     query = "SELECT apartment_id from apartments WHERE location_id = %s AND occupancy_status = 1;"

    #     conn = GetConnection()
    #     dbcursor = conn.cursor()    #Creating cursor object
    #     dbcursor.execute('USE {};'.format(devName)) #use database'
    #     print("------------------")
    #     print("Entered Database") 
    #     print("Purpose: Retrieve all tenants living in the location" + locationName)
    #     dbcursor.execute(query, (location.id,))
    #     apartmentIds = dbcursor.fetchall()

    #     query2 = "SELECT tenant_id FROM contracts WHERE apartment_id = %s;" #TODO remove those that no longer live in there by checking for days that are in date
    #     dbTenants = []
    #     for id in apartmentIds:
    #         dbcursor.execute(query, (id[0],))
    #         dbTenants.append(dbcursor.fetchall())

    #     query3 = "SELECT * FROM tenants WHERE tenant_id = %s;"
    #     tenants = []
    #     print(dbTenants)
    #     for tenantID in dbTenants:
    #         dbcursor.execute(query, (tenantID[0]))
    #         tenant = dbcursor.fetchone()
    #         tenants.append(Tenant(tenant[0],tenant[1],tenant[2],tenant[3],tenant[4],"Blocked", tenant[6],tenant[7],tenant[8]))
    #     dbcursor.close()
    #     conn.close()
    #     print("Closed Database")

    #     return tenants
    # else:
    #     dbcursor.close()
    #     conn.close()
    #     print("Closed Database")

    #     return None

        
def fetch_notifications(tenant_id=None, location_id=None):

    conn = GetConnection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('USE {};'.format(devName))

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

    query += " ORDER BY created_at DESC"

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()
    return results


def mark_notification_as_read(notification_id):

    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute('USE {};'.format(devName))

    cursor.execute(
        "UPDATE notifications SET is_read = 1 WHERE notification_id = %s",
        (notification_id,)
    )

    conn.commit()
    conn.close()