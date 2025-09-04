# CRIAÇAO DE TAUBADA
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA A SUA TAUBADA ATE 10
import time
while True:
    num = int(input("Digite um número para ver sua tabuada: "))
    print(f"Tabuada do {num}:")
    for c in range(1, 11):
        print(f"{num} x {c} = {num * c}")
        time.sleep(1)

    print("-----------------------FIM-----------------------")
    voltar = input("Deseja ver outra tabuada? (S/N): ").strip().upper()
    if voltar == "S":
        continue  # volta ao início do loop
    else:
        print("Saindo do programa...")
        break
# OU QUER VOLTAR A TAUBADA MAIS RÁPIDO? S/N
# resposta = input("Quer ver a tabuada de outro número? (S/N): ").strip().upper()
# while resposta == "S":

# num = num

# for c in range(1, 11):
#     time.sleep(0.5)
#     print(f"{num} x {c} = {num * c}")


