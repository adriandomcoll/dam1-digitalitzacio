import requests
from User import *

class DaoUserClient:
    base_URL = "http://localhost:5000"

    def login(self, user):
        # Petició HTTP amb token
        URL_peticio = self.base_URL + "/login"
        params_POST = {
            "token": user.token
        }
        response = requests.post(URL_peticio, json=params_POST)
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response = user_data_raw.get('coderesponse')
            if str(code_response) == "1":
                user = User(
                    user_data_raw['id'],
                    user_data_raw['username'],
                    "",
                    user_data_raw['email'],
                    user_data_raw['idrole'],
                    user_data_raw['token']
                )
                return user
            else:
                return None
        else:
            return None
#TEST        
daoClient=DaoUserClient()
user=User("", "", "", "", "", "6dce72cbc40848c17a8961428a45680442a1ee1a75808853b91c32ba76d71e6f")
resposta=daoClient.login(user)
print(resposta)

