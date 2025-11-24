# Lista de exemplo
thislist = ["apple", "banana", "cherry"]

# append() -> adiciona um elemento ao final da lista
thislist.append("orange")
print(thislist)  # ['apple', 'banana', 'cherry', 'orange']

# clear() -> remove todos os elementos da lista
thislist.clear()
print(thislist)  # []

# copy() -> retorna uma cópia da lista
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)  # ['apple', 'banana', 'cherry']

# count() -> retorna quantas vezes um valor aparece na lista
print(thislist.count("banana"))  # 1

# extend() -> adiciona os elementos de outra lista no final
list2 = ["kiwi", "mango"]
thislist.extend(list2)
print(thislist)  # ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# index() -> retorna o índice da primeira ocorrência do valor
print(thislist.index("cherry"))  # 2

# insert() -> insere um elemento na posição especificada
thislist.insert(1, "orange")
print(thislist)  # ['apple', 'orange', 'banana', 'cherry', 'kiwi', 'mango']

# pop() -> remove o elemento na posição especificada (último por padrão)
thislist.pop()
print(thislist)  # ['apple', 'orange', 'banana', 'cherry', 'kiwi']

# remove() -> remove o primeiro elemento com o valor especificado
thislist.remove("orange")
print(thislist)  # ['apple', 'banana', 'cherry', 'kiwi']

# reverse() -> inverte a ordem da lista
thislist.reverse()
print(thislist)  # ['kiwi', 'cherry', 'banana', 'apple']

# sort() -> ordena a lista
thislist.sort()
print(thislist)  # ['apple', 'banana', 'cherry', 'kiwi']
