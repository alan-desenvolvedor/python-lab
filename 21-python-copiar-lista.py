# Lista original
thislist = ["apple", "banana", "cherry"]

# 1. Usando o método copy()
mylist1 = thislist.copy()  # cria uma nova lista independente
print(mylist1)
# resultado: ['apple', 'banana', 'cherry']

# 2. Usando o construtor list()
mylist2 = list(thislist)  # também cria uma nova lista independente
print(mylist2)
# resultado: ['apple', 'banana', 'cherry']

# 3. Usando slicing (fatiamento)
mylist3 = thislist[:]  # cria uma cópia da lista usando fatia de todos os elementos
print(mylist3)
# resultado: ['apple', 'banana', 'cherry']
