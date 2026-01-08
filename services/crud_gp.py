import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, '..', 'db', 'db_gamer_paradise.db')

def inserir_grupos(grupo):
   con = sqlite3.connect(db_path)
   cur = con.cursor()
   sql = """INSERT INTO participantes_grupo (pg_nome_equipe, pg_nome_I, pg_nome_II, pg_nome_III, pg_nome_IV, pg_nome_V, pg_telefone, pg_camp_fk) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
   cur.execute(sql, (
      grupo['nome_equipe'], grupo['nome_I'], grupo['nome_II'], grupo.get('nome_III'), 
      grupo.get('nome_IV'), grupo.get('nome_V'), grupo['telefone'], grupo['camp_id']
   ))
   con.commit()
   cur.close()
   con.close()

def consultar_grupos():
   con = sqlite3.connect(db_path)
   cur = con.cursor()
   cur.execute("SELECT * FROM participantes_grupo")
   dados = cur.fetchall()
   cur.close()
   con.close()
   return dados

def editar_participante_grupo(pg_id, grupo):
   con = sqlite3.connect('db_gamer_paradise.db')
   cur = con.cursor()
   sql = f"""
      UPDATE participantes_grupo
      SET pg_nome_equipe = '{grupo['nome_equipe']}', 
         pg_nome_I = '{grupo['nome_I']}', 
         pg_nome_II = '{grupo['nome_II']}',
         pg_nome_III = '{grupo.get('nome_III')}', 
         pg_nome_IV = '{grupo.get('nome_IV')}', 
         pg_nome_V = '{grupo.get('nome_V')}', 
         pg_telefone = '{grupo['telefone']}',
         pg_camp_fk = {grupo['camp_id']}
      WHERE pg_id = {pg_id}
   """
   cur.execute(sql)
   con.commit()
   cur.close()
   con.close()

def apagar_grupos(pg_id):
   con = sqlite3.connect(db_path)
   cur = con.cursor()
   sql = "DELETE FROM participantes_grupo WHERE pg_id = ?"
   cur.execute(sql, (pg_id,))
   con.commit()
   cur.close()
   con.close()