numero = float(input('Digite um número, para verificar se e POSITIVO ou NEGATIVO: '))

if numero > 0:
    print(f'{numero} é um numero POSITIVO')
elif numero < 0:
    print(f'{numero} é um numero NEGATIVO')
else:
    print('O número é 0')