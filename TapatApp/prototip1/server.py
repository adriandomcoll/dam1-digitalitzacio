from flask import Flask, request, jsonify


class User:
    def __init__(self,username, nom, password, email, rol):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol

    def __str__(self):
        return self.nom


#us1=User(username="addo",nom="Adri",password="1234",email="ado@test.es",rol="ADMIN")

users = [
    User(username="addo",nom="Adri",password="1234",email="ado@test.es",rol="ADMIN"),
    User(username="addo",nom="Adri",password="1234",email="ado@test.es",rol="ADMIN"),
    User(username="addo",nom="Adri",password="1234",email="ado@test.es",rol="ADMIN"),
]

class UserDao:
    def __init__(self):
        self.users=users
        
    def getUserByUsername(self,username):
        return "TO-DO"

app = Flask(__name__)

@app.route('/user',methods=['GET'])
def user():
    resposta=""
    # Parametres
    username = request.args.get("username",default="")
    # Si els paràmetres OK
    if username != "":
        # Anar al DAO Server i cercar User per username
        # respondre amb dades Usuari si trobat
        resposta="username" + username
    
    # Si els paràmetres NO OK
    else: 
        # respondre error 
        resposta="username no informat"
    return resposta

if __name__ == '__main__':
    app.run(debug=True)