import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")  # Cria banco de dados SQLite "meu_banco"
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')

nome = "Pedro"
email = "pedro@gmail.com"
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", (nome, email))
conexao.commit()