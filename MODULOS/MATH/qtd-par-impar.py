# Inicializando contadores e somadores
quant_pares = 0
quant_impares = 0
soma_pares = 0
soma_impares = 0

for i in range(1, 5):
    numero = int(input(f"Digite o {i}º número: "))

    if numero % 2 == 0:
        quant_pares += 1      # conta pares
        soma_pares += numero  # soma pares
    else:
        quant_impares += 1      # conta ímpares
        soma_impares += numero  # soma ímpares

# Exibindo resultados
print(f"Números pares digitados: {quant_pares}")
print(f"Soma dos números pares: {soma_pares}")
print(f"Números ímpares digitados: {quant_impares}")
print(f"Soma dos números ímpares: {soma_impares}")
print(f"Soma total de todos os números: {soma_pares + soma_impares}")
