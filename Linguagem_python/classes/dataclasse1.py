"""Fazer ler 3 livros"""
class Livraria():
    def __init__(self,nome: str, autor: str, categoria: str, preco: float) -> None:
        self.nome = nome
        self.autor = autor
        self.categoria = categoria
        self.preco = preco

arquivo = "catalogo.txt"

livros = []

def salvar_dados():
    with open(arquivo, 'w') as catalogoDelivros:
        for livro in livros:
            catalogoDelivros.write(f'Nome do livro: {livro.nome}\nNome do autor: {livro.autor} \nCategoria: {livro.categoria}\nPreco: {livro.preco} ')

def ler_dados_catalogo():
    with open(arquivo, 'r') as catalogoDelivros:
        for livro in livros:
            registros =catalogoDelivros.read()
        print(registros)
        

livros.append(Livraria(
    nome = input("Digite o nome do livro: "),
    autor = input("Digite o nome do autor: "),
    categoria = input("Digite a categoria: "),
    preco = input("Digite o preco do livro: ")
))
salvar_dados()
ler_dados_catalogo()
