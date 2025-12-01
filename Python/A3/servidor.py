from flask import Flask, request, jsonify


app = Flask(__name__)


# --- GET: obtenir tots els articles ---
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World"

@app.route('/suma', methods=['GET'])
def suma():
    numero1 = request.args.get('a')
    numero2 = request.args.get('b')
    suma = int(numero1) + int(numero2)
    return "La suma de " + numero1 + "+" + numero2 + " és = " + str(suma)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="10050")
