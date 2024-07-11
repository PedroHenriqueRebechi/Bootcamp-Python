# São tipos especiais de iteradores - não armazenam todos os seus valores na memória

# invés de return, utiliza-se yield

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1,2,3]):
    print(i)

# Quando saber se usar iterador ou gerador? Geradores são usados para tarefas mais simples e Iteradores para mais complexos


