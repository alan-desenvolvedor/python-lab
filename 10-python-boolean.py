# -------------------------------
# COMO O PYTHON AVALIA VALORES COMO True OU False
# -------------------------------

print("=== VALORES QUE SÃO CONSIDERADOS TRUE ===")

# Qualquer string NÃO vazia é True
print(bool("abc"))   # True  -> string com conteúdo é verdadeira
print(bool("0"))     # True  -> mesmo "0" como texto é True
print(bool("Python"))# True

# Qualquer número diferente de 0 é True
print(bool(123))     # True
print(bool(-5))      # True
print(bool(3.14))    # True

# Listas, tuplas e dicionários NÃO vazios são True
print(bool(["maçã", "banana"]))  # True
print(bool((1, 2)))              # True
print(bool({"nome": "Ana"}))     # True


print("\n=== VALORES QUE SÃO CONSIDERADOS FALSE ===")

# False literal
print(bool(False))   # False

# None (ausência de valor)
print(bool(None))    # False

# Número 0 é False
print(bool(0))       # False
print(bool(0.0))     # False

# Strings vazias são False
print(bool(""))      # False
print(bool(''))      # False

# Estruturas vazias são False
print(bool(()))      # False -> tupla vazia
print(bool([]))      # False -> lista vazia
print(bool({}))      # False -> dicionário vazio
print(bool(set()))   # False -> conjunto vazio


# -------------------------------
# RESUMO (em código)
# -------------------------------

print("\n=== RESUMO ===")
print("Valores True: strings com conteúdo, números != 0, listas/tuplas/dicionários com itens.")
print("Valores False: '', 0, None, False, listas/tuplas/dicionários vazios.")
