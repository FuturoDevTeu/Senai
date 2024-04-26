import os


def menuDaLanchonete():
    print("="*50)
    print("Codigo \t\tDescrição do prato \tPreço")
    print("-"*50)
    print("1 \t\tX-BURGER \t\tR$11,50")
    print("-"*50)
    print("2 \t\tX-SALADA \t\tR$12,50")
    print("-"*50)
    print("3 \t\tX-BACON \t\tR$13,00")
    print("-"*50)
    print("4 \t\tX-EGG \t\t\tR$13,50")
    print("-"*50)
    print("5 \t\tX-FRANGO \t\tR$13,50")
    print("-"*50)
    print("6 \t\tX-TUDO \t\t\tR$14,50")
    print("-"*50)
    print("7 \t\tX-TUDO DE FRANGO\tR$14,50")
    print("-"*50)
    print("0 \t\tTERMINAR O PROGRAMA")
    print("="*50)
    opcaoDeMenu = input("Digite o codigo do produto que deseja: ")
    os.system("cls || clear")
    return opcaoDeMenu

def menuDeOpcao(opcaoDoMenu, prato, preco,codigo):

    match opcaoDoMenu:
        case '1':
            prato.append("X-BURGER")
            preco.append(11.50)
            codigo.append("1")
        case '2':
            prato.append("X-SALADA")
            preco.append(12.50)
            codigo.append("2")
        case '3':
            prato.append("X-BACON")
            preco.append(13.00)
            codigo.append("3")

        case '4':
            prato.append("X-EGG")
            preco.append(13.50)
            codigo.append("4")

        case '5':
            prato.append("X-FRANGO")
            preco.append(13.50)
            codigo.append("5")

        case '6':
            prato.append("X-TUDO")
            preco.append(14.50)
            codigo.append("6")

        case '7':
            prato.append("X-TUDO DE FRANGO")
            preco.append(14.50)
            codigo.append("7")

    return prato, preco,codigo

def pagamento(precoEmTratamento):
    formaDePagamento = input("Digite a forma de pagamento (dinheiro|cartao): ")
    os.system("cls || clear")
    booleanPrecoDesconto = False
    booleanPrecoAcresimo = False
    if formaDePagamento == "dinheiro":
        precoComDesconto = precoEmTratamento * 0.10
        precoDoPratoComDesconto = precoEmTratamento - precoComDesconto
        booleanPrecoDesconto = True
        return precoDoPratoComDesconto,precoComDesconto,booleanPrecoDesconto,booleanPrecoAcresimo
        
    elif formaDePagamento == "cartao":
        precoComAcresimo = precoEmTratamento * 0.10
        precoDoPratoComAcresimo = precoEmTratamento + precoComAcresimo
        booleanPrecoAcresimo = True
        return precoDoPratoComAcresimo,precoComAcresimo,booleanPrecoDesconto,booleanPrecoAcresimo

    else:
        print("FORMA DE PAGAMENTO INVALIDA")

def conta(prato, preco, precoFinal,precoComAcresimoOuDesconto,booleanPrecoDesconto,booleanPrecoAcresimo,codigo):
    print("="*50)
    print(f"{'Codigo':<1} {'prato':^20} {'preco':>20}")
    print("_"*50)
    for c in range(len(prato)):
        print(f"{codigo[c]:<1} \t{prato[c]:^20} {'R$':>15} {preco[c]:.2f}")
        print("-"*50)
    print(f"SUBTOTAL: {sum(preco):.2f}")
    print("-"*50)
    if booleanPrecoDesconto == True:
        print(f"DESCONTO: R${precoComAcresimoOuDesconto:.2f}")
        print("-"*50)
    elif booleanPrecoAcresimo == True:
        print(f"ACRESIMO: R${precoComAcresimoOuDesconto:.2f}")
        print("-"*50)
    print(f"Total: R${precoFinal:.2f}")
    print("="*50)

preco = []
prato = []
codigo = []
opcao = ""

while True:
    opcao = menuDaLanchonete()
    prato, preco,codigo = menuDeOpcao(opcao, prato, preco,codigo)
    if opcao == "0":
        break
precoFinal,precoComAcresimoOuDesconto,booleanPrecoDesconto,booleanPrecoAcresimo = pagamento(sum(preco))
conta(prato, preco, precoFinal,precoComAcresimoOuDesconto,booleanPrecoDesconto,booleanPrecoAcresimo,codigo)