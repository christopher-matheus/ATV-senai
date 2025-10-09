from flask import Flask, request

app = Flask(__name__)

alunos =[
    {"id": 1, "nome": "João"},
    {"id": 2, "nome": "Maria"}]

#endpoint para buscar todos os alunos
@app.route('/buscar_alunos/<int:aluno_id>/<string:nome>', methods=['GET'])
def buscar_alunos(aluno_id, nome):
    return f"O aluno: {nome}, do ID: {aluno_id}, foi encontrado"

#endpoint para adicionar um aluno
@app.route('/adicionar_aluno', methods=['POST'])
def adicionar_aluno():
    id= request.args.get('id')
    nome = request.args.get('nome')
    new = {"alunorm": id, "nome": nome}
    new["alunorm"] = len(alunos) + 1
    alunos.append(new)
    return alunos

def buscar_aluno_por_id(aluno_id):
    for aluno in alunos:
        if aluno["alunorm"] == aluno_id:
            return aluno
    return "Aluno não encontrado"

#endpoint para listar todos os alunos
@app.route('/listar_alunos', methods=['POST'])
def listar_alunos(alunos):
    return alunos

# Rodar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)