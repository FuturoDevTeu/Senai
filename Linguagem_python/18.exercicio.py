import os 
def logosenai():
    os.system("cls || clear")
    print("SENAI")

def calculadora():
    numero = []
    soma = 0
    media = 0.0
    for c in range(2):
        numeroInput = int(input(f"Digite o {c+1} numero: "))
        numero.append(numeroInput)
        soma+=numeroInput
    media = soma / 2
    os.system("cls || clear")
    print(f"{numero[0]} + {numero[1]} = {soma}")
    print(f"Media {media}")


logosenai()
calculadora()


