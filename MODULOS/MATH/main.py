from conta_numeros import contar_pares_impares

# Chama a função
resultado = contar_pares_impares()  # Por padrão, pede 4 números

# Exibe os resultados
print(f"Números pares digitados: {resultado['quant_pares']}")
print(f"Soma dos números pares: {resultado['soma_pares']}")
print(f"Números ímpares digitados: {resultado['quant_impares']}")
print(f"Soma dos números ímpares: {resultado['soma_impares']}")
print(f"Soma total de todos os números: {resultado['total']}")

