# criando uma lista de frutas
thislist = ["apple", "banana", "cherry"]

# adicionar um item no final da lista usando append
thislist.append("orange")  # 'orange' é adicionado no final
print(thislist)
# resultado: ['apple', 'banana', 'cherry', 'orange']


# inserir um item em uma posição específica usando insert
thislist = ["apple", "banana", "cherry"]

# queremos que 'orange' fique na segunda posição (índice 1)
thislist.insert(1, "orange")
print(thislist)
# resultado: ['apple', 'orange', 'banana', 'cherry']
# os itens a partir do índice 1 foram empurrados para a direita
