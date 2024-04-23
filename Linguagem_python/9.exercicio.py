import os
import time

c = 0
soma = 0
terminar = True

while terminar == True:
    print("Codigo \tInformação")
    print("s \tInserir mais uma nota")
    print("p \tVer quantas notas foram inseridas")  
    print("n \tCalcular a média aritmética das notas informadas")
    opcao = input("Digite o codigo do serviço que deseja: ")

    match opcao: 
        case 's':
            notas = float(input(f"Digite a {c+1}ª nota: "))
            soma += notas
            c+=1
            os.system("cls || clear")
        case 'p':
            print(f"total de notas inseridas: {c+1}")
            time.sleep(3)
            os.system("cls || clear")
        
        case 'n':
            media = soma / c
            print(f"Media: {media:.1f}")
            terminar = False
