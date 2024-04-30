import os 

def logosenai():
    os.system("cls || clear")
    print("SENAI")

def tabuada():
    numero = int(input("Digite o numero que deseja fazer a tabuada: "))
    for c in range(1,11):
        print(f"{numero} * {c} = {numero * c}")

tabuada()