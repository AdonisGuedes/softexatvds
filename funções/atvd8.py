def analisar_lista(numeros):
    soma_total = sum(numeros)
    maior_numero = max(numeros)
    return (soma_total, maior_numero)

lista = [1, 7,8, 9, 10]
resultado = analisar_lista(lista)
print("Soma:", resultado[0])
print("Maior número:", resultado[1])