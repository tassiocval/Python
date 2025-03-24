nome = 'Tassio'
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))

if n1 > n2 :
    print(f'{nome} o numero {n1}, e maior que o {n2}')
elif n2 > n1 :
    print(f'{nome} o numero {n2}, e maior que o {n1}')
else:
    print(f'{nome}, digite um número valído!')