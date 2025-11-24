# =============================
# DICIONÁRIOS EM PYTHON
# =============================
# Dicionários armazenam pares chave:valor
# Eles são ordenados (Python 3.7+), mutáveis e não permitem duplicatas nas chaves
# São escritos com chaves {}, e cada valor é acessado pela sua chave

# =============================
# Criando um dicionário
# =============================
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Dicionário completo:", thisdict)
# Resultado esperado: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# =============================
# Acessando valores
# =============================
# Podemos acessar valores usando a chave
print("Marca:", thisdict["brand"])
# Resultado esperado: Ford

# Também podemos usar get()
print("Modelo:", thisdict.get("model"))
# Resultado esperado: Mustang

# =============================
# Alterando valores
# =============================
thisdict["year"] = 2020
print("Dicionário após alteração:", thisdict)
# Resultado esperado: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# =============================
# Adicionando itens
# =============================
thisdict["color"] = "red"
print("Dicionário após adicionar cor:", thisdict)
# Resultado esperado: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}

# =============================
# Removendo itens
# =============================
# pop() remove item pela chave
thisdict.pop("model")
print("Após pop('model'):", thisdict)
# Resultado esperado: {'brand': 'Ford', 'year': 2020, 'color': 'red'}

# popitem() remove o último item inserido
thisdict.popitem()
print("Após popitem():", thisdict)
# Resultado esperado: {'brand': 'Ford', 'year': 2020}

# del remove item específico
del thisdict["year"]
print("Após del['year']:", thisdict)
# Resultado esperado: {'brand': 'Ford'}

# clear() limpa o dicionário
thisdict.clear()
print("Após clear():", thisdict)
# Resultado esperado: {}

# =============================
# Iterando sobre dicionários
# =============================
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Iterar pelas chaves
for key in thisdict:
    print("Chave:", key)
# Resultado esperado:
# Chave: brand
# Chave: model
# Chave: year

# Iterar pelos valores
for value in thisdict.values():
    print("Valor:", value)
# Resultado esperado:
# Valor: Ford
# Valor: Mustang
# Valor: 1964

# Iterar pelas chaves e valores
for key, value in thisdict.items():
    print(key, "->", value)
# Resultado esperado:
# brand -> Ford
# model -> Mustang
# year -> 1964

# =============================
# Verificando se uma chave existe
# =============================
if "brand" in thisdict:
    print("A chave 'brand' está presente")
# Resultado esperado: A chave 'brand' está presente

# =============================
# Copiando dicionários
# =============================
copydict = thisdict.copy()
print("Cópia do dicionário:", copydict)
# Resultado esperado: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# =============================
# Criando dicionários usando dict()
# =============================
mydict = dict(name="John", age=36, country="USA")
print("Dicionário criado com dict():", mydict)
# Resultado esperado: {'name': 'John', 'age': 36, 'country': 'USA'}
