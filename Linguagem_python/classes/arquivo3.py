class Usuario:
    def __init__(self, nome: str, nascimento: str, rg: str, cpf: str) -> None:
        self.nome = nome
        self.nascimento = nascimento
        self.rg = rg
        self. cpf = cpf


QUANTIDADE_USUARIOS = 5
arquivo = "Funcionarios.txt"
funcionario = []

def salvar_usuario():
    with open(arquivo, "w") as registro_funcionarios:
        for acessar in funcionario:
            registro_funcionarios.write(f"Nome do funcionario: {acessar.nome} \nData de nascimento{acessar.nascimento} \nRG do funcionario: {acessar.rg} \nCPF: {acessar.cpf}")

def ler_usuario():
    with open(arquivo,'r') as registro_funcionarios:
        registros = registro_funcionarios.read()
    print(registros)

for c in range(QUANTIDADE_USUARIOS):
    funcionario.append(Usuario(
        nome = input("Digite o nome do funcionario: "),
        nascimento = input("Digite a data de nascimento: "),
        rg =  input("Digite o rg: "),
        cpf  = input("Digite o cpf: ")
    ))

    salvar_usuario()
    ler_usuario()