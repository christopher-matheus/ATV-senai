from flask import Flask, request

app = Flask(__name__)

#endpoint para buscar todos os alunos
@app.route('/buscar_alunos/<int:aluno_id>/<string:nome>', methods=['GET'])
def buscar_alunos(aluno_id, nome):
    return f"O aluno: {nome}, do ID: {aluno_id}, foi encontrado"



#endpoint para adicionar um aluno
@app.route('/adicionar_aluno', methods=['POST'])
def adicionar_aluno():
    alunorm = request.args.get('alunorm')
    nome = request.args.get('nome')
    idade = request.args.get('idade')
    return f"O aluno: {nome}, do RM: {alunorm}, com a idade de: {idade} anos, foi adicionado a lista de alunos"




#endpoint para listar todos os alunos
@app.route('/listar_alunos', methods=['POST'])
def listar_alunos(alunos):
    alunos = ["Christopher", "Daniel", "Davi", "Igor", "Emanuel", "Gabriel Dutra", "João Filipe", "Roger"]
    return f"Lista de alunos: {alunos}"







# Rodar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)