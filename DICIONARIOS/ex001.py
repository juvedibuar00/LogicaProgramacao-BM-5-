# O que é dicionário em Python
# Dicionários em Python são estruturas de dados que armazenam pares de chave-valor.
# Eles são mutáveis, o que significa que você pode alterar, adicionar ou remover itens após a criação do dicionário.
# Dicionários são úteis para armazenar dados que precisam ser acessados por uma chave única
# Exemplo:
pessoa = {"nome": "Juvenaldo", "idade": 30, "cidade": "São Paulo"}
print(pessoa)  # Saída: {'nome': 'Juvenaldo', 'idade': 30, 'cidade': 'São Paulo'}
print(pessoa["nome"])  # Saída: Juvenaldo

# Como adicionar itens a um dicionário
pessoa["profissão"] = "Engenheiro"
print(pessoa)  # Saída: {'nome': 'Juvenaldo', 'idade': 30, 'cidade': 'São Paulo', 'profissão': 'Engenheiro'}

# Como remover itens de um dicionário
del pessoa["idade"]
print(pessoa)  # Saída: {'nome': 'Juvenaldo', 'cidade': 'São Paulo', 'profissão': 'Engenheiro'}

# Como iterar sobre um dicionário
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
# Saída:
# nome: Juvenaldo
# cidade: São Paulo
# profissão: Engenheiro

# Como verificar se uma chave existe em um dicionário
if "nome" in pessoa:
    print("A chave 'nome' existe no dicionário.")
# Saída: A chave 'nome' existe no dicionário.

# Métodos úteis para dicionários
# .keys() - Retorna uma lista das chaves no dicionário
print(pessoa.keys())  # Saída: dict_keys(['nome', 'cidade', 'profissão'])

# .values() - Retorna uma lista dos valores no dicionário
print(pessoa.values())  # Saída: dict_values(['Juvenaldo', 'São Paulo', 'Engenheiro'])

# .items() - Retorna uma lista de tuplas, cada uma contendo um par chave-valor
print(pessoa.items())  # Saída: dict_items([('nome', 'Juvenaldo'), ('cidade', 'São Paulo'), ('profissão', 'Engenheiro')])

# .get() - Retorna o valor para a chave especificada, ou None se a chave não existir
print(pessoa.get("idade"))  # Saída: None
print(pessoa.get("nome"))  # Saída: Juvenaldo

# .clear() - Remove todos os itens do dicionário
pessoa.clear()
print(pessoa)  # Saída: {}

# .copy() - Retorna uma cópia rasa do dicionário
pessoa = {"nome": "Juvenaldo", "idade": 30, "cidade": "São Paulo"}
pessoa_copia = pessoa.copy()
print(pessoa_copia)  # Saída: {'nome': 'Juvenaldo', 'idade': 30, 'cidade': 'São Paulo'}

# .update() - Atualiza o dicionário com os pares chave-valor de outro dicionário
pessoa.update({"idade": 31, "profissão": "Engenheiro"})
print(pessoa)  # Saída: {'nome': 'Juvenaldo', 'idade': 31, 'cidade': 'São Paulo', 'profissão': 'Engenheiro'}

# pop() - Remove o item com a chave especificada e retorna o valor
idade = pessoa.pop("idade")
print(idade)  # Saída: 31
print(pessoa)  # Saída: {'nome': 'Juvenaldo', 'cidade': 'São Paulo', 'profissão': 'Engenheiro'}

# popitem() - Remove e retorna um par chave-valor arbitrário como uma tupla
item = pessoa.popitem()
print(item)  # Saída: ('profissão', 'Engenheiro')
print(pessoa)  # Saída: {'nome': 'Juvenaldo', 'cidade': 'São Paulo'}

# Tamanho do dicionário
print(len(pessoa))  # Saída: 2
# Saída: 2

# Limpando o dicionário
pessoa.clear()
print(pessoa)  # Saída: {}

