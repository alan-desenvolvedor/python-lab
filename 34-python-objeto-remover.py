# Criando um conjunto
thisset = {"apple", "banana", "cherry"}

# Remover um item usando remove()
thisset.remove("banana")
print(thisset)
# Saída: {'apple', 'cherry'}
# Observação: se "banana" não existir, remove() gera um erro

# Remover um item usando discard()
thisset = {"apple", "banana", "cherry"}  # recriando o conjunto
thisset.discard("banana")
print(thisset)
# Saída: {'apple', 'cherry'}
# Observação: discard() NÃO gera erro se o item não existir
