class UserDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_user_by_username(self, username):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM User WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        cursor.close()
        return user

    def get_user_by_email(self, email):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM User WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        cursor.close()
        return user

    def validate_user(self, username, password):
        user = self.get_user_by_username(username)
        if user and user['password'] == password:
            return user
        return None