# CALCULADORA - 4 OPERAÇÕES BÁSICAS
# RECEBE DOIS NÚMEROS
# REVISÃO DO IF ELIF ELSE

while True:
    print("------- OPERAÇÕES -------")
    print("1 - SOMA (+)\n"
          "2 - SUBTRAIR (-)\n"
          "3 - MULTIPLICAÇÃO (*)\n"
          "4 - DIVISÃO (/)\n"
          "5 - SAIR")
    
    operacao = input("Escolha uma operação: ").strip().upper()

    if operacao == "5" or operacao == "SAIR":
        print("Até logo....")
        break

    print("------- NÚMEROS -------")
    numeroUm = int(input("Digite o 1º número: "))
    numeroDois = int(input("Digite o 2º número: "))
    print("-----------------------\n")  

    if operacao in ["1", "SOMA", "+"]:
        print(f"Resultado da soma: {numeroUm + numeroDois}")
    elif operacao in ["2", "SUBTRAIR", "-"]:
        print(f"Resultado da subtração: {numeroUm - numeroDois}")
    elif operacao in ["3", "MULTIPLICAÇÃO", "*"]:
        print(f"Resultado da multiplicação: {numeroUm * numeroDois}")
    elif operacao in ["4", "DIVISÃO", "/"]:
        print(f"Resultado da divisão: {numeroUm / numeroDois}")
    else:
        print("Operação inválida!")

    print("-----------------------\n")
    continuar = input("Deseja continuar? (S/N): ").strip().upper()