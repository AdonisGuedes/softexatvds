while True:
    nome = input("Digite o nome (mínimo 4 caracteres): ")
    if len(nome) < 4:
        print("Nome inválido. Deve ter pelo menos 4 caracteres.")
    else:
        break

while True:
    idade = int(input("Digite a idade (1 a 100): "))
    if idade < 1 or idade > 100:
        print("Idade inválida.")
    else:
        break

while True:
    salario = float(input("Digite o salário (maior que 0): "))
    if salario <= 0:
        print("Salário inválido.")
    else:
        break

while True:
    genero = input("Digite o gênero (m, f ou o): ")
    if genero != 'm' and genero != 'f' and genero != 'o':
        print("Gênero inválido.")
    else:
        break

while True:
    situempreg = input("Digite a situação empregatícia (e, d ou a): ")
    if situempreg != 'e' and situempreg != 'd' and situempreg != 'a':
        print("Situação inválida.")
    else:
        break