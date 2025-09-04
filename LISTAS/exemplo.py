# 1. Criação de uma lista de elementos/dados

lista = [1, 2, 3, 4, 5]

# Imprimindo a a lista
'''Para imprimir a lista completa, basta usar a função print, abre e fecha parênteses. Dentro dos parênteses, você coloca o nome da lista que deseja imprimir.'''
print(lista)
# Saída: [1, 2, 3, 4, 5]
# 2. Acessando elementos individuais da lista
'''Você pode acessar elementos individuais da lista usando índices. Os índices começam em 0, então o primeiro elemento está no índice 0, o segundo no índice 1, e assim por diante.'''
print(lista[0])  # Saída: 1
print(lista[2])  # Saída: 3
# 3. Modificando elementos da lista
'''Você pode modificar elementos individuais da lista atribuindo um novo valor ao índice correspondente.'''
lista[1] = 20
print(lista)  # Saída: [1, 20, 3, 4, 5]

# 4. Adicionando elementos à lista
'''Você pode adicionar elementos à lista usando o método append(), que adiciona um elemento ao final da lista.'''
lista.append(6)
print(lista)  # Saída: [1, 20, 3, 4, 5, 6]

# 5. Removendo elementos da lista
'''Você pode remover elementos da lista usando o método remove(), que remove a primeira ocorrência do valor especificado.'''
lista.remove(3)
print(lista)  # Saída: [1, 20, 4, 5, 6]

# 6. Iterando sobre a lista
'''Você pode iterar sobre os elementos da lista usando um loop for.'''
for elemento in lista:
    print(elemento)

# Copiando uma lista
lista_copiada = lista.copy()
print(lista_copiada)  # Saída: [1, 20, 4, 5, 6]

# Tamanho da lista
print(len(lista))  # Saída: 5

# Verificando se um elemento está na lista
print(20 in lista)  # Saída: True
print(3 in lista)   # Saída: False

# Ordenando a lista
lista.sort()
print(lista)  # Saída: [1, 4, 5, 6, 20]

# Invertendo a lista
lista.reverse()
print(lista)  # Saída: [20, 6, 5, 4, 1]

# Limpando a lista
lista.clear()
print(lista)  # Saída: []


