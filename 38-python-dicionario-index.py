# =============================
# ACESSANDO ITENS DE DICIONÁRIOS
# =============================

# Criando um dicionário
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# -----------------------------
# 1. Acessando valores diretamente pela chave
# -----------------------------
x = car["model"]
print("Valor da chave 'model':", x)
# Resultado esperado: Mustang

# -----------------------------
# 2. Usando get() para acessar valores
# -----------------------------
x = car.get("model")
print("Usando get():", x)
# Resultado esperado: Mustang

# -----------------------------
# 3. Obtendo todas as chaves com keys()
# -----------------------------
x = car.keys()
print("Chaves antes da mudança:", x)
# Resultado esperado: dict_keys(['brand', 'model', 'year'])

# Adicionando novo item ao dicionário
car["color"] = "white"
print("Chaves após adicionar 'color':", x)
# Resultado esperado: dict_keys(['brand', 'model', 'year', 'color'])
# Observação: A lista de chaves é dinâmica e reflete alterações no dicionário

# -----------------------------
# 4. Obtendo todos os valores com values()
# -----------------------------
x = car.values()
print("Valores antes da mudança:", x)
# Resultado esperado: dict_values(['Ford', 'Mustang', 1964, 'white'])

# Alterando valor existente
car["year"] = 2020
print("Valores após alterar 'year':", x)
# Resultado esperado: dict_values(['Ford', 'Mustang', 2020, 'white'])

# Adicionando um novo item
car["seats"] = 4
print("Valores após adicionar 'seats':", x)
# Resultado esperado: dict_values(['Ford', 'Mustang', 2020, 'white', 4])

# -----------------------------
# 5. Obtendo todos os itens com items()
# -----------------------------
x = car.items()
print("Itens antes da mudança:", x)
# Resultado esperado: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020), ('color', 'white'), ('seats', 4)])

# Alterando valor existente
car["brand"] = "Chevrolet"
print("Itens após alterar 'brand':", x)
# Resultado esperado: dict_items([('brand', 'Chevrolet'), ('model', 'Mustang'), ('year', 2020), ('color', 'white'), ('seats', 4)])

# Adicionando novo item
car["engine"] = "V8"
print("Itens após adicionar 'engine':", x)
# Resultado esperado: dict_items([('brand', 'Chevrolet'), ('model', 'Mustang'), ('year', 2020), ('color', 'white'), ('seats', 4), ('engine', 'V8')])

# -----------------------------
# 6. Verificando se uma chave existe
# -----------------------------
if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary")
# Resultado esperado: Yes, 'model' is one of the keys in the car dictionary
