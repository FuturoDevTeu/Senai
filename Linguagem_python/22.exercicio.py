



def inflacao10(preco):
    return preco + (preco * 0.10)

def inflacao20(preco):
    return preco + (preco * 0.20)



def produto():
    preco = float(input("Digite o preco do produto: "))

    if preco < 100 :
        resultado=inflacao10(preco)
    else:
        resultado=inflacao20(preco)
    print(f"Resultado: {resultado}")


produto()
