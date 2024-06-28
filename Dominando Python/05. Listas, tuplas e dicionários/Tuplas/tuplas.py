# São imutáveis enquanto listas são mutáveis

exemplo = 3,4,4,5,6
print(exemplo)

# Boa prática - Colocar virgulas no final da tupla
frutas = ("Laranja","uva","maça",) 
letras = tuple("Python")
numeros = tuple([1,2,3,4])
pais = ("Brasil",)
print(numeros)
print(frutas)
print(letras)
print(pais)

# Acessar valores
print(frutas[0])
print(frutas[-1])

# Matriz 
matriz = (
    (1, "a", 2),
    ("b", 3, 5),
    (6, 5, "c")
)
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])

# Fatiamento - Mesma lógica que as listas

# MÉTODOS

print(frutas.count("Laranja"))

print(frutas.index("maça"))

print(len(frutas))

