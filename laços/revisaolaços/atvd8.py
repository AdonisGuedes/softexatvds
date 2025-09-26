despesas = []

while True:
    valor = float(input("Digite o valor da despesa (0 para encerrar): "))
    if valor == 0:
        break
    elif valor < 0:
        print("Valor inválido!")
    else:
        despesas.append(valor)

total = sum(despesas)
quantidade = len(despesas)
media = total / quantidade if quantidade > 0 else 0

print(f"Total gasto: R$ {total:.2f}")
print(f"Número de despesas: {quantidade}")
print(f"Média por despesa: R$ {media:.2f}")