# frutas = ['maçã', 'banana', 'laranja']

# for indice, fruta in enumerate(frutas):
#     print(f'Indice {indice}: {fruta}')

x = [1, 2, 3]
y = x
z = x.copy()

print(hex(id(x)))
print(hex(id(y)))
print(hex(id(z)))