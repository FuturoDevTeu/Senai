nota = [[]]
aluno = [[]] 
media:float = 0
for l in range(3):
        alunoInput = input("Digite o nome do aluno: ")
        aluno.append(alunoInput)
        for c in range(2):
                notaInput = float(input(f"Digite a {c+1} nota de {aluno[l]}: "))
                nota.append(notaInput)
                
media = sum(nota) / len(nota)

for l in range(len(aluno)):
        print(f"Aluno: {aluno[l]}")
        for c in range(len(nota)):
                print(f"nota: {nota[l][c]} ")

print(f"Media: {media}")
