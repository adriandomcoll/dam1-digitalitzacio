from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"coderesponse": "0", "msg": "No validat"}), 400

    user = auth_service.validate_user(username, password)

    if user:
        return jsonify({
            "coderesponse": "1",
            "data": {
                "email": user.email,
                "id": user.id,
                "idrole": user.role_id,
                "password": user.password,
                "token": user.token,
                "username": user.username
            },
            "msg": "Authenticated"
        }), 200
    else:
        return jsonify({"coderesponse": "0", "msg": "No validat"}), 400

@auth_bp.route('/login/token', methods=['POST'])
def login_with_token():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"coderesponse": "0", "msg": "No validat"}), 400

    user = auth_service.validate_token(token)

    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "token": user.token,
            "idrole": user.role_id,
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200
    else:
        return jsonify({"coderesponse": "0", "msg": "No validat"}), 400