import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, '..', 'db', 'db_gamer_paradise.db')

def inserir_campeonato(campeonato):
   con = sqlite3.connect(db_path)
   cur = con.cursor()
   sql = "INSERT INTO campeonatos (cp_titulo) VALUES (?)"
   cur.execute(sql, (campeonato['titulo'],))
   con.commit()
   cur.close()
   con.close()
 
def editar_campeonato(camp_id, novo_titulo):
   con = sqlite3.connect(db_path)
   cur = con.cursor()
   sql = f"UPDATE campeonatos SET cp_titulo = '{novo_titulo}' WHERE cp_id = {camp_id}"
   cur.execute(sql)
   con.commit()
   cur.close()
   con.close()
   
def consultar_campeonatos():
   con = sqlite3.connect(db_path)
   cur = con.cursor()
   cur.execute("SELECT * FROM campeonatos")
   dados = cur.fetchall()
   cur.close()
   con.close()

   if not dados:
       return "Nenhum campeonato encontrado"

   options = ""
   for camp in dados:
      options += f'<option value="{camp[0]}">{camp[1]}</option>'
   return options

def consultar_campeonatos_sem_pscamp(id):
   con = sqlite3.connect(db_path)
   cur = con.cursor()
   cur.execute(f'SELECT * FROM campeonatos WHERE cp_id != {id}')
   dados = cur.fetchall()
   cur.close()
   con.close()

   if not dados:
       return "Nenhum campeonato encontrado"

   options = ""
   for camp in dados:
      options += f'<option value="{camp[0]}">{camp[1]}</option>'
   return options

def consultar_participantes_por_campeonato(camp_id):
   con = sqlite3.connect(db_path)
   cur = con.cursor()
   cur.execute("""
      SELECT ps_nome, ps_telefone FROM participantes_solo WHERE ps_camp_fk = ?
      UNION
      SELECT pg_nome_equipe, pg_telefone FROM participantes_grupo WHERE pg_camp_fk = ?
   """, (camp_id, camp_id))
   dados = cur.fetchall()
   cur.close()
   con.close()
   return dados