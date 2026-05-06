from flask import Flask, request, jsonify
from DaoServer import UserDao, ChildDao
from dataclasses import dataclass, asdict

@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list

# Instantiate DAO
user_dao=UserDao()
child_dao=ChildDao()

app = Flask(__name__)

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
    data = request.get_json() or {}

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
def child():
    token=request.headers.get("apikey")
    u=None
    if(token):
        # comprovar que el token existeix a un usuari
        print(token)
        u=user_dao.getUserByToken(token)
        print("USER:", u)
    
    if u:
        # obtener children autorizados por user id
        childs=child_dao.getChilds(str(u['id']))
        response = ApiResponse(
                msg="GetChilds",
                coderesponse="1",
                data=childs
            )
        return jsonify(asdict(response)),200
    else: 
        response = ApiResponse(
            msg="Acces not granted",
            coderesponse="0",
            data=""
        )
        return jsonify(asdict(response)),400


# All childs
@app.route('/childs', methods=['POST'])
def get_childs():

    token = request.headers.get("apikey")

    data = request.get_json() or {}
    childs = child_dao.getChilds()

    return jsonify({
        "msg": "Numero de Childs: " + str(len(childs)),
        "coderesponse": "1",
        "children": childs
    }), 200

# Taps: obtener taps de un child
@app.route('/child/<int:child_id>', methods=['GET'])
def get_child_taps(child_id):
    # opcional: validar token si se desea
    token = request.headers.get("apikey")
    if token:
        u = user_dao.getUserByToken(token)
        if not u:
            return jsonify({"coderesponse": "0", "msg": "Access not granted"}), 400

    taps = child_dao.get_taps(child_id)
    response = ApiResponse(msg="GetTaps", coderesponse="1", data=taps)
    return jsonify(asdict(response)), 200

if __name__ == '__main__':
    app.run(debug=True)