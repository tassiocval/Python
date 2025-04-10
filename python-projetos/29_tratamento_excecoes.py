try:
    x  = int(input('Digite um número: '))
    print(5/x)
except ValueError:
    print('Digite um número inteiro')
except ZeroDivisionError:
    print('Nao digite 0!')