saldo = 0
limite_saque = 0
lista = []

print("\n     SISTEMA BANCÁRIO")

while True:

    operacao = int(input("""
--------------------------                        
[1] Para depositar
[2] Para sacar
[3] Ver extrato
[4] Sair
--------------------------              
Digite: """))
    
    if operacao == 1:
        print(f"Saldo atual: {saldo}")
        deposito = float(input("Quantos R$ você quer depositar: "))
        if deposito <= 0.01:
             print("ERRO: O depósito deve ser maior que R$0.00")
             continue
        else:
            saldo += deposito
            print(f"Saldo: R${saldo}")
            lista.append(f"Depósito: R${deposito}")
            continue
    elif operacao == 2 and limite_saque <= 3:
        print(f"Saldo atual: {saldo}")
        saque = float(input("Quantos R$ você quer sacar: "))
        limite_saque += 1
        if saque < 0:
            print("\nERRO: O saque deve ser maior que R$0.00")
            continue
        elif saque > saldo:
            print("\nERRO: o saque não pode ser maior que o saldo")
            break
        elif saque > 500.00:
            print("\nERRO: não é possível sacar mais de R$500.00")
            break
        elif limite_saque > 3:
            print("\nLimite diário de saques atingido")
            continue
        else:
            saldo -= saque
            print(f"\nSaldo: R${saldo}")
            lista.append(f"Saque: R${saque}")
            continue
    elif operacao == 3:
        print("\n-----Extrato-----")
        for transacao in lista:
            print(transacao)
        print(f"\nSaldo: R${saldo}")
    elif operacao == 4:
        print("Saindo...")
        break
    elif limite_saque > 3:
        print("\nERRO: Limite diário de saques atingido")
    else:
        print("\nERRO: Informe alguma das opções fornecidas")
        break

