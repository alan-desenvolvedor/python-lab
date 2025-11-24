# Criando duas tuplas
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

# 1. Juntando duas tuplas usando o operador +
tuple3 = tuple1 + tuple2
print(tuple3)
# Saída:
# ('a', 'b', 'c', 1, 2, 3)
# Explicação: o operador + cria uma nova tupla contendo todos os itens de tuple1 seguidos pelos itens de tuple2

# 2. Multiplicando uma tupla usando o operador *
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
# Saída:
# ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
# Explicação: o operador * repete os elementos da tupla o número de vezes especificado. Aqui, repetimos 2 vezes
