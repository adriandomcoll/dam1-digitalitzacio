from dataclasses import dataclass, asdict
from flask import jsonify
from time import time
import mysql.connector
import hashlib
import random

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
        return user
    def setTokenUser (self, username):
        # conectar a BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        # generar Token
        token=self.getHash(username)

        # Update a BBDD camp token al usuari per username
        query = "UPDATE User SET token ='"+token +"' WHERE username" + username
        print(query)
        cursor.execute(query)
        # close BBDD
        cursor.close()
        con.close()
    
    def getHash(self, username):
        miliseconds = str(time() * 1000)
        data = username + miliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()

dao = UserDao()
print(dao.getHash("user1"))

u = dao.login("mare", "mare")
print(u)


miliseconds = str(time() * 1000)
print("Time in milliseconds since epoch", miliseconds)

data = "Holas " + miliseconds
print(data)
# Crea el objeto SHA-256

# Obtener el resultado en formato hexadecimal 
# token = hash_object.hexdigest()
# print(token)