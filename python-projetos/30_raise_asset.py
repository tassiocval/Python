def soma(n1 , n2):
    if n1 < 0 or n2 < 0:
        raise ValueError('n1 e n2 não podem ser negativos')
    return n1 + n2

print(soma(2, 3))