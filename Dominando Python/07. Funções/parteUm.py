def exibir_mensagem(): # Função básica
    print('Olá')
exibir_mensagem()

def exibir_mensagem_2(nome): # Necessita argumento ao chamar função
    print(f"Olá {nome}!")
exibir_mensagem_2("Pedro")

def exibir_mensagem_3(nome="Anônimo"): # Não necessita argumento ao chamar função
    print(f"Olá {nome}")
exibir_mensagem_3() 
exibir_mensagem_3("João")

def calcular(numeros):
    return sum(numeros)
print(calcular([2,4,5]))

def carro(nome,ano,placa):
    print(f"O nome do carro é {nome} do ano {ano} e placa {placa}")
carro("Sienna",2020,"ABC 8394") # 1ª forma
carro(nome="Sienna",ano=2020,placa="ABC 8394") # 2ª forma
carro(**{"nome": "Palio", "ano": 2022, "placa": "ADE 4785"}) # 3ª forma - dicionário

# *args(tuplas) e **kwargs(dicionários)

def exibir_poema(data, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Terça-feira, de Julho de 2024","Zen do python","Beautiful is better than ugly.", autor="Tim Peters", ano=1999 )