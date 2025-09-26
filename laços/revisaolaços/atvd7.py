luz_acesa = False

while True:
    acao = int(input("O que fazer? (1: apertar interruptor, 0: sair): "))

    if acao == 0:
        print("Programa encerrado.")
        break
    elif acao == 1:
        luz_acesa = not luz_acesa
        if luz_acesa:
            print("A luz está ACESA.")
        else:
            print("A luz está APAGADA.")
    else:
        print("Opção inválida.")