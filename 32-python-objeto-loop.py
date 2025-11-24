# Criando um conjunto
thisset = {"apple", "banana", "cherry"}

# Percorrer todos os itens do conjunto com um for loop
for x in thisset:
    print(x)
# Saída: a ordem não é garantida, pode ser qualquer ordem como:
# apple
# banana
# cherry

# Verificar se um item está presente no conjunto usando 'in'
print("banana" in thisset)
# Saída: True, porque "banana" está no conjunto

# Verificar se um item NÃO está presente usando 'not in'
print("banana" not in thisset)
# Saída: False, porque "banana" está sim no conjunto
