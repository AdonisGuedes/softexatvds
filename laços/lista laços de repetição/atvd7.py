numero = int(input("Digite um número de 0 a 100: "))

listanumero = []

while True:
    listanumero.append(numero)
    numero = int(input("Digite o proximo numero: "))
    if numero == 101:
        print(min(listanumero))
        break