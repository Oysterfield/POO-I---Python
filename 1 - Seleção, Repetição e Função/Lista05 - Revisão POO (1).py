import math
'''
#Exercício 1)

x = 0
y = 1
while x != y:
    x = int(input("1º Número: "))
    y = int(input("2º Número: "))
    if x < y:
        print("Crescente")
    elif x > y:
        print("Decrescente")
     
'''
'''
#Exercício 2)

teste = int(input("Quantidade de testes: "))
for i in range(teste):
    x = int(input("1º Número: "))
    y = int(input("2º Número: "))
    acumulador = 0
    if x > y:
        aux = x
        x = y
        y = aux
    for i in range(x+1,y):
        if i % 2 == 1:
            acumulador = acumulador + i
    print(acumulador)

'''
'''
#Exercício 3)

valor = float(input("Digite a quantia: R$ "))
notas = int(valor // 100)
print("NOTAS")
print("{} nota(s) de R$100.00".format(int(notas)))
resto = (valor % 100)
notas = resto // 50
print("{} nota(s) de R$50.00".format(int(notas)))
resto = resto % 50
notas = resto // 20
print("{} nota(s) de R$20.00".format(int(notas)))
resto = resto % 20
notas = resto // 10
print("{} nota(s) de R$10.00".format(int(notas)))
resto = resto % 10
notas = resto // 5
print("{} nota(s) de R$5.00".format(int(notas)))
resto = resto % 5
notas = resto // 2
print("{} nota(s) de R$2.00".format(int(notas)))
resto = resto % 2
moedas = resto // 1
print("MOEDAS")
print("{} moeda(s) de R$1.00".format(int(moedas)))
resto = resto % 1
moedas = resto // 0.5
print("{} moeda(s) de R$0.50".format(int(moedas)))
resto = resto % 0.5
moedas = resto // 0.25
print("{} moeda(s) de R$0.25".format(int(moedas)))
resto = resto % 0.25
moedas = resto // 0.1
print("{} moeda(s) de R$0.10".format(int(moedas)))
resto = resto % 0.1
moedas = resto // 0.05
print("{} moeda(s) de R$0.05".format(int(moedas)))
resto = resto % 0.05
moedas = resto // 0.01
print("{} moeda(s) de R$0.01".format(int(moedas)))

'''
'''
#Exercício 4)

while True:
    distancia, vf, vg = input("Distância entre o fugitivo e a Guarda Costeira e velocidades das embarcações do fugitivo e da Guarda Costeira: ").split()
    distancia = int(distancia)
    vf = int(vf)
    vg = int(vg)
    distGuarda = math.sqrt(distancia**2 + 12**2)
    tf = 12/vf
    tg = distGuarda/vg
    if tg < tf:
        print("S")
    else:
        print("N")

'''
'''
#Exercício 5)

x,y = input("Tempos que cada piloto, 1º e último, leva para dar uma volta: ").split()
x = int(x)
y = int(y)
count = 1
diff = 0
while True:
    diff = diff + y - x
    count +=1
    if diff >= x:
        break
print("{} foi a volta em que houve o retardatário".format(count))

'''
#Incompleto
#Exercício 6)

for i in range(5):
    nota = float(input("Nota da Esc. Samba: "))
    contagem = nota
    if i == 0:
        nota1 = nota
    

print(notaMeio1 + notaMeio2 + notaMeio3)

'''
#Exercício 7)

i = 0
while True:
    i +=1
    print(f"Teste {i}")
    depositos = int(input("Nº de depósitos: "))
    if depositos == 0:
        break
    diff = 0
    for n in range(depositos):
        joao = int(input("Centavos depositados: "))
        ze = int(input("Centavos depositados: "))
        diff = diff + (joao - ze)
        print(diff)
    print(" ")

'''
'''
#Exercício 8)

count = 0
while True:
    v = int(input("Digite o valor desejado: "))
    if v == 0:
        break
    count += 1
    
    print("Teste %d" % count)
    
    nota50 = v // 50
    nota10 = (v - (nota50*50)) // 10
    nota5 = (v - nota50*50 - nota10*10) // 5
    nota1 = (v - nota50*50 - nota10*10 - nota5*5)
    
    print("%d %d %d %d\n" % (nota50, nota10, nota5, nota1))

'''
'''
#Exercício 9)

a,b = input("Gols times A e B: ").split()
if a > b:
    venc1 = "A"
else:
    venc1 = "B"
c,d = input("Gols times C e D: ").split()
if c > d:
    venc2 = "C"
else:
    venc2 = "D"
e,f = input("Gols times E e F: ").split()
if e > f:
    venc3 = "E"
else:
    venc3 = "F"
g,h = input("Gols times G e H: ").split()
if g > h:
    venc4 = "G"
else:
    venc4 = "H"
i,j = input("Gols times I e J: ").split()
if i > j:
    venc5 = "I"
else:
    venc5 = "J"
k,l = input("Gols times K e L: ").split()
if a > b:
    venc6 = "K"
else:
    venc6 = "L"
m,n = input("Gols times M e N: ").split()
if m > n:
    venc7 = "M"
else:
    venc7 = "N"
o,p = input("Gols times O e P: ").split()
if o > p:
    venc8 = "O"
else:
    venc8 = "P"
venc1b,venc2b = input("Gols times 1º quarta de final: ").split()
if venc1b > venc2b:
    venc9 = venc1
else:
    venc9 = venc2
venc3b,venc4b = input("Gols times 2º quarta de final: ").split()
if venc3b > venc4b:
    venc10 = venc3
else:
    venc10 = venc4
venc5b,venc6b = input("Gols times 3º quarta de final: ").split()
if venc5b > venc6b:
    venc11 = venc5
else:
    venc11 = venc6
venc7b,venc8b = input("Gols times 4º quarta de final: ").split()
if venc7b > venc8b:
    venc12 = venc7
else:
    venc12 = venc8
venc9b,venc10b = input("Gols times 1º semifinal: ").split()
if venc9b > venc10b:
    venc13 = venc9
else:
    venc13 = venc10
venc11b,venc12b = input("Gols times 2º semifinal: ").split()
if venc11b > venc12b:
    venc14 = venc11
else:
    venc14 = venc12
venc13b,venc14b = input("Gols times final: ").split()
if venc13b > venc14b:
    vencedor = venc13
else:
    vencedor = venc14
print(vencedor)

'''
'''
#Exercício 10

x = int(input("X: "))
while True:
    z = int(input("Z: "))
    if z > x:
        break

count = 1
x2 = x
while True:
    count +=1
    x2 = x2 + (x+1)
    x +=1
    if x2 > z:
        break

print(count)

'''
'''
#Exercício 11

x,y = input("Digite as coordenadas x e y: ").split()
x = int(x)
y = int(y)
if x >= 0 and y >= 0:
    print("dentro")
else:
    print("fora")

'''
'''
#Exercício 12

portaP = int(input("0 ou 1?: "))
portaR = int(input("0 ou 1?: "))
if portaP == 1 and portaR == 1:
    print("A")
elif portaP == 1 and portaR == 0:
    print("B")
elif portaP == 0:
    print("C")

'''
'''
#Exercício 13)
quebrou = 0
bandejas = int(input("Nº de bandejas entregues: "))
for i in range(bandejas):
    latas = int(input("Latas na bandeja: "))
    copos = int(input("Copos na bandeja: "))
    if latas > copos:
        quebrou = quebrou + copos
print(f"O graçom quebrou {quebrou} copos.")

'''
'''
#Exercício 14)

while True:
    quadrados = 0
    lados = int(input("Nº de quadrados em cada lado: "))
    if lados == 0:
        break
    for i in range(lados,0,-1):
        quadrados = quadrados + i**2
    print(quadrados)

'''
'''
#Exercício 15)
alcool,gasolina,ra,rg = input("Preços por litro de álcool e gasolina, e respectivos rendimentos: ").split()
alcool = float(alcool)
gasolina = float(gasolina)
ra = float(ra)
rg = float(rg)
fimAlcool = ra/alcool
fimGasolina = rg/gasolina
if fimAlcool > fimGasolina:
    print("A")
if fimGasolina >= fimAlcool:
    print("G")

'''
'''
#Exercício 16)

while True:
    op1 = input("Opção jogador 1: ")
    op2 = input("Opção jogador 1: ")
    if op1 == op2:
        print("Empate!")
    elif op1 == "pedra" and op2 == "tesoura":
        print("Vitória do Jogador 1!")
    elif op1 == "tesoura" and op2 == "papel":
        print("Vitória do Jogador 1!")
    elif op1 == "papel" and op2 == "pedra":
        print("Vitória do Jogador 1!")
    elif op1 == "tesoura" and op2 == "pedra":
        print("Vitória do Jogador 2!")
    elif op1 == "papel" and op2 == "tesoura":
        print("Vitória do Jogador 2!")
    elif op1 == "pedra" and op2 == "papel":
        print("Vitória do Jogador 2!")
    jogar = input("Deseja continuar? [S/N]: ").upper()
    if jogar == "N":
        break

'''
'''
#Exercício 17)

a = int(input("1º Número: "))
b = int(input("2º Número: "))
c = int(input("3º Número: "))
if a < b < c:
    print(a,b,c)
elif a < c < b:
    print(a,c,b)
elif b < a < c:
    print(b,a,c)
elif b < c < a:
    print(b,c,a)
elif c < a < b:
    print(c,a,b)
elif c < b < a:
    print(c,b,a)

'''