# criando uma lista de frutas
thislist = ["apple", "banana", "cherry"]

# alterando um único item pelo índice
thislist[1] = "blackcurrant"  # substituímos 'banana' por 'blackcurrant'
print(thislist)  # resultado: ['apple', 'blackcurrant', 'cherry']


# alterar um intervalo de itens (slicing)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

# vamos trocar 'banana' e 'cherry' por 'blackcurrant' e 'watermelon'
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# resultado: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
# os itens do índice 1 e 2 foram substituídos


# inserir mais itens do que o número substituído
thislist = ["apple", "banana", "cherry"]

# substituindo apenas o segundo item ('banana') por dois novos valores
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# resultado: ['apple', 'blackcurrant', 'watermelon', 'cherry']
# o 'banana' foi substituído, e 'cherry' foi empurrado para frente
