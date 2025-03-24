
while True:
    nota = float(input('Digite um nota de (0 - 10): '))
    if 0 <= nota <=10:
        print(f'Nota armazenada com sucesso! {nota:.1f}')
        break
    
    print('Nota inválida, digite novamente!')
