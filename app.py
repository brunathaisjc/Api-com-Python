from flask import Flask, jsonify, request

app = Flask(__name__)

albuns = [
    {
    'id': 1,
    'banda': 'Memphis May Fire',
    'album': 'The Hollow',
    'ano': '2019'
    },
    {
        'id':2,
        'banda': 'Amira Elfek',
        'album': 'Surrender',
        'ano': '2025'
    },
    {
        'id': 3,
        'banda': 'Evanescence',
        'album': 'Open The Door',
        'ano': '20012'
    },
]

# Consultar (todos)
@app.route('/albuns', methods=['GET'])

def obterAlbuns():
    return jsonify(albuns)

# Consultar (id)
@app.route('/albuns/<int:id>',methods=['GET'])

def obterAlbunsId(id):
    for albun in albuns:
        if albun.get('id') == id:
            return jsonify(albun)

# Editar livro
@app.route('/albuns/<int:id>',methods=['PUT'])

def editarAlbunId(id):
    albunAlterado = request.get_json()
    for indice, albun in enumerate(albuns):
        if albun.get('id') == id:
            albuns[indice].update(albunAlterado)
            return jsonify(albuns[indice])


@app.route('/albuns', methods=['POST'])

def incluirAlbun():
    novoAlbun = request.get_json()
    albuns.append(novoAlbun)
    return jsonify(albuns)

@app.route('/albuns/<int:id>', methods=['DELETE'])   

def excluirAlbun(id):
    for indice, albun in enumerate(albuns):
        if albun.get('id') == id:
            del albuns[indice]
    return jsonify(albuns)

app.run(host='localhost', port=5000, debug=True)