import os
import time

class Login:
    def __init__(self, matricula: str, senha: str) -> None:
        self.matricula_cadastrada = "0101"
        self.senha_cadastrada = "func1"
        self.matricula = matricula
        self.senha = senha
    
    
        
class Funcionario:
    def __init__(self, salario: float, transporte: bool, vale_transporte: float ) -> None:
        self.salario = salario
        self.transporte = transporte
        self.vale_transporte = vale_transporte
        
            
login_funcionario = []
trabalhador = []

def limpar_tela():
    os.system("clear")

def pausar():
    time.sleep(1)
    
def cadastro():
    matricula = input("Digite o numero da matricula: ")
    senha = input("Digite o senha: ")
    login_funcionario.append(Login(matricula, senha))
    verificacao()


    
def verificacao():
        for variavel_verificacao in login_funcionario:
            if variavel_verificacao.matricula == variavel_verificacao.matricula_cadastrada and variavel_verificacao.senha == variavel_verificacao.senha_cadastrada:
                perguntando_salario_v_transporte()
            else:
                print("matricula ou senha incorreta")
                
                    

def perguntando_salario_v_transporte():
    limpar_tela()
    salario = float(input("Digite seu salario: "))
    pergunta_transporte = input("Voce tem vale transporte: (s|n)").upper()
    if pergunta_transporte == 'S':
        transporte = True
        valor_transporte = float(input("Digite quanto voce ganha no vale transporte: "))
    else:
        transporte = False
        valor_transporte = 0
    trabalhador.append(Funcionario(salario, transporte, valor_transporte, ))


def inss():
    for salarios in trabalhador:
        salario_bruto = salarios.salario + salarios.vale_transporte
        
    if salario_bruto <= 1100.00:
        salario_inss = salario_bruto - 0.75
    elif salario_bruto >= 1100.01 and salario_bruto <=2203.48:
        salario_inss = salario_bruto - 0.9
    elif salario_bruto >= 2203.49 and salario_bruto <=3305.22:
        salario_inss = salario_bruto - 1.2
    elif salario_bruto >= 3305.23 and salario_bruto <=6433.57:
        salario_inss = salario_bruto - 1.4
    else:
        salario_inss = salario_bruto - 854.36
        
    
    
    



cadastro()
inss()





            
                
            
    
    


    
        





        
        

        
