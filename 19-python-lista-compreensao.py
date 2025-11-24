# lista original de frutas
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# sem compreensão de lista: filtrar apenas frutas com "a"
newlist = []
for x in fruits:
    if "a" in x:  # se a fruta tiver a letra "a"
        newlist.append(x)  # adiciona à nova lista
print(newlist)
# resultado: ['apple', 'banana', 'mango']


# mesma coisa usando compreensão de lista
newlist = [x for x in fruits if "a" in x]
print(newlist)
# resultado: ['apple', 'banana', 'mango']
# sintaxe compacta: [expressão for item in iterável if condição]


# condição para excluir "apple"
newlist = [x for x in fruits if x != "apple"]
print(newlist)
# resultado: ['banana', 'cherry', 'kiwi', 'mango']


# sem filtro, apenas copiar a lista
newlist = [x for x in fruits]
print(newlist)
# resultado: ['apple', 'banana', 'cherry', 'kiwi', 'mango']


# usar range() como iterável
newlist = [x for x in range(10)]
print(newlist)
# resultado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# usar range() com condição: apenas números menores que 5
newlist = [x for x in range(10) if x < 5]
print(newlist)
# resultado: [0, 1, 2, 3, 4]


# manipular os itens: deixar todos em maiúsculas
newlist = [x.upper() for x in fruits]
print(newlist)
# resultado: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


# definir todos os valores iguais, independentemente da fruta
newlist = ['hello' for x in fruits]
print(newlist)
# resultado: ['hello', 'hello', 'hello', 'hello', 'hello']


# usar condição dentro da expressão: trocar "banana" por "orange"
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# resultado: ['apple', 'orange', 'cherry', 'kiwi', 'mango']
# aqui usamos a condição para alterar o valor somente quando x == "banana"
