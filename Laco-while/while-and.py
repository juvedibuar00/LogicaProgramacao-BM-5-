# nome = str(input("Digite seu nome: "))
# whil nome != "Juve":

#     print("Nome incorreto. Tente novamente.")
#     nome = str(input("Digite seu nome: ")) 

nome = str(input("Digite seu nome: "))

while nome != "Juve" and nome != "juve" and nome != "JUVE" and nome != "Juvenaldo":
    print("Nome incorreto. Tente novamente.")
    nome = str(input("Digite seu nome: "))
print(f"Nome correto. Bem-vindo, {nome}!")
