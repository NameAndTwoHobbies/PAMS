# Base repository for database operations
# This class provides common methods for executing queries and fetching results.
# Repositories for specific entities (e.g., UserRepository, ProductRepository) will inherit from this base class.
# Repositories folder replaces 'db.py' and contains all database-related logic, ensuring separation of concerns and maintainability.

class BaseRepository:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def fetch_one(self, query, params=None):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or ())
        result = cursor.fetchone()
        conn.close()
        return result

    def fetch_all(self, query, params=None):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or ())
        results = cursor.fetchall()
        conn.close()
        return results

    def execute(self, query, params=None):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        conn.close()