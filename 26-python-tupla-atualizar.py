# Tuplas são imutáveis, não podemos alterar seus itens diretamente
x = ("apple", "banana", "cherry")

# Solução: converter a tupla em lista para alterar os itens
y = list(x)          # transforma tupla em lista
y[1] = "kiwi"        # altera o segundo item
x = tuple(y)          # converte de volta para tupla
print(x)              # Saída: ('apple', 'kiwi', 'cherry')

# -----------------------------
# Adicionar itens em uma tupla

# 1. Convertendo para lista e usando append
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")    # adiciona "orange" ao final da lista
thistuple = tuple(y)
print(thistuple)      # Saída: ('apple', 'banana', 'cherry', 'orange')

# 2. Adicionando tupla a tupla (mais direto)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)        # crie uma nova tupla com o item a adicionar
thistuple += y         # concatena as tuplas
print(thistuple)       # Saída: ('apple', 'banana', 'cherry', 'orange')
