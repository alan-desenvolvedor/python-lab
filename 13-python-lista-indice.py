# criando uma lista de frutas
frutas = ["maçã", "banana", "cereja", "laranja", "kiwi", "melão", "manga"]

# acesso simples pelo índice
print(frutas[1])  # mostra o segundo item da lista, que é 'banana'
# lembre-se: o primeiro item é índice 0

# indexação negativa
print(frutas[-1])  # último item da lista, 'manga'
print(frutas[-2])  # penúltimo item, 'melão'

# faixa de índices (slicing)
print(frutas[2:5])  # pega do índice 2 até o 4 (5 não incluído): ['cereja', 'laranja', 'kiwi']

# podemos omitir o início ou o fim do intervalo
print(frutas[:4])  # do início até o índice 3: ['maçã', 'banana', 'cereja', 'laranja']
print(frutas[3:])  # do índice 3 até o final: ['laranja', 'kiwi', 'melão', 'manga']

# usar índices negativos com slicing
print(frutas[-4:-1])  # pega do quarto item do fim até o penúltimo: ['laranja', 'kiwi', 'melão']
