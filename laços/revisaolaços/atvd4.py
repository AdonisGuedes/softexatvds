qtd_alunos = int(input("Quantos alunos na turma? "))
soma = 0

for i in range(qtd_alunos):
    nota = -1
    while nota < 0 or nota > 10:
        nota = float(input(f"Digite a nota do aluno {i+1} (0-10): "))
    soma += nota

media = soma / qtd_alunos
print(f"Média da turma: {media:.2f}")