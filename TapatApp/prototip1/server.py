from flask import Flask, request, jsonify

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