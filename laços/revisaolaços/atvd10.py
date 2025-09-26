alguem_reprovou = False

for i in range(5):
    nota = -1
    while nota < 0 or nota > 10:
        nota = float(input(f"Digite a nota do aluno {i+1} (0-10): "))
    if nota < 5.0:
        alguem_reprovou = True

if alguem_reprovou:
    print("A turma possui pelo menos um aluno reprovado.")
else:
    print("Parabéns! Todos na turma foram aprovados.")