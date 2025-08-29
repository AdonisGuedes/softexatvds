numero = int(input("Digite um número inteiro positivo: "))

if numero <= 0:
    print("Por favor, digite um número inteiro **positivo**.")
else:
    print("Contagem regressiva de ímpares:")
    for i in range(numero, 0, -1):
        if i % 2 != 0:
            print(i)
