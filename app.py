from flask import Flask, request, jsonify

app = Flask(__name__)

alunos =[
    {"id": 1, "nome": "João", "idade": 23, "endereço": "Rua A, 123"},
    {"id": 2, "nome": "Maria", "idade": 22, "endereço": "Rua B, 456"},]

#endpoint para buscar todos os alunos
@app.route('/buscar_alunos/<int:aluno_id>/<string:nome>', methods=['GET'])
def buscar_alunos(id, nome):
    return f"O aluno: {nome}, do ID: {id}, foi encontrado"

#endpoint para adicionar um aluno
@app.route('/adicionar_aluno', methods=['POST'])
def adicionar_aluno():
    id = request.args.get('id')
    nome = request.args.get('nome')
    idade = request.args.get('idade')
    endereço = request.args.get('endereço')
    new = {"id": id, "nome": nome, "idade": idade, "endereço": endereço}
    new["id"] = len(alunos) + 1
    alunos.append(new)
    return alunos

#endpoint para remover um aluno por ID
@app.route('/remover_aluno/<int:aluno_id>', methods=['DELETE'])
def remover_aluno_por_id(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return f"Aluno com ID {id} removido"
    return "Aluno não encontrado"

#endpoint para buscar um aluno por ID
def buscar_aluno_por_id(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return aluno
    return "Aluno não encontrado"

@app.route('/alterar_aluno/<int:aluno_id>', methods=['PUT'])
def alterar_aluno():
    alterado = request.get_json()
    for i, aluno in enumerate(alunos):
        if aluno["id"] == alterado["id"]:
            alunos[i] = alterado
            alunos.pop(i)
            alunos.append(alterado)
            return alunos
    return "Aluno não encontrado"
    


#endpoint para listar todos os alunos
@app.route('/listar_alunos', methods=['POST'])
def listar_alunos(alunos):
    return alunos

# Rodar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)