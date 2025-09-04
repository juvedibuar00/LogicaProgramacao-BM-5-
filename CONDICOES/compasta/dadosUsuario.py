
# idade = str(input("Digite sua idade: "))
# if not idade.isdigit():
#     print("Valor inválido. Por favor, insira um número.")
# else:
#     idade = int(idade)
#     if idade >= 18:
#         print("Você é maior de idade.")
#     else:
#         print("Você é menor de idade.")
# # Como funciona o código acima?
# 1. Solicita ao usuário que insira sua idade.
# 2. Verifica se a entrada é composta apenas por dígitos usando isdigit().
# 3. Se a entrada não for um número válido, exibe uma mensagem de erro
# # 4. Se for válida, converte a entrada para um inteiro e verifica se o usuário é maior ou menor de idade, exibindo a mensagem correspondente.

# # Como voltar a versão anterior, quando o valor digitado é errado?
# # Podemos usar um loop para continuar solicitando a entrada até que o usuário insira um valor válido.
# # Exemplo:
# while True:
#     idade = str(input("Digite sua idade: "))
#     if not idade.isdigit():
#         print("Valor inválido. Por favor, insira um número.")
#     else:
#         idade = int(idade)
#         if idade >= 18:
#             print("Você é maior de idade.")
#         else:
#             print("Você é menor de idade.")
#         break
# Nesse exemplo, o loop while True continuará solicitando a idade até que o usuário insira um valor válido. Quando um valor válido é inserido, o loop é interrompido com break.
