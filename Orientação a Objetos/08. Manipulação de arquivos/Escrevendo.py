file = open(r"C:\Users\Rebechi\Dio Bootcmap - Python AI Back End\Bootcamp-Python-AI-Backend-Developer\Orientação a Objetos\08. Manipulação de arquivos\Exemplo2.txt", "w")

file.write("Ola mundo!")
file.writelines(["\nAprendendo ", "Python"])

file.close()