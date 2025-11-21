idades = []
idade = 0 

while idade != -1:
    idade = int(input("Digite uma idade (ou -1 para encerrar): "))
    
    if idade != -1:
        idades.append(idade)

maiores = 0
for idade in idades:
    if idade >= 18:
        maiores += 1

print("Total de pessoas cadastradas:", len(idades))
print("Número de pessoas maiores de idade:", maiores)
