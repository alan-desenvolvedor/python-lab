# Criando um conjunto com três itens
myset = {"apple", "banana", "cherry"}
print(myset)
# Saída: a ordem dos itens pode mudar, pois conjuntos são desordenados
# Por exemplo, pode imprimir {'banana', 'cherry', 'apple'}

# Características importantes de um conjunto:
# 1. Desordenado: os itens não têm posição fixa
# 2. Não indexado: não podemos acessar itens usando [0], [1], etc.
# 3. Itens são únicos: valores duplicados são automaticamente ignorados
# 4. Itens são imutáveis: não dá para alterar o item, mas podemos adicionar ou remover itens

# Exemplo de duplicatas sendo ignoradas
myset = {"apple", "banana", "cherry", "apple"}
print(myset)
# Saída: {'banana', 'cherry', 'apple'}
# "apple" não aparece duas vezes

# Podemos adicionar itens usando add()
myset.add("orange")
print(myset)
# Saída: {'banana', 'cherry', 'apple', 'orange'}

# Podemos remover itens usando remove() ou discard()
myset.remove("banana")  # remove o item e gera erro se não existir
myset.discard("kiwi")   # remove o item, mas não gera erro se não existir
print(myset)
# Saída: {'cherry', 'apple', 'orange'}
