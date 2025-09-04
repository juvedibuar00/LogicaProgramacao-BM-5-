# O que é uma tupla em Python?
# Uma tupla é uma coleção ordenada e imutável de elementos em Python. As tuplas são semelhantes às listas, mas diferem em alguns aspectos importantes:
# Imutabilidade: Uma vez criada, uma tupla não pode ser modificada (ou seja, você não pode adicionar, remover ou alterar elementos).
# Sintaxe: As tuplas são definidas usando parênteses () em vez de colchetes [].
# Uso: Tuplas são frequentemente usadas para armazenar dados que não devem ser alterados, como coordenadas, registros de banco de dados, etc.
# Exemplo:
minha_tupla = (1, 2, 3, "quatro", "cinco")
print(minha_tupla)  # Saída: (1, 2, 3, 'quatro', 'cinco')

# Acessando elementos da tupla
print(minha_tupla[0])  # Saída: 1
print(minha_tupla[3])  # Saída: quatro
print(minha_tupla[-1])  # Saída: cinco (último elemento)

# Tamanho da tupla
print(len(minha_tupla))  # Saída: 5

# Desempacotamento de tupla
a, b, c, d, e = minha_tupla
print(a)  # Saída: 1
print(d)  # Saída: quatro
print(e)  # Saída: cinco

# Tuplas aninhadas
tupla_aninhada = (1, 2, (3, 4), 5)
print(tupla_aninhada[2])  # Saída: (3, 4)
print(tupla_aninhada[2][0])  # Saída: 3 
print(tupla_aninhada[2][1])  # Saída: 4

# Métodos de tupla
# Tuplas têm poucos métodos devido à sua imutabilidade, mas aqui estão alguns úteis:
print(minha_tupla.count(2))  # Saída: 1 (conta quantas vezes o valor 2 aparece)
print(minha_tupla.index("quatro"))  # Saída: 3 (retorna o índice do primeiro valor "quatro")    

# Concatenando tuplas
outra_tupla = (6, 7, 8)
tupla_concatenada = minha_tupla + outra_tupla
print(tupla_concatenada)  # Saída: (1, 2, 3, 'quatro', 'cinco', 6, 7, 8)

# Repetindo tuplas
tupla_repetida = minha_tupla * 2
print(tupla_repetida)  # Saída: (1, 2, 3, 'quatro', 'cinco', 1, 2, 3, 'quatro', 'cinco')

# Verificando existência de um elemento
print(3 in minha_tupla)  # Saída: True
print("seis" in minha_tupla)  # Saída: False

# Iterando sobre uma tupla
for elemento in minha_tupla:
    print(elemento)
# Saída:
# 1
# 2
# 3
# quatro
# cinco

# Tuplas vs Listas
# Use tuplas quando você quiser garantir que os dados não sejam alterados. Use listas quando você precisar de uma coleção mutável.
# Tuplas são geralmente mais rápidas que listas para operações de leitura, devido à sua imutabilidade.
# No entanto, listas são mais flexíveis devido à sua capacidade de serem modificadas.
