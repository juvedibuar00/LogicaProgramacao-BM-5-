# par = 0
# impar = 0

# for i in range(1,5):
#     numero = int(input(f"Digite o {i}º numero: "))

#     if numero % 2 == 0:
#         par += 1
    
#     else:
#         impar += 1

# print(f"Você digitou {par} números pares e {impar} números ímpares. A soma de todos é igual a {sum(par + impar)}.")


pares = 0
impares = 0

for i in range(1, 5):
    numero = int(input(f"Digite o {i}º número: "))

    if numero % 2 == 0:
        pares += numero   # soma os valores pares
    else:
        impares += numero # soma os valores ímpares

print(f"Soma dos números pares: {pares}")
print(f"Soma dos números ímpares: {impares}")
print(f"Soma total: {pares + impares}")
print(f"Você digitou {pares} números pares e {impares} números ímpares.")
