
pessoas = []
while True:
    desicao = int(input('Digite 1 para cadastra uma pessoa e 2 para sair: '))
    if desicao == 2:
        break

    pessoa = {'nome': input('Digite o nome: '),
              'idade' : input('Digite a idade: '),  
              'peso': input('Digite seu peso: '), 
              'altura': input('Digite a altura: ')}
    
    pessoas.append(pessoa)


for i in pessoa.items():
    print(f'{i}')
