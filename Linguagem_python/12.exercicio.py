numero = []
somaPositivo = 0
numeroNegativo = 0 

for c in range(10):
        numerosInput = int(input(f"Digite o {c+1}º numero: "))
        numero.append(numerosInput)
        if numerosInput >= 0:
                somaPositivo += numerosInput 
        else:
                numeroNegativo += 1

for c in range(len(numero)):
     print("Numeros: ", numero[c])
print(f"Soma de numero positivo: {somaPositivo}")
print(f"Numero negativo : {numeroNegativo}")