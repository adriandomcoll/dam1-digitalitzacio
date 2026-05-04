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

    def getChildrenByUser(self, token):
        # Obtener user_id del token
        user_dao = UserDao()
        user = user_dao.getUserByToken(token)
        if not user:
            return []
        
        user_id = user['id']
        
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = """
            SELECT DISTINCT c.* FROM Child c
            INNER JOIN RelationUserChild ruc ON c.id = ruc.child_id
            WHERE ruc.user_id = %s
        """
        cursor.execute(query, (user_id,))
        children = cursor.fetchall()
        cursor.close()
        con.close()
        return children

    def getChilds(self):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM Child"
        cursor.execute(query)
        children = cursor.fetchall()
        cursor.close()
        con.close()
        return children
    
class TapDAO:

    def setTap (self,user:User.User,child:Child.Child,status:int):
        
        con = self.connectBBDD()
        sendSQL = con.cursor(dictionary=True)

        query = "INSERT INTO Tap(child_id,status_id,user_id)\
                VALUES (%s, %s, %s)"

        sendSQL.execute(query,(child.id,status,user.id))
        con.commit()

        sendSQL.close()
        con.close()
    
    def getTapById(self,id:int):
        
        con = self.connectBBDD()
        sendSQL = con.cursor(dictionary=True)

        query = "SELECT *\
                FROM Tap\
                WHERE id = %i"
        sendSQL.execute(query,(id))

        result=sendSQL.fetchall()

        sendSQL.close()
        con.close
        return result
            
    
    def getTapByUserId(self,id:int):
        
        con = self.connectBBDD()
        sendSQL = con.cursor(dictionary=True)

        query = "SELECT *\
                FROM Tap\
                WHERE user_id = %i"
        
        sendSQL.execute(query,(id))
        result=sendSQL.fetchall()
        
        sendSQL.close()
        con.close

        return result
    
    def getTapByChildId(self,id:int):
        
        con = self.connectBBDD()
        sendSQL = con.cursor(dictionary=True)
        query = "SELECT *\
                FROM Tap\
                WHERE child_id = %i"
        sendSQL.execute(query,(id))
        result=sendSQL.fetchall()

        sendSQL.close()
        con.close
        return result