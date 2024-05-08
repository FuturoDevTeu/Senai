class PerfilAluno:
    def __init__(self,aluno,nota,media):
        self.aluno = aluno
        self.nota = nota
        self.media = media
nota = []
boletin = []
def perguntando():
    aluno = input("Digite o nome do aluno: ")
    for c in range(4):
        notas = int(input(f"Digite a {c+1} nota: "))
        nota.append(notas)
    media = sum(nota) / len(nota)
    boletin.append(PerfilAluno(aluno,nota,media))

def mostrar():
    for alunos in boletin:
        print(f"ALUNO: {alunos.aluno.upper()}")
        for c in range(len(alunos.nota)):
             print(f"NOTAS {c+1}: {alunos.nota[c]}") 
        print(f"MEDIA: {alunos.media}")
        if alunos.media >=7:
            print("Aprovado")
        elif alunos.media >=5:
            print("Recuperacao")
        else:
            print("Reprovado")

perguntando()
mostrar()
