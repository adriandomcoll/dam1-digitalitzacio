from flask import Flask, request, jsonify
from dadesServer import *

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


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(user_dao.getAllUsers())


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = user_dao.getUserById(id)

    if user:
        return jsonify(user)

    return jsonify({"msg": "User no trobat"}), 404


@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()

    new_user = User(
        data["id"],
        data["username"],
        data["password"],
        data["email"],
        data["idrole"]
    )

    return jsonify(user_dao.addUser(new_user)), 201



@app.route('/children', methods=['GET'])
def get_children():
    return jsonify(child_dao.getAllChildren())


@app.route('/children/user/<int:user_id>', methods=['GET'])
def get_children_by_user(user_id):
    return jsonify(child_dao.getChildrenByUser(user_id))



@app.route('/taps/child/<int:child_id>', methods=['GET'])
def get_taps_by_child(child_id):
    return jsonify(tap_dao.getTapsByChild(child_id))



@app.route('/statuses', methods=['GET'])
def get_status():
    return jsonify(status_dao.getAllStatus())



@app.route('/roles', methods=['GET'])
def get_roles():
    return jsonify(role_dao.getAllRoles())


@app.route('/treatments', methods=['GET'])
def get_treatments():
    return jsonify(treatment_dao.getAllTreatments())


if __name__ == '__main__':
    app.run(debug=True)
