from flask import Flask, request, jsonify
class User:
    def __init__(self, username, nom, password, email, rol="tutor"):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol
    
    def __str__(self):
        return self.nom
    
class daoUserClient:
    def getUserByUsername(username): #el profe lo tiene con self
        #Petició Http al Webservice
        response = request.args.get('https://localhost:5000/getuser?username='+username)
        #Si la petició OK = code response 200

        if response.status_code == 200:
            #Obtenemos json
            user_data_raw = response.json()

            #Crear objeto user si se encontro
            msg = user_data_raw['msg']
            if msg:
                return None
            
            #Si no ha trobat return None
            else:
                user=User(user_data_raw['username'],user_data_raw['nom'],
                          user_data_raw['password'],user_data_raw['email'],user_data_raw['rol'])
                return user
        
        return None
    
class ViewConsole:
    def getInputUsername():
        #TODO
        return None
    
    def showUserInfo(username):
        #TODO
        return None
    
user_daoClient = daoUserClient()
daoUserClient.getUserByUsername("addo")
print(user_daoClient)