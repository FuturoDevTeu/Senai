def operacaomatematica(operacaoincorreta,operacao):
    while(operacaoincorreta == True):
        operacao = (input("Deseja fazer qual operacao: "))
        
        match operacao:
            case '+':
                  resultado = numero1 + numero2 
                  operacaoincorreta = False
                  return resultado,operacao
            case '-':
                  resultado = numero1 - numero2
                  operacaoincorreta = False
                  return resultado,operacao
            case '*':
                  resultado = numero1 * numero2
                  operacaoincorreta = False
                  return resultado,operacao
            case '/':
                 resultado = numero1 / numero2
                 operacaoincorreta = False
                 return resultado,operacao
            case _:
                operacaoincorreta = True
        

    

import os
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
operacao = (input("Deseja fazer qual operacao: "))

match operacao:
    case '+':
        resultado = numero1 + numero2 
    case '-':
        resultado = numero1 - numero2
    case '*':
        resultado = numero1 * numero2
    case '/':
        resultado = numero1 / numero2
    case _:
        print("Coloque uma operacao matematica correta: ")
        operacaoincorreta = True
        resultado,operacao = operacaomatematica(operacaoincorreta,operacao)

        


os.system("cls || clear")

print(f"{numero1} {operacao} {numero2} = {resultado}")

