# Criando uma tupla simples
thistuple = ("apple", "banana", "cherry")
print(thistuple)  # ('apple', 'banana', 'cherry')

# Tuplas permitem valores duplicados
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)  # ('apple', 'banana', 'cherry', 'apple', 'cherry')

# Tuplas são ordenadas e indexadas
print(thistuple[0])  # 'apple' -> primeiro item
print(thistuple[-1]) # 'cherry' -> último item (indexação negativa)

# Comprimento da tupla
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # 3

# Criando uma tupla com apenas um item (atenção à vírgula)
thistuple = ("apple",)
print(type(thistuple))  # <class 'tuple'>

thistuple = ("apple")  # sem vírgula
print(type(thistuple))  # <class 'str'> -> não é tupla

# Tuplas podem conter diferentes tipos de dados
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)  # ('abc', 34, True, 40, 'male')

# Tuplas também podem ser criadas com o construtor tuple()
thistuple = tuple(("apple", "banana", "cherry"))  # note os parênteses duplos
print(thistuple)  # ('apple', 'banana', 'cherry')

# Tipo de dados da tupla
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))  # <class 'tuple'>
