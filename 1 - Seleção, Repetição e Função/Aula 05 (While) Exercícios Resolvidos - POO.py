'''
#Exercício 1

sexo = input("Digite seu sexo: ").upper()
while (sexo != "M") and (sexo != "F"):
    sexo = input("Digite novamente: ").upper()
    if (sexo == "M") or (sexo == "F"):
        break
print("Ok")

'''
'''
#Exercício 2

from random import randrange
num = randrange(11)
cont = 1
teclado = int(input("Digite um número entre 0 e 10: "))
while (num != teclado):
    teclado = int(input("Digite novamente: "))
    cont += 1
print(f"Na mosca! O número correto era {num}.\n Você teve {cont} tentativas.")

'''
'''
#Exercício 3

resposta = "S"
while resposta == "S":
    salario = float(input("Digite seu salário: "))
    descPadrao = (salario/100)*11
    if descPadrao <= 320:
        print(f"O desconto foi de R${descPadrao:.2f}")
    if descPadrao > 320:
        descTeto = 320
        porcentDesc = (320/salario)*100
        print(f"O desconto foi de R${descTeto:.2f} e a porcentagem foi de {porcentDesc:.2f}%")

    resposta = str(input("Deseja repetir o processo? [S/N]: ")).upper()

'''
'''
#Exercício 4

i = 0
count = 0
num = int(input("Digite um número: "))
while i < 10000:
    i +=1
    if i % num == 2:
        count +=1
        print(i)

'''
'''
#Exercício 5

i = 0
num = int(input("Tabuada de: "))
while i < 10:
    i +=1
    print(f"{num} x {i} = {num*i}")

'''
'''
#Exercício 6

sequencia =" "
x = 1
while x != 0:
    x = int(input("Digite um número: "))
    sequencia =" "
    for i in range(1,x+1):
        sequencia +=" "+str(i)
    print(sequencia)

'''
'''
#Exercício 7

TotAlcool = 0
TotGasolina = 0
TotDiesel = 0
x = 1
while x != 4:
    x = int(input("Digite uma opção: [1.Álcool] [2.Gasolina] [3.Diesel] [4.Finalizar]: "))
    if x == 4:
        break
    if x < 1 or x > 4:
        print("Código inválido. Digite novamente")
    if x == 1:
        TotAlcool +=1
    if x == 2:
        TotGasolina +=1
    if x == 3:
        TotDiesel +=1

print(f"MUITO OBRIGADO \nÁlcool: {TotAlcool} \nGasolina: {TotGasolina} \nDiesel: {TotDiesel}")

'''
'''
#Exercício 8

sequencia = " "
soma = 0
while True:
    m = int(input("Digite um número: "))
    n = int(input("Digite outro número: "))
    sequencia = " "
    soma = 0
    if m <= 0 or n <= 0:
        break
    if m < n:
        for i in range(m,n+1):
            sequencia +=" "+str(i)
            soma = soma + i
        print(sequencia, f"Sum={soma}")   
    elif m > n:
        for i in range(n,m+1):
            sequencia +=" "+str(i)
            soma = soma + i
        print(sequencia, f"Sum={soma}")
        
'''