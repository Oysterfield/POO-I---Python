from random import uniform
'''
#Exercício 1

def PesadasOuLeves(e):
    return e[2]

lista = []
while True:
    lista0 = []
    lista0.append(input("Nome: "))
    lista0.append(int(input("Idade: ")))
    lista0.append(int(input("Peso: ")))
    lista.append(lista0[:])
    lista0.clear()
    if (input("Deseja continuar? [S/N] ")).upper() == "N":
        break

print(f"{len(lista)} pessoas foram cadastradas.")

lista.sort(reverse=True,key=PesadasOuLeves)
print("Pessoas mais pesadas: ", lista)

lista.sort(key=PesadasOuLeves)
print("Pessoas mais leves: ", lista)

lista1 = []
anos20 = 0
for i in lista:
    if i[1] > 20:
        anos20 +=1
        lista0.append(i[0])
        lista0.append(i[1])
        lista1.append(lista0[:])
        lista0.clear()
print(f"Pessoas com mais de 20 anos: {anos20}\n{lista1}")

'''
'''
#Exerício 2

matriz = []
matriz2 = []

ordem = int(input("Ordem da matriz: "))
for l in range(ordem):
    for c in range(ordem):
        matriz.append(float(format(uniform(0,10), '.1f')))
    matriz2.append(matriz[:])
    matriz.clear()
print(matriz2)

l = int(input("Linha da operação: "))
operacao = input("Soma ou Média? [S/M]: ").upper()
soma = 0
j = 0
for i in matriz2[l]:
    soma +=matriz2[l][j]
    j +=1
if operacao == 'S':
    print("Soma: ", soma)
elif operacao == 'M':
    print("Média: ", format(soma / 12, '.1f'))
    
print(matriz2)

'''
'''
#Exercício 3

matriz = []
matriz2 = []

ordem = int(input("Ordem da matriz: "))
q = input("Deseja preencher a matriz pelo teclado ou randomicamente? [T/R] ").upper()
if q == 'T':
    for l in range(ordem):
        for c in range(l):
            matriz.append(int(input("Adicione um item à matriz: ")))
            soma += matriz[l][c]
        matriz2.append(matriz[:])
        matriz.clear()
    print(matriz2)
else:
    for l in range(ordem):
        for c in range(l):
            matriz.append(float(format(uniform(-10,10), '.1f')))
        matriz2.append(matriz[:])
        matriz.clear()
    print(matriz2)

soma = 0
for l in matriz2:
    for c in l:
        soma += c
o = input("Soma ou Média? [S/M] ").upper()
if o == 'S':
    print(f"Soma: {soma}")
else:
    print(f"Média : {soma/len(matriz2)}")

'''
'''
#Exercício 4

while True:
    
    def Carac(cTot,matriz,n,m,a):
        flag = True
        for i in range(n):
            c1 = 0
            for j in range(m):
                if matriz[j][i] == 1:
                    c1 +=1
            if (a == 2 or a == 4) and c1 == 0:
                flag = False
                break
            elif (a == 1 or a == 3) and c1 == m:
                flag = False
                break
        if flag == True:
            cTot +=1
        return cTot
    
    #main
    n = int(input("Número de participantes: "))
    m = int(input("Número de problemas: "))
    if n == 0 or m == 0:
        break
    
    matriz0 = []
    matriz = []
    for i in range(n):
        for j in range(m):
            matriz0.append(int(input("1 ou 0?: ")))       
        matriz.append(matriz0[:])
        matriz0.clear()
        
    cTot = 0
    for a in range(1,5):
        if a == 1 or a == 4:
            cTot = Carac(cTot,matriz,n,m,a)
        if a == 2 or a == 3:
            cTot = Carac(cTot,matriz,m,n,a)
    print(cTot)

'''
'''
#Exercício 5

matriz = []
for i in range(int(input("Número de pessoas que participaram da pesquisa: "))):
    matriz.append(int(input("1 ou 0?: ")))

if matriz.count(0) > matriz.count(1):
    print('Y')
else:
    print('N')

'''
'''
#Exercício 6
while True:
    m,r = input("Voluntários que mergulharam e retornos: ").split()
    m = int(m)
    r = int(r)
    
    mSet = set()
    for i in range(1,m+1):
        mSet.add(i)
    rSet = set()
    for i in range(r):
       rSet.add(int(input("Mergulhador que retornou: ")))
    
    x = mSet.difference(rSet)
    if x == set():
        print('*')
    else:
        print(sorted(x))

'''
'''
#(?)
#Exercício 7

pulo,canos = input("Digite a altura do pulo do sapo e o nº de canos: ").split()
pulo = int(p)
canos = int(n)

while pulo < 1 or pulo > 5:
    pulo = int(input("Valor fora do limite permitido. Digite novamente: "))
while canos < 2 or canos > 100:
    canos = int(input("Valor fora do limite permitido. Digite novamente: "))

alturaCanos = []
for i in range(canos):
    a = int(input(f"Altura do cano {i}: "))
    while a > 10:
        a = int(input("Valor fora do limite permitido. Digite novamente: "))
    alturaCanos.append(a)
    if i > 0:
        if alturaCanos[i] - alturaCanos[i-1]

'''
'''
#Exercício 8

while True:
    n = int(input("Número de questões da folha de resposta: "))
    if n == 0:
        break
    for i in range(n):
        lista = []
        flag = 0
        for i in range(5):
            lista.append(int(input("Tom de cinza: ")))
            if lista[i] <= 127:
                flag +=1
        if flag > 1:
            print("*")
        else:
            for i in range(5):
                if lista[i] <= 127:
                    if i == 0:
                        print("A")
                    elif i == 1:
                        print("B")
                    elif i == 2:
                        print("C")
                    elif i == 3:
                        print("D")
                    elif i == 4:
                        print("E")

'''
'''
#Exercício 9

def Perfeito(x):
    divs = []
    soma = 0
    for i in range(1,x):
        if x % i == 0:
            divs.append(i)
            soma += divs[i] 
    if soma == x:
        print(x,"eh perfeito")
    else:
        print(x,"nao eh perfeito")

casos = int(input("Casos de teste: "))
while casos < 1 or casos > 20:
    casos = int(input("Valor fora do limite permitido. Digite novamente: "))
    
for i in range(casos):
    x = int(input("Digite um número para verificar se é perfeito: "))
    while x < 1 or x > 100000000:
        x = int(input("Valor fora do limite permitido. Digite novamente: "))
    Perfeito(x)

'''
'''
#Exercício 10
while True:
    print("JOGA NA MEGA SENA")
    jogos = int(input("Quantos tipos de jogos você quer que eu sorteie?: "))
    if jogos == 0:
        break
    print(f"SORTEANDO {jogos} JOGOS")

    matriz0 = []
    matriz = []
    for i in range(jogos):
        for j in range(6):
            matriz0.append(int(float(uniform(1,60))))
        matriz.append(matriz0[:])
        matriz0.clear()
        print(f"Jogo {i+1}: {matriz[i]}")
    print("BOA SORTE\n")   

'''
'''
#Exercício 11

dados = []
aluno = []
soma = 0
for i in range(int(input("Nº de alunos: "))):
    aluno.append(input(f"Nome do aluno {i+1}: "))
    for j in range(3):
        aluno.append(int(input(f"Nota {i+1}: ")))
        soma += aluno[j+1]
    aluno.append(int(soma/3))
    dados.append(aluno[:])
    aluno.clear()

print('='*20)
print("BOLETIM")
for i in range(len(dados)):
    
    print(f"Aluno {dados[i][0]}:\n Média: {dados[i][4]}")
print('='*20)


while True:
    q = input("Deseja consultar alguma nota? [S/N]: ").upper()
    if q == 'N':
        break
    a = int(input("Qual aluno (por número)?: "))
    nota = int(input("Qual nota?: "))
    print(f"Aluno {dados[a][0]}:\n Nota {nota}: {dados[a][nota]}")

'''