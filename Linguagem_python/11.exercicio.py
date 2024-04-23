 

numero = []

for c in range(5):
    numeroInput = int(input(f"Digite o {c+1}º numero: "))
    numero.append(numeroInput)

for c in range(len(numero)):
    print(f"{numero[c]}")

print(f"Maior numero {max(numero)}")
print(f"Menor numero {min(numero)}") 