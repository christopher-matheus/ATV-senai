from flask import Flask, request

app = Flask(__name__)

#endpoint para buscar todos os alunos
@app.route('/buscar_alunos', methods=['GET'])
def buscar_alunos():
    return "todos alunos listados"









if __name__ == '__main__':
    app.run(debug=True)