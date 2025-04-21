# Sistema bancário - KatsBank

saldo = 1000.00
extrato = []
saques_diarios = 0

SAQUES_DIARIOS_MAXIMO = 3
LIMITE_SAQUE = 500.00


Menu = """
Bem vinda ao banco KatsBank!!!
Escolha uma das opções abaixo:
1. Depositar
2. Saque
3. Extrato
4. Sair
"""

def Deposito():
    global saldo, extrato
    try:
        valor = float(input("Digite o valor que deseja depositar: "))
    except ValueError:
        print("Valor inválido. Por favor, tente novamente.")
        return

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")
        print(f"""
        Você depositou R$ {valor:.2f}
        Seu saldo atual é R$ {saldo:.2f}
        """)
    else:
        print("Valor inválido para DEPÓSITO. Tente novamente.")
    

def Saque():
    global saldo, extrato, saques_diarios
    if saques_diarios >= SAQUES_DIARIOS_MAXIMO:
        print("Você já atingiu o limite de saques diários.")
        return

    tentativa = 0
    while tentativa < 3:
        try:
            valor = float(input("Digite o valor que deseja sacar: "))
        except ValueError:
            print("Valor inválido. Por favor, tente novamente.")
            tentativa += 1
            continue
        
        if valor > saldo:
            print("Desculpe, você não tem dinheiro suficiente para isso.")
            tentativa += 1
        elif valor > LIMITE_SAQUE:
            print(f"""
            Desculpe, você ultrpassou o limite pré estabelecido!
            O limite de saque é R$ {LIMITE_SAQUE:.2f}.""")
            tentativa += 1
        else:
            saldo -= valor
            extrato.append(f"Saque: R${valor:.2f}")
            saques_diarios += 1
            print(f"""
            Você sacou R$ {valor:.2f}
            Seu saldo atual é R$ {saldo:.2f}
            """)
            break
    else:
        print("Você excedeu o número máximo de tentativas de SAQUE.")


def Extrato():
    global saldo, extrato
    print("\n=== Extrato ===")
    
    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        print("Transações realizadas:")
        for transacao in extrato:
            print(f"- {transacao}")
    
    print("=================")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=================")



while True:
    print(Menu)
    opcao = input("Escolha uma opção: ").strip()

    match opcao:  # Corrigido para usar 'opcao'
        case "1":
            print("Você escolheu a opção 1")
            Deposito()
        case "2":
            print("Você escolheu a opção 2")
            Saque()
        case "3":
            print("Você escolheu a opção 3")
            Extrato()
        case "4":
            print("Você escolheu a opção 4")
            print("""
            Saindo do sistema...
            Obrigado por usar o KatsBank!
            """)
            break
        case _:
            print("Opção inválida. Tente novamente.")