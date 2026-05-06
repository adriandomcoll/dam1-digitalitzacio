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
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM User WHERE token = %s"
        cursor.execute(query, (token,))
        user = cursor.fetchone()
        cursor.close()
        con.close()
        return user

    def login(self, identifier, password):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = """
            SELECT * FROM User
            WHERE (username = %s OR email = %s) AND password = %s
        """
        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        token = ""
        if user:
            token = self.setTokenUser(user['username'])
            user['token'] = token
        cursor.close()
        con.close()
        return user
    
    def setTokenUser(self, username):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        token = self.getHash()
        query = "UPDATE User SET token = %s WHERE username = %s"
        cursor.execute(query, (token, username))
        con.commit()
        cursor.close()
        con.close()
        return token
    
    def getHash(self):
        miliseconds = str(time() * 1000)
        data = miliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()

class ChildDao:

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )
        return connection

    # Mantengo el método que obtiene children a partir de token (útil en server)
    def getChildrenByUser(self, token):
        # Obtener user_id del token
        user_dao = UserDao()
        user = user_dao.getUserByToken(token)
        if not user:
            return []
        
        user_id = user['id']
        return self.getChilds(user_id)

    # getChilds ahora acepta opcionalmente user_id para comportarse como los otros métodos
    def getChilds(self, user_id=None):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        if user_id:
            query = """
                SELECT DISTINCT c.* FROM Child c
                INNER JOIN RelationUserChild ruc ON c.id = ruc.child_id
                WHERE ruc.user_id = %s
            """
            cursor.execute(query, (user_id,))
        else:
            query = "SELECT * FROM Child"
            cursor.execute(query)
        children = cursor.fetchall()
        cursor.close()
        con.close()
        return children
    
    # Devuelve taps por id (mantengo nombres existentes para compatibilidad)
    def getTapById(self, id):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM Tap WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        cursor.close()
        con.close()
        return result
            
    
    def getTapByUserId(self, id):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM Tap WHERE user_id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        cursor.close()
        con.close()
        return result
    
    def getTapByChildId(self, id):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM Tap WHERE child_id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        cursor.close()
        con.close()
        return result
    
    def get_taps(self, child_id):
        return self.getTapByChildId(child_id)

'''    
cdao=ChildDao()
res=cdao.getTapByChildId("1")
print(res)
'''
