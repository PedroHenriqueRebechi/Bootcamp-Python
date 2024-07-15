from pathlib import Path

ROOT_PATH = Path(__file__).parent 

try:
    with open(ROOT_PATH / "Exemplo.txt", "r") as exemplo: # Fecha arquivo depois de usar automaticamente
        print("Trabalhando com o arquivo")
        print(exemplo.read()) 
except IOError:
    print("Erro ao abrir arquivo")


print("-" * 50)

try:
    with open(ROOT_PATH / "Exemplo.txt", "r", encoding="utf-8") as exemplo: # Define codificação - UTF-8
        print("Trabalhando com o arquivo")
        print(exemplo.read()) 
except IOError:
    print("Erro ao abrir arquivo")