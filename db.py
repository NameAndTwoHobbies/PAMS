import sys
import random

import mysql.connector
from mysql.connector import errorcode

from dbSecrets import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import * 
from PySide6.QtSql import *
from ErrorBoxes import ErrorMessage

isUsingDev = True

host = ""
user = ""
password = ""
dbName = ""

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


def GetTenants():

    query = "SELECT * FROM tenants"

    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")   
    dbcursor.execute(query)
    records = dbcursor.fetchall()
    conn.commit()

    conn.close()
    dbcursor.close()
    return records

def GetLocations():

    query = "SELECT * FROM locations"

    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")   
    dbcursor.execute(query)
    records = dbcursor.fetchall()
    conn.commit()

    conn.close()
    dbcursor.close()
    return records

# Gets all the headers from a table in the database
def GetHeaders(table : str):
    query = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = %s;"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")
    dbcursor.execute(query, (table,))
    headers = dbcursor.fetchall()
    dbcursor.close()
    conn.close()
    return headers

def CheckEmailIsValid(email : str):
    query = "SELECT * FROM tenants WHERE email = %s"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")
    dbcursor.execute(query, (email,))
    user = dbcursor.fetchone()
    
    if user is not None:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        title = "Tenant Already Exists"
        description = "This email has already been used to sign up a user. Please try a different email."
        error = ErrorMessage(title, description)
        return (error)
    else:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        return None

def SignUpUser():
    pass

def LoginUser(email : str, hashedPassword : str):
    pass
