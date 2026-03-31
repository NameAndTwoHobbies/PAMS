import mysql.connector
from mysql.connector import errorcode
from security.dbSecrets import devHost, devUser, devPassword, devName, prodHost, prodUser, prodPassword, prodName


class DatabaseConnection:

    def __init__(self, use_dev=False):
        self.use_dev = use_dev

    def get_connection(self):
        if self.use_dev:
            config = {
                "host": devHost,
                "user": devUser,
                "password": devPassword,
                "database": devName
            }
        else:
            config = {
                "host": prodHost,
                "user": prodUser,
                "password": prodPassword,
                "database": prodName
            }

        try:
            return mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise Exception("Invalid DB credentials")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise Exception("Database does not exist")
            else:
                raise err