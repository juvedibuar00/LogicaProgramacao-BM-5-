# O que é uma condicional composta de múltiplas condições (if, elif, else)?
# É uma estrutura de controle que permite verificar várias condições em sequência, executando o bloco de código correspondente à primeira condição verdadeira.
# Sintaxe:
# if condição1:
#     bloco de código se condição1 for verdadeira
# elif condição2:
#     bloco de código se condição2 for verdadeira
# else:
#     bloco de código se todas as condições anteriores forem falsas
# Exemplo:
idade = 17
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")