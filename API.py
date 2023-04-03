
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        'name': 'Misael',
        'cpf': '12345678945',
        'birth': '2000-07-27'
    },
    {
        'name': 'Moacir',
        'cpf': '98765432165',
        'birth': '1999-01-05'
    }
]

@app.route('/users', methods=['GET'])
def search_all():           #devolve todos os usuários registrados
    return jsonify(users)


@app.route('/users/<name>', methods=['GET'])
def search_user(name):      #consulta um usuário registrado pelo nome    
    for user in users:
        if user.get('name') == name:
            return jsonify(user)
        
@app.route('/users', methods=['POST'])
def register_user():        #registra um novo usuário
    register = request.get_json()
    users.append(register)

    return jsonify(users)


app.run(port=5000, host='localhost', debug=True)