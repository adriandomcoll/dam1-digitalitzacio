import requests

class User:
    def __init__(self, username, nom, password, email, rol="ADMIN"):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol
    
    def __str__(self):
        return self.nom
    
class daoUserClient:
    def getUserByUsername(self, username): #el profe lo tiene con self
        #Petició Http al Webservice
        response = requests.get('http://127.0.0.1:5000/getuser?username='+username)

        #Si la petició OK = code response 200
        if response.status_code == 200:
            #Obtenemos json
            user_data_raw = response.json()

            #Crear objeto user si se encontro
            if 'msg' in user_data_raw.keys():
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
    
view=ViewConsole.showUserInfo

  
daoUserClient = daoUserClient()
u=daoUserClient.getUserByUsername("addo")
print(u)