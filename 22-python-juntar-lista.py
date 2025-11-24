# Listas iniciais
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# 1. Usando o operador + para concatenar
list3 = list1 + list2  # cria uma nova lista sem alterar list1 ou list2
print(list3)
# resultado: ['a', 'b', 'c', 1, 2, 3]

# 2. Usando append() em um loop
# adiciona cada elemento de list2 em list1
list1 = ["a", "b", "c"]  # resetando a lista original
for x in list2:
    list1.append(x)
print(list1)
# resultado: ['a', 'b', 'c', 1, 2, 3]

# 3. Usando extend()
# adiciona todos os elementos de list2 ao final de list1 de forma direta
list1 = ["a", "b", "c"]  # resetando a lista original
list1.extend(list2)
print(list1)
# resultado: ['a', 'b', 'c', 1, 2, 3]
