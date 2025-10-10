from flask import Flask, request, jsonify

app = Flask(__name__)

alunos =[
    {"id": 1, "nome": "João"},
    {"id": 2, "nome": "Maria"}]

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
def remover_aluno_por_id(aluno_id):
    for aluno in alunos:
        if aluno["alunorm"] == aluno_id:
            alunos.remove(aluno)
            return f"Aluno com ID {aluno_id} removido"
    return "Aluno não encontrado"

#endpoint para buscar um aluno por ID
def buscar_aluno_por_id(aluno_id):
    for aluno in alunos:
        if aluno["id"] == aluno_id:
            return aluno
    return "Aluno não encontrado"

@app.route('/alterar_aluno/<int:aluno_id>', methods=['UPDATE'])
def alterar_aluno(aluno_id):
    for alunos in alunos:
        if alunos["id"] == aluno_id:
            alunos["nome"] = request.args.get('nome', alunos["nome"])
            alunos["idade"] = request.args.get('idade', alunos["idade"])
            alunos["endereço"] = request.args.get('endereço', alunos["endereço"])
            return f"Aluno com ID {aluno_id} alterado"


#endpoint para listar todos os alunos
@app.route('/listar_alunos', methods=['POST'])
def listar_alunos(alunos):
    return alunos

# Rodar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)