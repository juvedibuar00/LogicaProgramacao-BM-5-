
def soma(a, b):
    soma = a + b
    print(f"A soma entre {a} e {b} é igual a {soma}")
soma(4, 5)  # Saída: A soma entre 4 e 5 é igual a 9


def subtracao(a, b):
    subtracao = a - b
    print(f"A subtração entre {a} e {b} é igual a {subtracao}")
subtracao(10, 3)  # Saída: A subtração entre 10 e 3 é igual a 7

def multiplicacao(a, b):
    multiplicacao = a * b
    print(f"A multiplicação entre {a} e {b} é igual a {multiplicacao}")
multiplicacao(4, 5)  # Saída: A multiplicação entre 4 e 5 é igual a 20

def divisao(a, b):
    divisao = a / b
    print(f"A divisão entre {a} e {b} é igual a {divisao}")
divisao(20, 4)  # Saída: A divisão entre 20 e 4 é igual a 5.0

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
print(f"O fatorial de 5 é {fatorial(5)}")  # Saída: O fatorial de 5 é 120

# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         seq = [0, 1]
#         for i in range(2, n):
#             next_value = seq[-1] + seq[-2]
#             seq.append(next_value)
#         return seq
# print(f"A sequência de Fibonacci com 10 termos é: {fibonacci(10)}")  # Saída: A sequência de Fibonacci com 10 termos é: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  