# remover um item específico pelo valor usando remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")  # remove a primeira ocorrência de 'banana'
print(thislist)
# resultado: ['apple', 'cherry']

# se houver mais de uma ocorrência, remove apenas a primeira
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")  # remove o primeiro 'banana'
print(thislist)
# resultado: ['apple', 'cherry', 'banana', 'kiwi']


# remover um item pelo índice usando pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # remove o item no índice 1 ('banana')
print(thislist)
# resultado: ['apple', 'cherry']

# pop sem índice remove o último item
thislist = ["apple", "banana", "cherry"]
thislist.pop()  # remove 'cherry'
print(thislist)
# resultado: ['apple', 'banana']


# remover um item ou intervalo usando del
thislist = ["apple", "banana", "cherry"]
del thislist[0]  # remove o primeiro item
print(thislist)
# resultado: ['banana', 'cherry']

# del também pode excluir a lista inteira
thislist = ["apple", "banana", "cherry"]
del thislist
# a lista não existe mais, acessar thislist agora dará erro


# esvaziar a lista sem deletá-la usando clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()  # remove todos os itens
print(thislist)
# resultado: []
# a lista ainda existe, mas está vazia
