nome = None
contador = 0

while contador < 5:
    print("Digite seu nome: ")
    nome = input()
    print(f"Olá {nome}, essa é a tentativa {contador + 1}!")
    contador += 1 # Incrementa o contador 

print(f"Bem-vindo, {nome}!")
print("Até logo!")