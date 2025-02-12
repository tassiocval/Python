# Simples, Composto, Encadeado

n1 = n2 = 0
media = 0.0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

# Calcular a média aritmética das notas

media = (n1 + n2) / 2

if (media >= 7):
    print("Resultado: APROVADO!")
    print("Parabéns!")
elif (media >= 5):
    print("Aluno: RECULPERAÇÃO!")
else:
    print("Aluno: REPROVADO!")

print("Sua media é {}".format(media))

