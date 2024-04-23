pergunta = 's'
c = 0
soma = 0

while pergunta == 's' :
    notas = float(input(f"Digite a {c+1}ª nota: "))
    soma += notas
    c+=1
    pergunta = input("deseja continuar: ")
    

media = float(soma / c)
 
print(f"Media {media}")