from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook", "preço": 3500},
    {"id": 2, "nome": "Mouse", "preço": 50},
    {"id": 3, "nome": "Teclado", "preço": 100}
]

@app.route('/produtos')
def listar_produtos():
    return jsonify(produtos)

if __name__ == '__main__':
    app.run(port=5002)