while True:
    print("\n=== Caixa Eletrônico ===")
    print("1. Ver Saldo")
    print("2. Fazer Depósito")
    print("3. Fazer Saque")
    print("4. Sair")

    opcao = int(input("Escolha uma opção (0 para encerrar): "))

    if opcao == 0:
        print("Encerrando...")
        break
    elif opcao == 1:
        print("Você escolheu 'Ver Saldo'.")
    elif opcao == 2:
        print("Você escolheu 'Fazer Depósito'.")
    elif opcao == 3:
        print("Você escolheu 'Fazer Saque'.")
    elif opcao == 4:
        print("Você escolheu 'Sair'.")
    else:
        print("Opção inválida, tente novamente.")