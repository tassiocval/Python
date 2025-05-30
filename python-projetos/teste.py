# Soma de dois números

# n1 = float(input('Digite um número: '))
# n2 = float(input('Digite outro número: '))

# soma = n1 + n2
# print(f'A soma dos numeros é: {soma:.0f}')

#Calculadora de média

# nota1 = float(input('Digite a primeiria nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# nota3 = float(input('Digite a terceira nota: '))

# media = (nota1 + nota2 + nota3) / 3

# print(f'A sua media é: {media:.1f}')

# Área de um retângulo

# largura = float(input('Digite a largura do retângulo: '))
# altura = float(input('Digite a altura do retângulo: '))

# area = largura * altura

# print(f'A Área do retângulo é: {area}')

#Conversão de temperatura

# temperatura_celsius = float(input('Insira a temperatura em Celsius: '))

# temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# print(f'Em Fahrenheit é: {temperatura_fahrenheit:.2f}')

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))

# resto = n1 % n2
# print(f'O resto da divisão é: {resto}')


# numero = int(input('Digite um número: '))

# if numero > 0:
#     print(f'O número é positivo')
# elif numero < 0:
#     print(f'O número é negativo!')
# else:
#     print(f'O número é Zero')

# pessoa1 = float(input('Digite a altura da primeira pessoa (em metros): '))
# pessoa2 = float(input('Digite a altura da segunda pessoa (em metros): '))

# if pessoa1 > pessoa2:
#     print('A primeira pessoa é mais alta.')
# elif pessoa2 > pessoa1:
#     print('A segunda pessoa é mais alta.')
# else:
#     print('As alturas são iguais.')


# nota = float(input("Digite sua nota: "))
# frequencia = float(input("Digite sua frequência (%): "))

# if nota >= 7 and frequencia >= 75:
#     print('Aprovado!')
# else:
#     print('Reprovado!')

# num = int(input('Digite um número: '))

# if num >= 10 and num <= 20:
#     print(f'O {num}, está no intervalor entre (10 e 20)!')
# else:
#     print(f'O {num}, não está no intervalor entre (10 e 20)!')

# idade = int(input('Digite sua idade: '))
# acompanhado = input('Está acompanhado de um responsável? (s/n): ')

# if idade >= 18 or acompanhado == 's':
#     print('Pode entrar na festa!')
# else:
#     print('Não pode entrar na festa!')

# num = int(input('Digite um número: '))

# if num > 0 and num % 2==0:
#     print('O numero e positivo e par')
# else:
#     print('O numero NÃO e positivo e par')


# admin = input('Você é administrador? (s/n):')

# if not admin.lower() == 's':
#     print('Acesso negado! 🚫')
# else:
#     print('Acesso autorizado! ✅')

# nota = float(input('Digite uma nota de 0 a 10: '))

# if 0 <= nota <= 4:
#     print('Reprovado!')
# elif 5 <= nota <= 6:
#     print('Recuperação!')
# elif 7 <= nota <= 10:
#     print('Aprovado!')
# else:
#     print('Nota inválida! Digite uma nota entre 0 e 10.')

senha_correta = ("admin123")

senha = input("Digite sua senha: ")

if senha == senha_correta:
    print("Acesso permitido.")
else:
    print("Senha incorreta.")  
