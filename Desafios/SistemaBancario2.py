from textwrap import dedent

def menu():
    menu = """\n
    ------------------MENU------------------
    [d] DEPOSITAR
    [s] SACAR
    [e] EXTRATO
    [u] CRIAR USUÁRIO
    [c] CRIAR CONTA CORRENTE
    [q] SAIR

    -> """
    return input(dedent(menu)).lower()

def depositar(saldo, valor, extrato, /): # POSITIONAL ONLY
    if valor > 0:
        saldo += valor 
        extrato += f"Depósito: R$ {valor:.2f}\n"
        
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # KEYWORD ONLY

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:   
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: -R$ {valor:.2f}\n"
        numero_saques += 1
       
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def historico(saldo, /, *, extrato): # HÍBRIDO
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = int(input("Digite seu CPF: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado")
        return
    
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço: ")

    usuarios.append({"Nome": nome, "Data de nascimento": data_nascimento,"CPF": cpf, "Endereço": endereco})
         
def filtrar_usuario(cpf, usuarios):
    filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf ]
    return filtrados[0] if filtrados else None

def criar_conta(contas):
    usuario = str(input("Digite seu nome completo: "))
    numero_conta = len(contas) + 1

    contas.append({"Usuário": usuario, "Número da conta corrente": numero_conta, "Agência": "0001"})
    print(contas)

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            deposito = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, deposito, extrato)
            print(f"Novo saldo: R$ {saldo}")
        
        elif opcao == "s":
            saque = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            print(f"Novo saldo: R$ {saldo}")

        elif opcao == "e":
            historico(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            criar_conta(contas)
            
        elif opcao == "q":
            break

        else:
            print(f"\nOpção inválida")

main()