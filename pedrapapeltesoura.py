import random

print("Escolha pedra, papel ou tesoura:")
usuario = input()

if usuario == "pedra" or usuario == "papel" or usuario == "tesoura":
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)

    print("Você escolheu:", usuario)
    print("Computador escolheu:", computador)

    if usuario == computador:
        print("Empate!")
    else:
        if usuario == "pedra":
            if computador == "tesoura":
                print("Você ganhou!")
            else:
                print("Computador ganhou!")
        else:
            if usuario == "papel":
                if computador == "pedra":
                    print("Você ganhou!")
                else:
                    print("Computador ganhou!")
            else:
                # usuario == "tesoura"
                if computador == "papel":
                    print("Você ganhou!")
                else:
                    print("Computador ganhou!")
else:
    print("Erro: opção inválida.")
