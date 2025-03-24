print('Exemplo de uso: 5.5 10 9.0 3.0')
print()
nome = input('Digite seu nome: ')
nota1 = float(input('Digite a nota da AV1: '))
nota2 = float(input('Digite a nota da AV2: '))
nota3 = float(input('Digite a nota da AV3: '))
nota4 = float(input('Digite a nota da AV4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f'Parabéns {nome}, você foi APROVADO!')
elif media == 5:
    print(f'{nome}, você está de RECUPERAÇÃO!')
elif media <= 4:
    print(f'{nome}, você está de REPROVADO!')
else:
    print(f'{nome}, Ops verifiquei que você digitou uma nota invalída!')