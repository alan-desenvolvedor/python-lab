# Criando uma tupla
thistuple = ("apple", "banana", "cherry")

# 1. Percorrendo os itens diretamente com um for
for x in thistuple:
    print(x)
# Saída:
# apple
# banana
# cherry
# Explicação: o for pega cada item da tupla, um por um, e atribui à variável x

# 2. Percorrendo pelo índice usando range() e len()
for i in range(len(thistuple)):
    print(thistuple[i])
# Saída:
# apple
# banana
# cherry
# Explicação: len(thistuple) retorna 3, range(3) gera [0,1,2],
# e usamos o índice para acessar cada item da tupla

# 3. Usando um loop while
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
# Saída:
# apple
# banana
# cherry
# Explicação: começamos com i = 0 e vamos incrementando até i ser menor que o tamanho da tupla
