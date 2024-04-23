import os

numero = []
pares = 0
impares = 0
positivos = 0
negativos = 0
c = 0
maiornumero = 0
menornumero = 99999
somaimpar = 0
somapar = 0
soma = 0
media = 0.0

for c in range(5):
    numeroInput = int(input(f"Digite o {c+1} numero: "))
    numero.append(numeroInput)
    soma += numeroInput
    if numeroInput %2 == 0: 
        somapar += numeroInput
        pares += 1
    else:
        somaimpar += numeroInput
        impares += 1
    
    if numeroInput >= 0: 
        
        positivos += 1 
    else:
        negativos += 1 
    
    if numeroInput > maiornumero:
        maiornumero = numeroInput
    
    if numeroInput < menornumero:
        menornumero = numeroInput

os.system("cls || clear")
media = soma / 5

print(f"Quantidade de numeros pares: {pares}")
print(f"Quantidade de numeros impares: {impares}")
print(f"Quantidade de numeros positivos: {positivos}")
print(f"Quantidade de numeros negativos: {negativos}")
print(f"Quantidade de numeros: {c}")
print(f"Maior numero {maiornumero}")
print(f"Menor numero {menornumero}")
print(f"Soma de numero par: {somapar}")
print(f"Soma de numero impar: {somaimpar}")
print(f"media total de numeros: {media}")
for c in range(len(numero)-1,-1,-1):
    print(numero[c])
