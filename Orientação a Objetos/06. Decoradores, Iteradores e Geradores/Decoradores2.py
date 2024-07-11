import functools

def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return envelope

@duplicar # Decoradores com parametros
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()

aprender('Python')
print(aprender('Python'))

# Introspecção 
# Importar functools
print(aprender.__name__) 


# Praticando
def entrar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        senha = input("Digite a senha: ")
        if int(senha) == 1234:
            print("Logando...")
            func(*args, **kwargs)
            print("Saindo...")
        else:
            print("Senha errada")
            return
        
    return envelope

@entrar 
def logado(nome):
    menu = f"""\n
    Olá  {nome}
    ------------------MENU------------------
    [d] DEPOSITAR
    [s] SACAR
    [e] EXTRATO
    [u] CRIAR USUÁRIO
    [c] CRIAR CONTA CORRENTE
    [q] SAIR

    -> """

    print(menu)

logado("Pedro")
