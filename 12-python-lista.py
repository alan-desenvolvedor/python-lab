# criando uma lista com três frutas
lista = ["maçã", "banana", "cereja"]
print(lista)  # mostra todos os itens da lista

# acessando itens pelo índice
print(lista[0])  # primeiro item
print(lista[1])  # segundo item
print(lista[2])  # terceiro item

# listas são mutáveis: podemos trocar um valor
lista[1] = "melancia"
print(lista)  # banana virou melancia

# adicionando um item ao final da lista
lista.append("laranja")
print(lista)  # agora temos quatro frutas

# removendo um item específico
lista.remove("maçã")
print(lista)  # maçã saiu da lista

# listas permitem valores repetidos
lista2 = ["maçã", "banana", "cereja", "maçã", "cereja"]
print(lista2)  # repetimos maçã e cereja sem problemas

# podemos inserir um item em qualquer posição
lista2.insert(1, "abacaxi")
print(lista2)  # abacaxi ficou no índice 1

# podemos pegar o tamanho da lista
print(len(lista2))  # quantos itens tem na lista

# verificar se um item existe na lista
print("banana" in lista2)  # True se banana estiver presente

# ordenar a lista (alfabeticamente)
lista2.sort()
print(lista2)  # itens em ordem alfabética

# inverter a ordem da lista
lista2.reverse()
print(lista2)  # agora está de trás para frente
