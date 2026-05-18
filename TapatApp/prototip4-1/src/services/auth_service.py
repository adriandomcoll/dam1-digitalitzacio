class AuthService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def login(self, username, password):
        user = self.user_dao.get_user_by_username_or_email(username)
        if user and user.password == password:
            return {
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
            }
        return {
            "coderesponse": "0",
            "msg": "No validat"
        }

    def validate_token(self, token):
        user = self.user_dao.get_user_by_token(token)
        if user:
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "token": user.token,
                "idrole": user.role_id,
                "msg": "Usuari Ok",
                "coderesponse": "1"
            }
        return {
            "coderesponse": "0",
            "msg": "No validat"
        }