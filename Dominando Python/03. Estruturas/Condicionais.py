# Estruturas simples
valor = 10
if valor == 10:
    print("Valor é 10")

elif valor < 10:
    print("Valor menor de 10")

else:
    print("Valor é maior que 10")

# Estruturas aninhadas
var = True
if var == True:
    if valor <= 10:
        print('Valor menor ou igual verdadeiro')
    else:
        print("Valor maior verdadeiro")


# Estruturas ternárias
status = "Sucesso" if valor >= 10 else "Falha"
print(f"{status} ao verificar valor ")