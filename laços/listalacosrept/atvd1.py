nota = int(input("Digite uma nota entre 0 e 5:"))

while True: 
    if nota >= 0 and nota <= 5:
        print("Nota Válida")    
        break
    else: 
        print("A nota tem que ser entre 0 e 5")
        nota = int(input("Digite uma nota entre 0 e 5:"))
        