# Exemplos de conversão de tipos em Python

x = 1      # int
y = 2.8    # float
z = 1j     # complex

# converter de int para float
a = float(x)

# converter de float para int
b = int(y)

# converter de int para complex
c = complex(x)

print(a)        # 1.0
print(b)        # 2
print(c)        # (1+0j)

print(type(a))  # <class 'float'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'complex'>
