from dataclasses import dataclass, asdict
from flask import jsonify
import mysql.connector

class UserDao:

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )
        return connection

    def login(self, identifier, password):
        # Conexión a BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = """
            SELECT * FROM User
            WHERE (username = %s OR email = %s) AND password = %s
        """
        cursor.execute(query,(identifier,identifier,password))
        user = cursor.fetchone()
        cursor.close()
        con.close()
        # Query para validar Usuario 
            # if return 1 = registro User OK
            # else None
        # Cerrar conexión
        return user
    
dao = UserDao()
u = dao.login("mare", "mare")
print(u)