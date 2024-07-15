import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent # Diretório pai do arquivo atual

os.mkdir(ROOT_PATH / 'Novo Diretório') # Criando diretório na pasta

arquivo = open(ROOT_PATH / 'Novo-Arquivo.txt', 'w') # Criando arquivo na pasta

arquivo.close()

os.remove(ROOT_PATH / 'Novo-arquivo.txt') # Removendo arquivos