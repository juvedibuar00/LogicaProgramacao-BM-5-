# conta_numeros.py

def contar_pares_impares(qtd_numeros=4):
    """
    Solicita ao usuário a entrada de números e retorna a quantidade e soma de pares e ímpares.
    
    Parâmetros:
    qtd_numeros (int): Quantidade de números que serão digitados (padrão=4)
    
    Retorna:
    dict: Contendo 'quant_pares', 'soma_pares', 'quant_impares', 'soma_impares', 'total'
    """
    quant_pares = 0
    quant_impares = 0
    soma_pares = 0
    soma_impares = 0

    for i in range(1, qtd_numeros + 1):
        numero = int(input(f"Digite o {i}º número: "))

        if numero % 2 == 0:
            quant_pares += 1
            soma_pares += numero
        else:
            quant_impares += 1
            soma_impares += numero

    total = soma_pares + soma_impares

    return {
        "quant_pares": quant_pares,
        "soma_pares": soma_pares,
        "quant_impares": quant_impares,
        "soma_impares": soma_impares,
        "total": total
    }
