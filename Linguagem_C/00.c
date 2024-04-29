import os
precoDesconto = False
precoAcresimo = False
somaPreco = 0
finalizacao = str
PrecoAdicional: int = 0
prato = []
preco = []

def menu():
        print("\n ==== MENU ==== \n")
        print("1 - lasanha   || R$: 20")
        print("2 - churrasco || R$: 35")
        print("3 - pizza     || R$: 25")
        print("4 - pudim     || R$: 10")
        print("5 - açai      || R$: 15")
        print("6 - bolo      || R$: 12")
        print("7 - coxinha   || R$: 5")
       
def receber():
        print("1 - Dinheiro")
        print("2 - cartão de crédito")
       
comecar = str(input("Olá, deseja fazer algum pedido? "))

while comecar == "sim":
    menu()
    opcao = int(input("\nQual a opção você deseja?:"))
    match opcao:
        case 1:
            prato.append("prato: 1- lasanha")
            preco.append(20)
            print(f"{prato}  || R$: {preco}")
           
        case 2:
            prato.append("prato: 2 - churrasco")
            preco.append(35)
            print(f"{prato} || R$: {preco}")
           
        case 3:
            prato.append("prato: 3 - pizza")
            preco.append(25)
            print(f"{prato} || R$: {preco}")
           
        case 4:
            prato.append("prato: 4 - pudim")
            preco.append(10)
            print(f"{prato} || R$: {preco}")
           
        case 5:
            prato.append("prato: 5 - açai")
            preco.append(15)
            print(f"{prato} || R$: {preco}")
           
        case 6:
            prato.append("prato: 6 - bolo")
            preco.append(12)
            print(f"{prato} || R$: {preco}")
           
        case 7:
            prato.append("prato: 7 - coxinha")
            preco.append(5)
            print(f"{prato} || R$: {preco}")
    
    os.system("cls || clear")
    
    somaPreco = sum(preco)

    comecar = (input("\ndeseja fazer mais um pedido? "))

receber()
finalizacao = int(input("Qual vai ser a forma de pagamento?"))
match finalizacao:
    case 1:
        precoDoDesconto= somaPreco/10
        somaPrecoDesconto = somaPreco - precoDoDesconto
        precoDesconto = True
           
    case 2:
        precoDoAcresimo= somaPreco/10
        acresimo = somaPreco + precoDoAcresimo
        precoAcresimo = True
   

subTotal = somaPreco
print()
for c in range(len(prato)):
    print(f"Prato(s) escolhido(s): {prato[c]} {preco[c]}")
print(f"Total a pagar: {somaPreco}")
print(f"subTOTAL: {subTotal}")
if precoDesconto == True:
    total = subTotal - precoDoDesconto
    print(f"Desconto: {precoDoDesconto}")
    print(f"Total: {total}")
elif precoAcresimo == True:
     total = subTotal + precoDoAcresimo
     print(f"Preço adicional: {precoDoAcresimo}")
     print(f"Total: {total}")
    
