print("\n===== 1. OPERADORES ARITMÉTICOS =====")
print("Soma: adiciona valores")
print(15 + 4, "→ resultado da soma 15 + 4")

print("Subtração: retira um valor do outro")
print(15 - 4, "→ resultado da subtração 15 - 4")

print("Multiplicação: multiplica os valores")
print(15 * 4, "→ resultado da multiplicação 15 * 4")

print("Divisão: divide e retorna número decimal")
print(15 / 4, "→ resultado da divisão 15 / 4")

print("Módulo: mostra o RESTO da divisão")
print(15 % 4, "→ resto da divisão 15 % 4")

print("Exponenciação: potencia (eleva um número ao outro)")
print(15 ** 4, "→ 15 elevado a 4")

print("Divisão inteira: divide e remove as casas decimais")
print(15 // 4, "→ divisão inteira de 15 // 4")


print("\n===== 2. OPERADORES DE ATRIBUIÇÃO =====")
a = 10
a += 3
print(a, "→ += adiciona e salva o resultado na variável")

a = 10
a -= 3
print(a, "→ -= subtrai e salva")

a = 10
a *= 3
print(a, "→ *= multiplica e salva")

a = 10
a /= 2
print(a, "→ /= divide e salva (vira float)")

a = 10
a %= 4
print(a, "→ %= pega o resto da divisão e salva")

a = 10
a //= 3
print(a, "→ //= faz divisão inteira e salva")

a = 3
a **= 3
print(a, "→ **= eleva ao quadrado e salva")


print("\n===== 3. OPERADOR WALRUS (:=) =====")
numeros = [1, 2, 3, 4, 5]

if (quantidade := len(numeros)) > 3:
    print(quantidade, "→ ':=' atribui e usa o valor ao mesmo tempo")


print("\n===== 4. OPERADORES DE COMPARAÇÃO =====")
print(5 == 3, "→ verifica se os valores são iguais")
print(5 != 3, "→ verifica se são diferentes")
print(5 > 3,  "→ verifica se é maior")
print(5 < 3,  "→ verifica se é menor")
print(5 >= 3, "→ maior ou igual")
print(5 <= 3, "→ menor ou igual")


print("\n===== 5. OPERADORES LÓGICOS =====")
print(5 > 0 and 5 < 10, "→ AND só é verdadeiro se as duas condições forem verdadeiras")
print(5 < 5 or 5 > 10, "→ OR é verdadeiro se pelo menos uma condição for verdadeira")
print(not(5 > 3 and 5 < 10), "→ NOT inverte o resultado da expressão")


print("\n===== 6. OPERADORES DE IDENTIDADE =====")
lista1 = ["maçã", "banana"]
lista2 = ["maçã", "banana"]
lista3 = lista1

print(lista1 is lista3, "→ verifica se são o MESMO objeto na memória")
print(lista1 is lista2, "→ mesmo conteúdo mas objetos diferentes")
print(lista1 == lista2, "→ conteúdo igual, por isso True")
print(lista1 is not lista2, "→ objetos diferentes, por isso True")


print("\n===== 7. OPERADORES DE ASSOCIAÇÃO =====")
frutas = ["maçã", "banana", "uva"]

print("banana" in frutas, "→ verifica se o item está dentro da lista")
print("abacaxi" not in frutas, "→ verifica se o item NÃO está na lista")

texto = "Hello World"
print("H" in texto, "→ verifica se uma letra está na string")
print("hello" in texto, "→ é sensível a maiúsculas e minúsculas")
print("z" not in texto, "→ 'z' não aparece no texto")


print("\n===== 8. OPERADORES BITWISE (BINÁRIOS) =====")
print("6 = 0110 em binário")
print("3 = 0011 em binário")

print(6 & 3, "→ AND compara bit a bit e retorna 1 só quando os dois são 1")
print(6 | 3, "→ OR retorna 1 quando pelo menos um dos bits é 1")
print(6 ^ 3, "→ XOR retorna 1 quando os bits são diferentes")
print(~6,    "→ NOT inverte todos os bits")
print(6 << 1, "→ desloca bits para a esquerda, multiplicando por 2")
print(6 >> 1, "→ desloca bits para a direita, dividindo por 2")


print("\n===== 9. PRECEDÊNCIA DE OPERADORES =====")
print((6 + 3) - (6 + 3),
      "→ expressões dentro de parênteses são resolvidas primeiro")

print(100 + 5 * 3,
      "→ multiplicação é feita antes da soma")


print("\n===== 10. AVALIAÇÃO DA ESQUERDA PARA DIREITA =====")
print(5 + 4 - 7 + 3,
      "→ quando operadores têm a mesma prioridade, Python resolve da esquerda para a direita")
