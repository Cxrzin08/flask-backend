from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=[])

usuarios = []

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Hello, world!'})

@app.route('/usuario/novo', methods=['POST'])
def criar_novo_usuario():
    novo_usuario = request.json
    usuarios.append(novo_usuario)
    return jsonify({
        'user': novo_usuario,
        'message': 'Usuário criado com sucesso!'
    })

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify({'usuarios': usuarios})

if __name__ == '__main__':
    app.run(port=5000)
