pessoa = {
    "nome": "João",
    "idade": 25,
    "estudante": True
}


pessoa["altura"] = 1.75

del pessoa["estudante"]

print(pessoa["altura"])