from pympler.asizeof import asizesof # type: ignore

def dobro(lista):
    for i in lista:
        yield i*2



x = dobro(range(0, 10000))

for i in x:
    print(i)