# Criando uma tupla
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# Acessar um item específico pelo índice
print(thistuple[1])  # 'banana' -> o segundo item (o primeiro índice é 0)

# Indexação negativa: começar do final
print(thistuple[-1]) # 'mango' -> último item
print(thistuple[-2]) # 'melon' -> penúltimo item

# Acessar uma faixa de itens (slicing)
print(thistuple[2:5])  # ('cherry', 'orange', 'kiwi') -> do índice 2 ao 4 (o 5 não entra)
print(thistuple[:4])   # ('apple', 'banana', 'cherry', 'orange') -> do início até o índice 3
print(thistuple[2:])   # ('cherry', 'orange', 'kiwi', 'melon', 'mango') -> do índice 2 até o final

# Faixa de índices negativos
print(thistuple[-4:-1]) # ('orange', 'kiwi', 'melon') -> do índice -4 até -2 (o -1 não entra)

# Verificar se um item existe na tupla
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")  # Saída: Yes, 'apple' is in the fruits tuple
