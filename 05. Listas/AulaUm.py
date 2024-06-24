#----LISTAS----

frutas = ["laranja","maçã"]
vazia = []
letras = list("Python")
numeros = list(range(10))
print(numeros)

# Acessar valores
print(frutas[0])
print(frutas[-1]) # Ultimo elemento
print(letras[2:])
print(letras[::])
print(letras[0::2])


# Matrizes
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])

# Repetição
carros = ["gol","celta","t-cross","uno"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# Compreensão de listas
numeros = [1,20,32,3,9,35]
pares = [numero for numero in numeros if numero % 2 == 0]

#for numero in numeros:     METODO ANTIGO
#   if numero % 2 == :
#   pares.append(numero)

