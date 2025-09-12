soma = 0

for c in range(1, 4):
    while True:
        # Explique o trecho abaixo
        # O try-except é usado para capturar erros de conversão de tipo.
        try:
            num = float(input(f"Digite o {c}º valor (entre 0 e 10): "))
            # Explique o trecho abaixo
            # Verifica se o número está dentro do intervalo permitido (0 a 10).
            if 0 <= num <= 10:
                soma += num
                break
            else:
                print("Número inválido! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

media = soma / 3
print(f"A soma dos valores é {soma:.1f} e a média é {media:.1f}")
