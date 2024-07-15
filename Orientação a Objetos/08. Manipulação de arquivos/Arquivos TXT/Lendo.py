# Read - Coloca o texto todo em string
file = open(r"C:\Users\Rebechi\Dio Bootcmap - Python AI Back End\Bootcamp-Python-AI-Backend-Developer\Orientação a Objetos\08. Manipulação de arquivos\Exemplo.txt", "r")
print(file.read())
file.close()

print('-'*50)

# Readline - lê uma linha por vez
file = open(r"C:\Users\Rebechi\Dio Bootcmap - Python AI Back End\Bootcamp-Python-AI-Backend-Developer\Orientação a Objetos\\08. Manipulação de arquivos\Exemplo.txt", "r")
print(file.readline()) 
file.close()

print('-'*50)
# Readlines - retorna uma lista onde cada elemento é uma linha do arquivo
file = open(r"C:\Users\Rebechi\Dio Bootcmap - Python AI Back End\Bootcamp-Python-AI-Backend-Developer\Orientação a Objetos\\08. Manipulação de arquivos\Exemplo.txt", "r")
print(file.readlines())

for linha in file.readlines(): # Para formatar a lista, use um loop
    print(linha)

file.close()
