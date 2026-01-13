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
    User("addo", "Adri", "1234", "ado@test.es", "ADMIN"),
    User("jodo", "John", "1234", "jodo@test.es", "ADMIN"),
    User("maria", "Maria", "1234", "madb@test.es", "ADMIN"),
    User("jodo", "John", "1234", "jodo@test.es", "ADMIN")
]


class UserDao:
    def __init__(self):
        self.users = users
        
    def getUserByUsername(self, uname):
        for u in self.users:
            if u.username == uname:
                return u.__dict__
        return None
    
    def getAllUsers(self):
        resposta = []
        for u in self.users:
            resposta.append(u.__dict__)
        return resposta

    def addUser(self, user):
        self.users.append(user)


user_dao = UserDao()
app = Flask(__name__)


@app.route('/user', methods=['GET'])
def user():
    username = request.args.get("username", default="")
    
    if username != "":
        resposta = user_dao.getUserByUsername(username)
        if resposta is None:
            resposta = {"msg": "Usuari No Trobat"}
    else:
        resposta = {"msg": "Falta paràmetre Username"}
    
    return jsonify(resposta)


@app.route('/getuser', methods=['GET'])
def userList():
    return jsonify(user_dao.getAllUsers())


@app.route('/users', methods=['POST'])
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