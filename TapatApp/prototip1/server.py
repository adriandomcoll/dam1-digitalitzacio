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
    User(username="jodo",nom="John",password="1234",email="jodo@test.es",rol="ADMIN"),
    User(username="maria",nom="Maria",password="1234",email="madb@test.es",rol="ADMIN"),
    User(username="jodo",nom="John",password="1234",email="jodo@test.es",rol="ADMIN")
]

class UserDao:
    def __init__(self):
        self.users=users
        
    def getUserByUsername(self,uname):
        user = None
        for u in self.users:
            if u.username == uname:
                user = u.__dict__
        return user
    
    def getAllUsers(self):
        resposta = []
        for u in self.users:
            resposta.append(u.__dict__)
        return resposta

def getAllUsers(self):
    return [u.to_dict() for u in self.users]

user_dao = UserDao()
app = Flask(__name__)

def __init__(self):
    self.users = users


def addUser(self, user):
    self.users.append(user)


@app.route('/user',methods=['GET'])
def user():
    resposta=""
    # Parametres
    username = request.args.get("username",default="")
    # Si els paràmetres OK
    if username != "":     
        # Ir al DAO Server y buscar User por username 
        resposta=user_dao.getUserByUsername(username)
        if resposta == None:
            resposta = {"msg":"Usuari No Trobat"}

    # Si els paràmetres NO OK
    else: 
        # respondre error 
        resposta={"msg":"Falta paràmetre Username"}
    
    return jsonify(resposta)

@app.route('/getuser', methods=['GET'])
def userList(self):
    resposta = user_dao.get
    return jsonify(user_dao.getAllUsers())

@app.route('/users', methods=['POST'])
def addUser(self):
    self.users.append(user)
    return user

if __name__ == '__main__':
    app.run(debug=True)
