# Criando um conjunto
thisset = {"apple", "banana", "cherry"}

# Adicionar um item usando add()
thisset.add("orange")
print(thisset)
# Saída: {'apple', 'banana', 'cherry', 'orange'}
# Observação: a ordem não é garantida, pois sets são desordenados

# Adicionar itens de outro conjunto usando update()
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# Saída: {'apple', 'banana', 'cherry', 'orange', 'pineapple', 'mango', 'papaya'}

# Adicionar itens de qualquer iterável, como listas
mylist = ["kiwi", "orange"]  # "orange" já existe, será ignorado
thisset.update(mylist)
print(thisset)
# Saída: {'apple', 'banana', 'cherry', 'orange', 'pineapple', 'mango', 'papaya', 'kiwi'}
