from flask import Flask, request
import crud_ps, crud_gp, crud_cp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

""" PARTICIPANTES """

# Cadastrar Participantes
@app.route('/cadps')
def cadastrar_participantes():
   params = request.args
   jogador = {
      "nome": params.get('nome'), 
      "telefone": params.get('telefone'), 
      "campeonato": params.get('campeonato')
   }
   crud_ps.inserir_paticipantes(jogador)
   return "Participante Registrado com Sucesso!"

# Consultar Participantes
@app.route('/sltps')
def consultar_participantes():
   str = crud_ps.consultar_paticipantes()
   return str

# Alterar Participantes
@app.route('/updps')
def alterar_participantes():
   params = request.args
   id = params.get('id')
   jogador = {
      "nome": params.get('nome'),
      "telefone": params.get('telefone'),
      "camp_id": params.get('campeonato')
   }
   crud_ps.editar_paticipantes(id, jogador)
   return "Participante Alterado com Sucesso!"

# Remover Participantes
@app.route('/delps')
def remover_participantes():
   params = request.args
   id_jogador = params.get('id')
   crud_ps.apagar_paticipantes(id_jogador)
   return "Participante Removido com Sucesso!"

""" GRUPOS """

# Consultar Participantes
@app.route('/cadgp')
def cadastrar_grupos():
   params = request.args
   grupo = {
      "nome_equipe": params.get('nome'), 
      "nome_I": params.get('mb1'), 
      "nome_II": params.get('mb2'),
      "nome_III": params.get('mb3'),
      "nome_IV": params.get('mb4'),
      "nome_V": params.get('mb5'),
      "telefone": params.get('telefone'),
      "camp_id": params.get('campeonato')
   }
   crud_gp.inserir_grupos(grupo)
   return "Grupo Registrado com Sucesso!"
    
""" CAMPEONATOS """

@app.route('/sltcp')
def consultar_campeonatos():
   str = crud_cp.consultar_campeonatos()
   return str

@app.route('/sltcpus')
def consultar_campeonato_usuario():
   params = request.args
   id = params.get('id')
   str = crud_ps.consultar_participante_por_id(id)
   return str

@app.route('/sltoptsus')
def consultar_campeonato_suse():
   params = request.args
   id = params.get('id')
   str = crud_cp.consultar_campeonatos_sem_pscamp(id)
   return str

if __name__ == '__main__':
    app.run(debug=True)