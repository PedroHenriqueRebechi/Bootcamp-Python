import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")  # Cria banco de dados SQLite "meu_banco"
cursor = conexao.cursor()

# CRIANDO TABELA
# cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

atualizar_registro(conexao, cursor, "Pedro Henrique", "p01edro@gmail.com", 1) 

def deletar_registro(conexao, cursor, id):
    data = (id, )
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

deletar_registro(conexao, cursor, 2)

def inserir_lote(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    conexao.commit()

dados = [("Guilherme", "Gui@gmail.com"), ("Julia", "Ju@gmail.com")]
inserir_lote(conexao, cursor, dados)

def recuperar_cliente(cursor, id):
    cursor.row_factory = sqlite3.Row  # Extra - ROW FACTORY 
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

cliente = recuperar_cliente(cursor, 1)
print(dict(cliente)) # Extra - ROW FACTORY

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;")

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)



