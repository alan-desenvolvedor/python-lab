# ----- STRINGS EM VÁRIAS LINHAS -----
# Permite escrever texto longo em várias linhas
texto = """Este é um texto
escrito em várias linhas
usando aspas triplas."""
print(texto)

# ----- FATIA (SLICE) DE STRING -----
s = "Olá, Mundo!"
print(s[2:5])    # caracteres da posição 2 até 4
print(s[:4])     # do início até a posição 3
print(s[3:])     # da posição 3 até o final
print(s[-6:-1])  # usa índices negativos (contando do fim)

# ----- MAIÚSCULAS E MINÚSCULAS -----
s = "Olá, Mundo!"
print(s.upper())  # transforma em maiúsculas
print(s.lower())  # transforma em minúsculas

# ----- REMOVER ESPAÇOS EXTERNOS -----
s = "   Olá, Mundo!   "
print(s.strip())   # remove espaços antes e depois

# ----- SUBSTITUIR PALAVRAS OU LETRAS -----
s = "Olá, Mundo!"
print(s.replace("Olá", "Oi"))  # troca texto por outro

# ----- DIVIDIR STRING (SPLIT) -----
s = "maçã,banana,uva"
print(s.split(","))  # divide a string onde tem vírgula

# ----- CONCATENAÇÃO (JUNTAR STRINGS) -----
a = "Olá"
b = "Mundo"
print(a + " " + b)   # junta as strings

# ----- FORMATAR STRING -----
idade = 30
print(f"Eu tenho {idade} anos")  # f-string insere valores

preco = 49.99
print(f"O preço é R${preco:.2f}")  # formata com 2 casas decimais

print(f"O total é {10 * 5}")  # faz conta dentro da f-string

# ----- CARACTERES DE ESCAPE -----
# Servem para inserir caracteres especiais
print("Ele disse: \"Olá\"")  # aspas dentro da string
print("Caminho: C:\\Users")   # barra invertida
print("Linha\nnova")          # nova linha
print("Coluna\tnova")         # tabulação
print("ABC\bD")               # backspace (apaga o anterior)
print("Texto\fNovaPágina")    # form feed (mudança de página, visual)
