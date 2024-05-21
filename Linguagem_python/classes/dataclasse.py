'''import os 
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Aluno:
    nome:str
    idade:int

QUANTIDADE_ALUNOS =2

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = int("Digite sua idade: ")
    alunos.append(Aluno(nome = nome, idade = idade))

    for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
    )
    alunos.append(aluno)


arquivo = "alunos.txt"

with open(arquivo, 'w') as arquivoDeAlunos:
    for aluno in alunos:
        arquivoDeAlunos.writer(f"{aluno.nome}, {alunos.idade} \n")
'''

class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura 
    
pessoas = []
arquivo = "arquivo.txt"

pessoas.append(Pessoa(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    peso = float(input("Digite seu peso: ")),
    altura = float(input("Digite sua altura: "))
))

with open(arquivo, 'w') as arquivoDados:
    for pessoa in pessoas:
        arquivoDados.write(f'Nome: {pessoa.nome}\n idade: {pessoa.idade}\n peso: {pessoa.peso}\n Altura: {pessoa.altura}')