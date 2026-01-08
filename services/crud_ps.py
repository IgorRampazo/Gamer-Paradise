import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, '..', 'db', 'db_gamer_paradise.db')

def inserir_paticipantes(participante):
   con = sqlite3.connect(db_path)
   cur = con.cursor()
   sql = """INSERT INTO participantes_solo (ps_nome, ps_telefone, ps_camp_fk) 
            VALUES (?, ?, ?)"""
   cur.execute(sql, (participante['nome'], participante['telefone'], participante['campeonato']))
   con.commit()
   cur.close()
   con.close()
   
def consultar_paticipantes():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT * FROM participantes_solo")
    dados_user = cur.fetchall()
    cur.execute("SELECT * FROM campeonatos")
    dados_camp = cur.fetchall()
    cur.close()
    con.close()

    if not dados_user:
        return "Nenhum participante encontrado"

    options = ""
    for camp in dados_user:
        for i in dados_camp:
            if camp[3] == i[0]:
                options += f'<tr><td>{camp[0]}</td><td>{camp[1]}</td><td>{camp[2]}</td><td>{i[1]}</td><td><a href="./update-sl.html?id={camp[0]}" class="edt"><i class="fa-solid fa-pencil"></i></a><button class="del" value="{camp[0]}" onclick="remover_user({camp[0]})"><i class="fa-solid fa-trash"></i></button></td></tr>'
    return options

import sqlite3

def consultar_participante_por_id(participante_id):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    try:
        # Consultar os dados do participante
        cur.execute("SELECT * FROM participantes_solo WHERE ps_id = ?", (participante_id,))
        dados_user = cur.fetchone()

        if not dados_user:
            return "Participante não encontrado"

        # Consultar os dados do campeonato relacionado
        cur.execute("SELECT * FROM campeonatos WHERE cp_id = ?", (dados_user[3],))
        dados_camp = cur.fetchone()

        if dados_camp:
            option = f'{dados_user[0]}, {dados_user[1]}, {dados_user[2]}, {dados_camp[1]}, {dados_camp[0]}'
        else:
            option = "Campeonato relacionado não encontrado"

    except Exception as e:
        option = f"Erro ao consultar o banco de dados: {e}"

    cur.close()
    con.close()

    return option

def editar_paticipantes(ps_id, participante):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = """
        UPDATE participantes_solo
        SET ps_nome = ?, 
            ps_telefone = ?, 
            ps_camp_fk = ?
        WHERE ps_id = ?
    """
    cur.execute(sql, (participante['nome'], participante['telefone'], participante['camp_id'], ps_id))
    con.commit()

    cur.close()
    con.close()

def apagar_paticipantes(ps_id):
   con = sqlite3.connect(db_path)
   cur = con.cursor()
   sql = "DELETE FROM participantes_solo WHERE ps_id = ?"
   cur.execute(sql, (ps_id,))
   con.commit()
   cur.close()
   con.close()