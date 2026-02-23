from flask import Flask, request, jsonify
from dadesServer import *
import uuid

app = Flask(__name__)


class UserDao:

    def getAllUsers(self):
        return [u.__dict__ for u in users]

    def getUserById(self, id):
        for u in users:
            if u.id == id:
                return u.__dict__
        return None

    def addUser(self, user):
        users.append(user)
        return user.__dict__
    
    def getUserByUsername(self, username):
        for user in users:
            if user.username == username or user.email == username:
                return user
        return None
    
    def login(self, username, password):
        for u in users:
            if u.username == username and u.password == password:
                return u
        return None
    
    def getUserByToken(self, token):
        for u in users:
            if hasattr(u, "token") and u.token == token:
                return u
        return None




class ChildDao:

    def getAllChildren(self):
        return [c.__dict__ for c in children]

    def getChildrenByUser(self, user_id):
        child_ids = [r["child_id"] for r in relation_user_child if r["user_id"] == user_id]
        return [c.__dict__ for c in children if c.id in child_ids]



class TapDao:

    def getTapsByChild(self, child_id):
        return [t.__dict__ for t in taps if t.child_id == child_id]



class StatusDao:

    def getAllStatus(self):
        return [s.__dict__ for s in statuses]



class RoleDao:

    def getAllRoles(self):
        return [r.__dict__ for r in roles]



class TreatmentDao:

    def getAllTreatments(self):
        return [t.__dict__ for t in treatments]


user_dao = UserDao()
child_dao = ChildDao()
tap_dao = TapDao()
status_dao = StatusDao()
role_dao = RoleDao()
treatment_dao = TreatmentDao()


# Login

@app.route('/login', methods=['POST'])
def login():

    token_header = request.headers.get("Authorization")

    # Login por token
    if token_header:
        user = user_dao.getUserByToken(token_header)

        if user:
            return jsonify({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "token": user.token,
                "idrole": user.idrole,
                "msg": "Usuari Ok",
                "coderesponse": "1"
            }), 200

        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400


    # Login normal
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

    user = user_dao.login(username, password)

    if user:
        # Para generar el token
        user.token = str(uuid.uuid4())

        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "token": user.token,
            "idrole": user.idrole,
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200

    return jsonify({
        "coderesponse": "0",
        "msg": "No validat"
    }), 400


# Child

@app.route('/child', methods=['POST'])
def get_child():

    token = request.headers.get("Authorization")

    if not token:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

    user = user_dao.getUserByToken(token)

    if not user and not iduser.is_integer:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

    data = request.get_json()
    iduser = data.get("iduser")

    childs = child_dao.getChildrenByUser(iduser)

    return jsonify({
        "msg": str(len(childs)),
        "coderesponse": "1",
        "children": childs
    }), 200


if __name__ == '__main__':
    app.run(debug=True)