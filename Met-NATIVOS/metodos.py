# métodos nativos para manipulação de strings
# capitalize(), lower(), upper(), title(), strip(), replace(), split(), join()

'''
.lower() → converte para minúsculas

.upper() → converte para maiúsculas

.capitalize() → deixa só a primeira letra em maiúscula

.title() → coloca a primeira letra de cada palavra em maiúscula

.swapcase() → inverte maiúsculas ↔ minúsculas

.casefold() → versão mais agressiva de lower() (bom para comparações)
'''


'''
Manipulação de espaços e caracteres

.strip() → remove espaços/brancos do início e fim

.lstrip() → remove do lado esquerdo

.rstrip() → remove do lado direito

.removeprefix(prefix) → remove prefixo (se existir)

.removesuffix(suffix) → remove sufixo (se existir)
'''



''''
Substituição e formatação

.replace(old, new[, count]) → substitui partes da string

.format(*args, **kwargs) → interpolação de valores

.format_map(mapping) → como format(), mas com dicionário direto

.expandtabs(tabsize=8) → troca \t por espaços

.translate(table) → substituições baseadas em tabela (com str.maketrans())
'''