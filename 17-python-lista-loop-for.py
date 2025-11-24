# criar uma lista de frutas
thislist = ["apple", "banana", "cherry"]

# percorrer todos os itens usando um for loop
for x in thislist:
    print(x)
# resultado:
# apple
# banana
# cherry
# o loop passa por cada item da lista e imprime


# percorrer os itens usando seus índices
for i in range(len(thislist)):
    print(thislist[i])
# resultado:
# apple
# banana
# cherry
# aqui usamos range(len(thislist)) para gerar os índices
# e acessamos cada item pelo seu índice

# percorrer a lista usando compreensão de listas
# sintaxe curta e elegante
[print(x) for x in thislist]
# resultado:
# apple
# banana
# cherry
# a compreensão de listas aqui é usada apenas para executar print em cada item