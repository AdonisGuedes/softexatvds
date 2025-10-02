def contar_vogais(texto):
    vogais = "aeiouAEIOUáÁéÉíÍóÓúÚâÂêÊôÔãÃõÕ"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

frase = "Clube Náutico Capibaribe, o maior de Recife!"
print(contar_vogais(frase))