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

    def getUserByToken(self, token):
        # Conexión a BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM User WHERE token =  '" + token + "'"
        
        cursor.execute(query)
        user = cursor.fetchone()
        cursor.close()
        con.close()
        return user

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
        token= ""
        if user:
            token = self.setTokenUser(user['username'])
            user['token'] = token
            print(user)
        cursor.close()
        con.close()
        return user
    
    def setTokenUser (self, username):
        # Connect a BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        # Generate Token
        token=self.getHash()

        # Update a BBDD camp token al usuari per username
        print(type(token))
        query = "UPDATE User SET token='"+ token +"' WHERE username= '" + username + "'"

        cursor.execute(query)
        con.commit()

        # Close BBDD
        cursor.close()
        con.close()
        return token
    
    def getHash(self):
        miliseconds = str(time() * 1000)
        data = miliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest() + ""

class ChildDao:

    def getChilds(self,username):
        return "" #TODO



dao = UserDao()
u = dao.getUserByToken("0d68b59a19040fdcd094a60ad2e5f8bfc0f59acd46810213aec25e8afb3f0926")
print(u)
u = dao.getUserByToken("token invalido")
print(u)

'''
class ChildDao:

    def __init__(self):
        self.childs = children
        self.relation_user_child = relation_user_child

    def getAllChildren(self):
        return [c.__dict__ for c in self.childs]

    def getChildrenByUser(self, user_id):
        child_ids = [r["child_id"] for r in self.relation_user_child if r["user_id"] == user_id]
        return [c.__dict__ for c in self.childs if c.id in child_ids]

# Crea el objeto SHA-256

# Obtener el resultado en formato hexadecimal 
# token = hash_object.hexdigest()
# print(token)


#TODO Endpoint del Login
'''