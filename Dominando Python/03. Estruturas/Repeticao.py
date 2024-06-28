# EXEMPLO 1
inicio = 5
for numeros in range(inicio,11):
    print(numeros)
    inicio + 1

# EXEMPLO 2
texto = "Pedro"
vogais = "AEIOU"
for letra in texto:
    if letra.upper() in vogais:
        print(letra)
else: # Executa no final das repetições
    print('FIM')

# EXEMPLO 3
for numero in range(0,51,5): # Tabuada do cinco
    print(numero, end=" ") 

# EXEMPLO 4
# Usa-se o while quando não se sabe o número exato de vezes que o código vai ser executado
opcao = -1
while opcao != 0:
    opcao = int(input("\n[1] para sacar\n[2] para investir\n[0] para sair\nDigite:"))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print("Investindo...")
    elif opcao == 0:
        print("Saindo...")



