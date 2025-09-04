nome = '   Ju ve n a l d o  Flo ren tin o   '
nome = "".join(nome.split())   # tira todos os espaços
# agora temos 'AnaMaria'

# vamos separar em palavras: "Ana" + "Maria"
# usando regex para quebrar entre maiúsculas
import re
partes = re.findall(r'[A-Z][a-z]*', nome)
nome_corrigido = " ".join(partes)

print(nome_corrigido)  # Ana Maria
