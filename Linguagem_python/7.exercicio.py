nota = [] 
soma = 0

for c in range(3):
    inputNotas = int(input(f"Digite a {c+1}ª nota "))
    nota.append(inputNotas)

    if nota [c]>= 0 and nota[c] <= 10 :
        soma += nota[c]

for c in range(3):

    while nota [c] < 0 or nota[c] > 10:
        print("nota invalida")
        nota[c]=int(input(f"Digite a {c+1}° nota: "))
        if nota [c]>= 0 and nota[c] <= 10 :
            soma += nota[c]
        
       

media = soma /2            

print(f"Media: {media}")
if media >= 7:
    print("Aprovado")
elif media > 5:
    print("Recuperacao")
else:
    print("reprovado")