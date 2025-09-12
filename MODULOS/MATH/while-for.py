# Programa que recebe 5 valores, calcula a soma e a média dos valores válidos (entre 0 e 10).
soma = 0
for c in range(1, 6):
    while True:
        try:
            num = float(input(f"Digite o {c}º valor (entre 0 e 10): "))
            if 0 <= num <= 10:
                soma += num
                break
            else:
                print("Número inválido! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")