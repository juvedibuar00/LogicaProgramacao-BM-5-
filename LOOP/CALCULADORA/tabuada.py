# CRIAÇAO DE TAUBADA
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA A SUA TAUBADA ATE 10
import sys
import time
num = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada do {num}:")
for c in range(1, 11):
    print(f"{num} x {c} = {num * c}")
    time.sleep(1)

print("-----------------------FIM-----------------------")
# OU QUER VOLTAR A TAUBADA MAIS RÁPIDO? S/N
voltar = input("Deseja ver outra tabuada? (S/N): ").strip().upper()
if voltar == "S":
    # volta ao início do loop
    import os
    os.execl(sys.executable, sys.executable, *sys.argv)
else:
    print("Saindo do programa...")

 
# OU QUER VOLTAR A TAUBADA MAIS RÁPIDO? S/N
# resposta = input("Quer ver a tabuada de outro número? (S/N): ").strip().upper()
# while resposta == "S":

# num = num

# for c in range(1, 11):
#     time.sleep(0.5)
#     print(f"{num} x {c} = {num * c}")


