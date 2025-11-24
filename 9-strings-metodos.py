s = "python é legal"

print(s.capitalize())
# Resultado: Python é legal
# O que faz: deixa só a primeira letra maiúscula

print(s.casefold())
# Resultado: python é legal
# O que faz: converte tudo para minúsculas (mais forte que lower)

print(s.center(20))
# Resultado:    python é legal
# O que faz: centraliza o texto em um espaço de 20 caracteres

print(s.count("e"))
# Resultado: 1
# O que faz: conta quantas vezes "e" aparece

print(s.encode())
# Resultado: b'python \xc3\xa9 legal'
# O que faz: transforma a string em bytes

print(s.endswith("legal"))
# Resultado: True
# O que faz: verifica se termina com "legal"

print("Python\taí legal".expandtabs(4))
# Resultado: Python  ai legal
# O que faz: substitui TAB pelo número de espaços definido

print(s.find("é"))
# Resultado: 7
# O que faz: retorna a posição onde "é" aparece (ou -1 se não achar)

print("Olá {}".format("Mundo"))
# Resultado: Olá Mundo
# O que faz: formata inserindo valores na string

print("{x} anos".format_map({"x": 30}))
# Resultado: 30 anos
# O que faz: formata a partir de um dicionário

print(s.index("p"))
# Resultado: 0
# O que faz: retorna a posição de "p" (erro se não encontrar)


# ---- Métodos de verificação ----

print("abc123".isalnum())
# Resultado: True
# O que faz: verifica se só tem letras e números

print("abc".isalpha())
# Resultado: True
# O que faz: verifica se só tem letras

print("abc".isascii())
# Resultado: True
# O que faz: verifica se todos são caracteres ASCII

print("123".isdecimal())
# Resultado: True
# O que faz: verifica se todos são números decimais

print("123".isdigit())
# Resultado: True
# O que faz: verifica se todos são dígitos

print("var1".isidentifier())
# Resultado: True
# O que faz: verifica se é um nome válido de variável

print("ola".islower())
# Resultado: True
# O que faz: verifica se tudo está minúsculo

print("123".isnumeric())
# Resultado: True
# O que faz: verifica se é número (inclui caracteres especiais numéricos)

print("abc?".isprintable())
# Resultado: True
# O que faz: verifica se todos são caracteres imprimíveis

print("   ".isspace())
# Resultado: True
# O que faz: verifica se só tem espaços

print("Título Aqui".istitle())
# Resultado: True
# O que faz: verifica se as palavras começam com maiúscula

print("OLA".isupper())
# Resultado: True
# O que faz: verifica se tudo é maiúsculo


# ---- join ----

print("-".join(["a", "b", "c"]))
# Resultado: a-b-c
# O que faz: junta os elementos usando o separador "-"


# ---- Ajustes e transformações ----

print(s.ljust(20))
# Resultado: python é legal
# O que faz: alinha à esquerda preenchendo espaço

print(s.lower())
# Resultado: python é legal
# O que faz: transforma tudo em minúsculas

print("   teste".lstrip())
# Resultado: teste
# O que faz: remove espaços da esquerda

print(str.maketrans({"a": "@"}))
# Resultado: {97: '@'}
# O que faz: cria uma tabela de tradução

print("a-b-c".partition("-"))
# Resultado: ('a', '-', 'b-c')
# O que faz: divide a string no primeiro "-"

print(s.replace("python", "Python"))
# Resultado: Python é legal
# O que faz: substitui uma parte da string por outra

print("banana".rfind("a"))
# Resultado: 5
# O que faz: encontra a última posição de "a"

print("banana".rindex("a"))
# Resultado: 5
# O que faz: igual ao rfind, mas dá erro se não achar

print(s.rjust(20))
# Resultado:       python é legal
# O que faz: alinha à direita

print("a-b-c".rpartition("-"))
# Resultado: ('a-b', '-', 'c')
# O que faz: divide no último "-"

print("a,b,c".rsplit(","))
# Resultado: ['a', 'b', 'c']
# O que faz: divide a partir do fim

print("teste   ".rstrip())
# Resultado: teste
# O que faz: remove espaços da direita

print("a,b,c".split(","))
# Resultado: ['a', 'b', 'c']
# O que faz: divide pelo separador

print("linha1\nlinha2".splitlines())
# Resultado: ['linha1', 'linha2']
# O que faz: divide por quebras de linha

print(s.startswith("python"))
# Resultado: True
# O que faz: verifica se começa com "python"

print("   teste   ".strip())
# Resultado: teste
# O que faz: remove espaços dos dois lados

print("Python".swapcase())
# Resultado: pYTHON
# O que faz: inverte maiúsculas/minúsculas

print("ola mundo".title())
# Resultado: Ola Mundo
# O que faz: deixa a primeira letra de cada palavra maiúscula


# ---- translate ----

tabela = str.maketrans("aeiou", "12345")
print("amigo".translate(tabela))
# Resultado: 1m3g4
# O que faz: troca letras baseadas na tabela


print(s.upper())
# Resultado: PYTHON É LEGAL
# O que faz: transforma tudo em maiúsculas

print("123".zfill(5))
# Resultado: 00123
# O que faz: preenche com zeros à esquerda
