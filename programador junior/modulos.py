print("########## SEJA BEM VINDO A AUTO ESCOLA PYTHON #############")

print("-------------------------------------------------------------------------")

nome = str(input("Digite seu nome aqui! --> "))
print("-------------------------------------------------------------------------")

idade = int(input("Digite a sua idade, para verificar se esta apto a dirigir! "))
print("-------------------------------------------------------------------------")

if idade >= 18:
    print(nome,"Você esta apto a dirigir!")
elif idade == 17:
    print(nome,"Olha, você pode esperar mais um ano, pois ainda não completou 18 anos")
else:
    print("Ops! verifiquei aqui",nome, ",e vi que você e menor de idade, entao não esta apto a dirigir!")

print("-------------------------------------------------------------------------")
