# Parâmetros especiais - Posição e Keyword

# Posição - O argumento é definido pela posição
# Keyword - Identificar argumento ao chamar função

# Positional only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro("Palio",1999,"ABC-3942", "Fiat", motor="1.0",combustivel="Gasolina") # A keyword pode ser definida pela posição também

# Keyword only
def criar_carro(*,modelo, ano, placa, marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-3942", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Híbrido - Positional e Keyword
def criar_carro(modelo, ano, placa, /,*, marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro("Palio", 1999, "ABC-3942", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Usando funções 

# Exemplo 1
def somar(a, b):
    return a + b

def imprimir_resultado(a, b, funcao):
    resultado = funcao(a,b)
    print(resultado)

imprimir_resultado(2,3,somar)

# Exemplo 2 - Não é uma boa prática
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    print(salario)

salario_bonus(300)