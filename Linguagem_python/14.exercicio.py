numero = []
o = 6

for c in range(6):
    while True:
        numeroInput = int(input(f"Digite o {c+1} numero: "))

        if numeroInput %2 == 0 and numeroInput > 0:
            numero.append(numeroInput)
            break
        else:
            print("Erro!!")
            numeroInput = int(input(f"Digite o {c+1} numero: "))


for c in range(len(numero)-1,-1,-1):
    print(numero[c]) 