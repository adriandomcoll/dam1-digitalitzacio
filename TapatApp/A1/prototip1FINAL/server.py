from flask import Flask, request, jsonify


class User:
    def __init__(self, username, nom, password, email, rol):
        self.username = username
        self.nom = nom
        self.password = password
        self.email = email
        self.rol = rol

    def __str__(self):
        return self.nom


users = [
    User(username="addo", nom="Adri", password="1234", email="addo@test.es", rol="ADMIN"),
    User(username="jodo", nom="John", password="1234", email="jodo@test.es", rol="ADMIN"),
    User(username="maria", nom="Maria", password="1234", email="madb@test.es", rol="ADMIN"),
    User(username="jojo", nom="Jojo", password="1234", email="jojo@test.es", rol="ADMIN")
]


class UserDao:
    def __init__(self):
        self.users = users
        
    def getUserByUsername(self, uname):
        for u in self.users:
            if u.username == uname:
                return u.__dict__
        return None
    
    def getAllUsers(self,u):
        self.users.append(u)
        return [user.__dict__ for user in self.users]

    def addUser(self, user):
        self.users.append(user)


user_dao = UserDao()
app = Flask(__name__)


@app.route('/user', methods=['GET'])
def user():
    username = request.args.get("username", default="")
    if username != "":
        resposta = user_dao.getUserByUsername(username)
        if resposta == None:
            resposta = {"msg": "Usuari No Trobat"}
    else:
        resposta = {"msg": "Falta parametre Username"}
    
    return jsonify(resposta)


@app.route('/alluser', methods=['GET'])
def userList():
    return jsonify(user_dao.getAllUsers(user))


@app.route('/adduser', methods=['POST'])
def addUser():
    data = request.get_json()

    user = User(
        data["username"],
        data["nom"],
        data["password"],
        data["email"],
        data["rol"]
    )

    user_dao.addUser(user)
    return jsonify(user.__dict__), 201


if __name__ == '__main__':
    app.run(debug=True)