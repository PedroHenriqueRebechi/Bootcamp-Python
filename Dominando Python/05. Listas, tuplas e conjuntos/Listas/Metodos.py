# APPEND - Acrescenta no final
lista = []
lista.append("Python")
lista.append([20,30,4])
print(lista)

# CLEAR - Apaga tudo
numeros = [2,34,63,4]
numeros.clear()
print(numeros)

# COPY
nomes = ["Pedro","Henrique"]
nomes2 = nomes.copy() # Cria lista idêntica mas não é a original
print(nomes2)

# COUNT - Conta elementos iguais
cores = ["Vermelho","Azul","Azul","Verde"]
print(cores.count("Azul"))

# EXTEND - Mescla arrays
linguagens = ["Java","JS"]
linguagens.extend(["Python", "C"])
print(linguagens)

# INDEX - Posição da primeira ocorrência
print(linguagens.index("C")) 

# POP - Remove ultimo elemento
atores = ["Bradd", "Leo", "Julius", "Andrew"]
print(atores.pop())
print(atores.pop(0)) # Ou passe o índice do elemento

# REMOVE - Remove primeira ocorrencia
atores.remove("Julius")

# REVERSE - Inverte lista
atores.reverse()

# SORT - Ordenar alfabeticamente
idades = ["Onze","Treze","Quatorze","Quinze"]
idades.sort()
print(idades)

idades.sort(reverse=True) # Inverso
print(idades)

idades.sort(key=lambda x: len(x)) # Mais extenso
print(idades)

idades.sort(key=lambda x: len(x), reverse=True)
print(idades)

# LEN
quantidades = [2,4,654,3]
print(len(linguagens))

# SORTED
sorted(idades)
print(idades)

