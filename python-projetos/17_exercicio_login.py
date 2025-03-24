user = ('Admin')
senha = ('Password')


while True:
    print()
    print('--------------------------------------')
    new_user = input('Digite seu Login: ')
    print()
    print('--------------------------------------')
    new_senha = input('Digite sua Senha: ')
    print()
    print('--------------------------------------')
    if (user == new_user) and (senha == new_senha):
        print('Logado com sucesso!')
        break
    print('Login do usúario é INVALIDO!')
