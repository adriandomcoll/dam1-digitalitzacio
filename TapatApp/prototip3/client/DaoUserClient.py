import requests
from User import *
from flask import jsonify

class DaoUserClient:
    base_URL = "http://127.0.0.1:5000"
    token=""

    def login(self, user):
        # Validació paràmetres 
        # TO-DO
        # Petició HTTP al Webservice /login
        URL_peticio= self.base_URL + "/login"
        params_POST = {
            "username": user.username,
            "password": user.password
        }
        response = requests.post(URL_peticio, json=params_POST)
        if response.status_code == 200:
            user_raw = response.json()
            code_response=user_raw['coderesponse']
            if code_response == '1': # Usuari Validat  (self, id, username, password, email, idrole,token):
                user=User(user_raw['id'], user_raw['username']
                          , "" ,user_raw['email']
                          , "", user_raw['token'])
                self.token=user_raw['token']
                return user
            else: 
                return None
        else:
            return None
    
    def loginToken(self, token):
        URL_peticio= self.base_URL + "/login"
        print(token)
        headers = {'Content-Type': 'application/json', 'apikey': token}
        response = requests.post(URL_peticio,headers=headers) 
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response=user_data_raw['coderesponse']
            if code_response == '1': # Usuari Validat  (self, id, username, password, email, idrole,token):
                user_raw=user_data_raw
                user=User(user_raw['id'], user_raw['username']
                          , "" ,user_raw['email']
                          , "", user_raw['token'])
                return user  
        else:
            return None

    def childToken(self, token):
        URL_peticio= self.base_URL + "/child"
        #print(token)
        headers = {'Content-Type': 'application/json', 'apikey': token}
        response = requests.post(URL_peticio,headers=headers) 
        if response.status_code == 200:
            user_raw = response.json()
            code_response=user_raw['coderesponse']
            if code_response == '1': # Usuari Validat  (self, id, username, password, email, idrole,token):
                return user_raw
        else:
            return None

    def tapId(self, child_id, token=None):
        URL = f"{self.base_URL}/child/{child_id}"
        headers = {}
        if token:
            headers['apikey'] = token
        try:
            response = requests.get(URL, headers=headers, timeout=5)
        except Exception:
            return None
        if response.status_code != 200:
            return None
        try:
            data = response.json()
        except Exception:
            return None
        if str(data.get("coderesponse")) == "1":
            return data.get("data", [])
        return None


daoClient=DaoUserClient()

#resposta=daoClient.loginToken("20732fb71deb93f1ec163dc3b03aaafddfff76ccfdf45150e94d01eb099eb651")
#print(resposta)

#user=User("","mare", "mare", "12345", "", "")
#resposta=daoClient.login(user)
#print(resposta)
#print(daoClient.token)
resposta=daoClient.tapId("3394116c3286fb20a3ffd2e3e64c0300e80bdaf97e07d4220faf349e5153fd89")
print(resposta)


'''Servei Login
End-point: /login
Method: POST
Estat: Public
Tipus petició : application/json
Paramètres:

username : (string) username o email
password : (string) password
Resposta Usuari validat Ok:
http Response Code: 200 ok

{
  "coderesponse": "1",
  "data": {
    "email": "prova@gmail.com",
    "id": 1,
    "idrole": 1,
    "password": "12345",
    "token": "",
    "username": "mare"
  },
  "msg": "Authenticated"
}
Resposta Usuari No validat: http Response Code: 400 ok

{
     "coderesponse": "0"
     "msg": "No validat"
}
'''