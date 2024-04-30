import os


def transformador(metro):
    centimetro = metro * 100
    return centimetro

def metro():
    metro = float(input("Digite o valor em metro: "))
    os.system("clear")
    centimetro=transformador(metro)
    print(f"Metro: {metro}")
    print(f"Em centimetro: {centimetro}")

metro()
