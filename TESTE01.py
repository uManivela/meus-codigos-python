
numeros_impares = 0
numeros_pares = 0

for numeros in range(1,11):
    numero_digitado = int(input(f'{numeros}º Numero:'))

    if numero_digitado % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

print(f"Você digitou {numeros_pares} numeros pares e {numeros_impares} numeros impares... Legal!")