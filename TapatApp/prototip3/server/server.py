from flask import Flask, request, jsonify
from DaoServer import *
import uuid

app = Flask(__name__)

user_dao = UserDao()
child_dao = ChildDao()



# Login

@app.route('/login', methods=['POST'])
def login():

    token_header = request.headers.get("apikey")

    # Login por token
    if token_header:
        user = user_dao.getUserByToken(token_header)

        if user:
            return jsonify({
                "id": user['id'],
                "username": user['username'],
                "password": user['password'],
                "email": user['email'],
                "token": user['token'],
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
    print (user)

    if user:
        return jsonify({
            "id": user['id'],
            "username": user['username'],
            "password": user['password'],
            "email": user['email'],
            "token": user['token'],
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

    token = request.headers.get("apikey")
    user = None
    
    if token:
        user = user_dao.getUserByToken(token)

    if not user:
        return jsonify({
            "coderesponse": "0",
            "msg": "Acces not granted"
        }), 400

    # Pasar el token directamente
    childs = child_dao.getChildrenByUser(token)

    return jsonify({
        "msg": "Numero de Childs: " + str(len(childs)),
        "coderesponse": "1",
        "children": childs
    }), 200


# All childs
@app.route('/childs', methods=['POST'])
def get_childs():

    token = request.headers.get("apikey")

    data = request.get_json()
    childs = child_dao.getChilds()

    return jsonify({
        "msg": "Numero de Childs: " + str(len(childs)),
        "coderesponse": "1",
        "children": childs
    }), 200

if __name__ == '__main__':
    app.run(debug=True)