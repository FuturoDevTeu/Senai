import os 
def logosenai():
    os.system("cls || clear")
    print("SENAI")

def adicao(n1,n2):
    return n1 + n2

def subtracao(n1,n2):
    return n1 - n2

def multiplicacao (n1,n2):
    return n1 * n2

def divisao(n1,n2):
    return n1 / n2

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
operacao = str(input("coloque qual tipo de operação deseja fazer: "))

if operacao == '+':
    resultado = adicao(numero1,numero2)

elif operacao == '-':
    resultado = subtracao(numero1,numero2)

elif operacao == '*':
    resultado = multiplicacao(numero1,numero2)

elif operacao == '/':
    resultado = divisao(numero1,numero2)

print(f"resultado: {resultado}")