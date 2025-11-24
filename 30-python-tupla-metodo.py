# Criando uma tupla
mytuple = ("apple", "banana", "cherry", "apple", "cherry", "apple")

# 1. Método count()
# Conta quantas vezes um valor específico aparece na tupla
apple_count = mytuple.count("apple")
print(apple_count)
# Saída: 3
# Explicação: "apple" aparece 3 vezes na tupla

# 2. Método index()
# Retorna o índice da primeira ocorrência de um valor
cherry_index = mytuple.index("cherry")
print(cherry_index)
# Saída: 2
# Explicação: a primeira vez que "cherry" aparece está no índice 2
