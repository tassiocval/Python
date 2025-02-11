
salario = float(input("Digite seu salario: "))

if salario <= 1903.98:
    liquota = 0
elif salario <= 2259.65:
    liquota = 7.5
elif salario <= 3751.05:
    liquota = 15
elif salario <= 4664.68:
    liquota = 22.5
else:
    liquota =  27.5


print(f"\nPara o salario de {salario:.2f}")
print(f"A liquota sera de {liquota:.2f}")
    
