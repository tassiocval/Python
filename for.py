# lista = [2,6,9,4,0,12,3,7]
# palavra = "Tassio"
# for letra in palavra:
#     print(letra)

# nome = input("Digite seu nome: ")
# for x in range(10):
#     print(f"{x+1} {nome}")


# range(valor_inicialn valor_final, incremento)
# for x in range(20, 1, -1):
#     print(x)

pedras = ("Rubi","Esmeralda","Quartzo","Safira","Diamante","Turmalina")

for pedra in pedras:
    if pedra == "Quartzo":
        continue
    print(pedra)