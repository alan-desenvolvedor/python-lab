# =============================
# JUNÇÃO DE CONJUNTOS EM PYTHON
# =============================

# Criando dois conjuntos com diferentes tipos de dados (strings e inteiros)
set1 = {"a", "b", "c"}          # Conjunto 1 com strings
set2 = {1, 2, 3}                # Conjunto 2 com inteiros

# -----------------------------
# União de conjuntos
# -----------------------------
# Método union() cria um novo conjunto contendo todos os elementos de set1 e set2
union_set = set1.union(set2)
print("União usando union():", union_set)
# Resultado esperado: {'a', 'b', 'c', 1, 2, 3}  (ordem pode variar porque conjunto é desordenado)

# Operador | faz a mesma coisa que union()
union_set_op = set1 | set2
print("União usando | :", union_set_op)
# Resultado esperado: {'a', 'b', 'c', 1, 2, 3}  (ordem pode variar)

# -----------------------------
# União de vários conjuntos
# -----------------------------
set3 = {"John", "Elena"}        # Conjunto 3 com strings de nomes
set4 = {"apple", "banana", "cherry"}  # Conjunto 4 com frutas

# Usando union() para unir vários conjuntos de uma vez
multi_union = set1.union(set2, set3, set4)
print("União de múltiplos conjuntos usando union():", multi_union)
# Resultado esperado: {'a', 'b', 'c', 1, 2, 3, 'John', 'Elena', 'apple', 'banana', 'cherry'}

# Usando | para unir vários conjuntos
multi_union_op = set1 | set2 | set3 | set4
print("União de múltiplos conjuntos usando | :", multi_union_op)
# Resultado esperado: {'a', 'b', 'c', 1, 2, 3, 'John', 'Elena', 'apple', 'banana', 'cherry'}

# -----------------------------
# União com outros iteráveis (lista, tupla, etc.)
# -----------------------------
# Criando uma tupla com inteiros
mytuple = (10, 20, 30)

# Unindo um conjunto com a tupla usando union()
union_with_tuple = set1.union(mytuple)
print("União de conjunto com tupla:", union_with_tuple)
# Resultado esperado: {'a', 'b', 'c', 10, 20, 30}

# Criando uma lista com strings
mylist = ["kiwi", "mango"]

# Unindo um conjunto com uma lista
union_with_list = set2.union(mylist)
print("União de conjunto com lista:", union_with_list)
# Resultado esperado: {1, 2, 3, 'kiwi', 'mango'}

# -----------------------------
# Observações importantes
# -----------------------------
# 1. O método union() não altera os conjuntos originais, ele cria um novo conjunto.
# 2. O operador | é equivalente a union(), também cria um novo conjunto.
# 3. É possível unir conjuntos com qualquer iterável (lista, tupla, etc.)
# 4. Conjuntos não permitem duplicatas, então elementos repetidos serão ignorados.
