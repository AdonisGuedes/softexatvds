print("1 - Pizza - R$30")
print("2 - Suco - R$7")
print("3 - Salada - R$18")
print("4 - Sorvete - R$12")
print("5 - Café - R$5")

opcao = input("Escolha um item: ")

if opcao == "1":
    print("Você escolheu Pizza - R$30")
else:
    if opcao == "2":
        print("Você escolheu Suco - R$7")
    else:
        if opcao == "3":
            print("Você escolheu Salada - R$18")
        else:
            if opcao == "4":
                print("Você escolheu Sorvete - R$12")
            else:
                if opcao == "5":
                    print("Você escolheu Café - R$5")
                else:
                    print("Opção inválida")
