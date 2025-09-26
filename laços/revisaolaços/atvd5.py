frase = input("Digite uma frase: ").lower()

vogais = "aeiou"
qtd_vogais = 0
qtd_consoantes = 0

for letra in frase:
    if letra.isalpha():
        if letra in vogais:
            qtd_vogais += 1
        else:
            qtd_consoantes += 1

print(f"Vogais: {qtd_vogais}")
print(f"Consoantes: {qtd_consoantes}")