from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

@app.route('/testfelipelindo', methods=['GET'])
def Cliente():
    return jsonify({"message:", "Teste kkk"})

@app.route('/usuario/novo', methods=['POST'])
def Novousuario():
    novo_usuario = request.json
    print(novo_usuario)
    return jsonify({
        'user': novo_usuario,
        'message': "Usuário criado com sucesso!"  
    })



if __name__ == '__main__':
    app.run(port=3000)