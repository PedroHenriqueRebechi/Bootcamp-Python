saldo = 0

while True:

    operacao = int(input("""
[1] Para depositar
[2] Para sacar
[3] Ver extrato
[4] Sair
              
Digite: """))
    
    if operacao == 1:
        deposito = float(input("Quantos R$ você quer depositar: "))
        saldo += deposito
        print(f"Saldo: R${saldo}")
        continue
    elif operacao == 2:
        saque = float(input("Quantos R$ você quer sacar: "))
        saldo -= saque
        print(f"Saldo: R${saldo}")
        continue
    elif operacao == 3:
        print(f"Saldo: R${saldo}")
    elif operacao == 4:
        print("Saindo...")
        break
    else:
        print("ERRO")
        break

