'''if 5 != 7 and 6 == 6:
    print('Ola')
    print('tudo bem')

print('Até mais!')
'''

'''
nome = input('Digite seu nome: ')

if nome == 'Tassio':
    print(f'Seja Bem Vindo {nome}')
else:
    print(f'Nao conheço {nome}')

print('Até mais!')'''

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print(f'{nome}, Você Já pode tirar sua habilitaçao!')
elif idade == 17:
     print(f'{nome}, Espere mais um ano para poder tira sua habilitaçao!')
else:
     print(f'{nome}, Você não pode tirar sua habilitaçao!')