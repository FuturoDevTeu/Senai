notas = []
media:float = 0
c=0
for c in range(4):
    notasInput = int(input(f"Digite a {c+1} nota: "))
    notas.append(notasInput)

media = sum(notas) / len(notas)

for c in range(len(notas)):
    print(f"{c+1}º nota: {notas[c]}")
    
print(f"Media: {media:.2f}")
if media >= 7:
    print("Aprovado!!")
elif media >= 5:
    print("Recuperação('-')")
else:
    print("Reprovado :(")



