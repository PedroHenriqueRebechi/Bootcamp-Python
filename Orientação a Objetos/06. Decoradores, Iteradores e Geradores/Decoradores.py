# Recapitulando - As funções em python são de primeira classe ou seja podem ser usadas como parametros

def cantar(musica):
    print(f"A mulher começa a cantar {musica.title()}")
    return f"Cantando.."

def gritar(musica):
    print(f"A mulher começa a gritar ao cantar {musica.title()}")
    return f"Gritando.."

def exibir_funcao(funcao, musica):
    print("Executando...")
    return funcao(musica)

exibir_funcao(cantar,"o sol")
exibir_funcao(gritar,"O Sol")
print(exibir_funcao(cantar, "O Sol"))
print(exibir_funcao(gritar, "O Sol"))

print('-' * 50)

# Inner functions - Funções dentro de outras funções

def principal():
    print("Executando principal")

    def funcao_interna():
        print("Função interna")

    funcao_interna()

principal()
#funcao_interna() - Não existe fora da função principal

print('-' * 50)

def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao: # Nova forma de escrever - if operacao == "+"
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div


op = calculadora("+")(2, 2) # Mesma saída
print(op)

op = calculadora("-") # Mesma saída
print(op(2, 2))

op = calculadora("*")
print(op(2, 2))

op = calculadora("/")
print(op(2, 2))

print('-' * 50)

# Decoradores 

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar função")
        funcao()
        print("Faz algo depois de executar função")
    
    return envelope

@meu_decorador # Forma fácil de chamar o decorador
def ola():
    print("Olá mundo")

ola()



