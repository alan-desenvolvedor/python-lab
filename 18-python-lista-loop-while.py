# criar uma lista de frutas
thislist = ["apple", "banana", "cherry"]

# percorrer a lista usando um while loop
i = 0
while i < len(thislist):  # enquanto o índice for menor que o tamanho da lista
    print(thislist[i])    # imprime o item no índice i
    i = i + 1             # incrementa o índice para não entrar em loop infinito
# resultado:
# apple
# banana
# cherry


# percorrer a lista usando compreensão de listas
# sintaxe curta e elegante
[print(x) for x in thislist]
# resultado:
# apple
# banana
# cherry
# a compreensão de listas aqui é usada apenas para executar print em cada item
