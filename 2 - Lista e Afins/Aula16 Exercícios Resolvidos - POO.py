
#Exercício 1
while True:
    n = int(input("Número de suspeitos: "))
    if n == 0:
        break
    suspeitos = []
    for i in range(n):
        suspeitos.append(int(input("Diga quão suspeita é a pessoa: ")))
    suspeitos.sort()
    print(suspeitos.index(suspeitos[n-1]))

'''
#Exercício 2

n = int(input("Quantidade de número na lista de Bino: "))
lista = []
mult2 = 0
mult3 = 0
mult4 = 0
mult5 = 0
for i in range(n):
    lista.append(int(input("Adicione um número à lista: ")))
    if lista[i] % 2 == 0:
        mult2 +=1
    if lista[i] % 3 == 0:
        mult3 +=1
    if lista[i] % 4 == 0:
        mult4 +=1
    if lista[i] % 5 == 0:
        mult5 +=1

print(f"{mult2} Múltiplo(s) de 2 \n{mult3} Múltiplo(s) de 3 \n{mult4} Múltiplo(s) de 4 \n{mult5} Múltiplo(s) de 5")

'''
'''
#Exercício 3

n = int(input("N: "))
conjunto = set()
for i in range(n-1):
    conjunto.add(int(input("Adicione um nº ao conjunto: ")))
print(conjunto)
for i in range(len(conjunto)):
    if i+1 not in conjunto:
        print(i+1)

'''