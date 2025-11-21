numero_secreto = 42

palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número: "))
    
    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")

print("Acertou!")
