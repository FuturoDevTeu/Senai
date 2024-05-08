

guardarNumeros = []
class Numero:
    def __init__(self,numeros,media):
        self.numeros = numeros
        self.media = media

def pedindoNumeros():
    c = 0 
    soma = 0
    media:float  = 0.0  
    while True:
        numeros = int(input(f"Digite o {c+1}º numero: "))

        if numeros >= 0:
            guardarNumeros.append(Numero([numeros],media))
            soma += numeros
            c += 1

        media = soma / c

        if numeros < 0:
            break

def mostrandoNumeros():
    for numero in guardarNumeros:
        print(f"Numeros: {numero.numeros}")
    print(f"Media: {numero.media:.2f}")

pedindoNumeros()
mostrandoNumeros()

        