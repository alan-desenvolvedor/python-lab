# =============================
# FROZENSET EM PYTHON
# =============================
# Um frozenset é uma versão imutável de um conjunto (set)
# Ele contém elementos únicos, não ordenados e não permite adição ou remoção de itens
# No entanto, suporta operações que não modificam o frozenset

# =============================
# Criando um frozenset
# =============================
x = frozenset({"apple", "banana", "cherry"})
print("Frozenset:", x)
# Resultado esperado: frozenset({'apple', 'banana', 'cherry'})  (ordem pode variar)
print("Tipo:", type(x))
# Resultado esperado: <class 'frozenset'>

# =============================
# Métodos de Frozenset
# =============================

# 1. copy() -> retorna uma cópia rasa
y = x.copy()
print("Cópia do frozenset:", y)
# Resultado esperado: frozenset({'apple', 'banana', 'cherry'})

# 2. union() / | -> retorna a união de dois frozensets
fs1 = frozenset({"a", "b", "c"})
fs2 = frozenset({1, 2, 3})
union_fs = fs1.union(fs2)
print("União:", union_fs)
# Resultado esperado: frozenset({'a', 'b', 'c', 1, 2, 3})

# Operador | funciona da mesma forma
union_fs_op = fs1 | fs2
print("União usando |:", union_fs_op)
# Resultado esperado: frozenset({'a', 'b', 'c', 1, 2, 3})

# 3. intersection() / & -> retorna elementos comuns
fs3 = frozenset({"a", "b", "x"})
intersection_fs = fs1.intersection(fs3)
print("Interseção:", intersection_fs)
# Resultado esperado: frozenset({'a', 'b'})
intersection_fs_op = fs1 & fs3
print("Interseção usando &:", intersection_fs_op)
# Resultado esperado: frozenset({'a', 'b'})

# 4. difference() -> retorna elementos do primeiro que não estão no segundo
difference_fs = fs1.difference(fs3)
print("Diferença:", difference_fs)
# Resultado esperado: frozenset({'c'})

# 5. symmetric_difference() / ^ -> elementos que estão em um ou outro, mas não em ambos
sym_diff_fs = fs1.symmetric_difference(fs3)
print("Diferença simétrica:", sym_diff_fs)
# Resultado esperado: frozenset({'c', 'x'})

# 6. isdisjoint() -> verifica se não há elementos comuns
print("fs1 e fs2 são disjuntos?", fs1.isdisjoint(fs2))
# Resultado esperado: True
print("fs1 e fs3 são disjuntos?", fs1.isdisjoint(fs3))
# Resultado esperado: False

# 7. issubset() / <= -> verifica se um frozenset é subconjunto de outro
print("fs1 é subconjunto de fs3?", fs1 <= fs3)
# Resultado esperado: False
fs4 = frozenset({"a", "b"})
print("fs4 é subconjunto de fs1?", fs4 <= fs1)
# Resultado esperado: True

# 8. issuperset() / >= -> verifica se um frozenset é superconjunto de outro
print("fs1 é superconjunto de fs4?", fs1 >= fs4)
# Resultado esperado: True
print("fs4 é superconjunto de fs1?", fs4 >= fs1)
# Resultado esperado: False

# =============================
# Observações importantes
# =============================
# - Frozensets são imutáveis: não é possível adicionar, remover ou alterar elementos
# - Permitem operações de conjunto que não modificam os frozensets originais
# - Podem ser usados como chaves de dicionário ou membros de outros conjuntos (set) porque são hashable
