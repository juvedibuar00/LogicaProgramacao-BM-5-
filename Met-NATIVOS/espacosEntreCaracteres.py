nome = '   Ju ve n a l d o  Flo ren tin o   '
nome = "".join(nome.split())   # tira todos os espaços

# O que se espera com a exibição da variável nome?

# print(nome)

# Separar em palavras: "Juvenaldo" + "Florentino"
# usando regex para quebrar entre maiúsculas
import re
partes = re.findall(r'[A-Z][a-z]*', nome)
nome_corrigido = " ".join(partes)

print(nome_corrigido)  # Juvenaldo Florentino

