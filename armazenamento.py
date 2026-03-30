import sqlite3

def conectar():
    return sqlite3.connect("banco.db")


def carregar_funcionarios():
    conexao = conectar()
    conexao.row_factory = sqlite3.Row

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    
    dados = cursor.fetchall()

    funcionarios = [dict(d) for d in dados]

    conexao.close()
    
    return funcionarios

