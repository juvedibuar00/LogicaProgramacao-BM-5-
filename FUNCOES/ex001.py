# O que é uma funaçao Python?
# Funções em Python são blocos de código reutilizáveis que realizam uma tarefa específica.
# Elas ajudam a organizar o código, tornando-o mais legível e fácil de manter.
# Funções podem receber parâmetros de entrada e retornar valores.
# Exemplo de definição e chamada de uma função:
def saudacao(nome):
    """Função que exibe uma saudação personalizada."""
    return f"Olá, {nome}!"
print(saudacao("Juvenaldo"))  # Saída: Olá, Juvenaldo!

# Funções com múltiplos parâmetros
def soma(a, b):
    """Função que retorna a soma de dois números."""
    return a + b
print(soma(5, 3))  # Saída: 8


# Funções com parâmetros padrão
def potencia(base, expoente=2):
    """Função que retorna a potência de um número. O expoente padrão é 2 (quadrado)."""
    return base ** expoente
print(potencia(4))      # Saída: 16 (4 ao quadrado)
print(potencia(4, 3))   # Saída: 64 (4 ao cubo)
