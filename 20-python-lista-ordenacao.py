# Lista de frutas
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# classificar a lista em ordem alfabética (crescente)
thislist.sort()  # o sort() organiza os itens da lista em ordem crescente por padrão
print(thislist)
# resultado: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Lista de números
thislist = [100, 50, 65, 82, 23]

# classificar numericamente em ordem crescente
thislist.sort()
print(thislist)
# resultado: [23, 50, 65, 82, 100]

# Classificar em ordem decrescente usando reverse=True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)  # organiza os itens do maior para o menor
print(thislist)
# resultado: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# Lista de números em ordem decrescente
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
# resultado: [100, 82, 65, 50, 23]
