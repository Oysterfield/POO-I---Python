import random

#Exercício 1
def AdicionaTupla():
    elemTupla = int(input("Adicione um elemento à tupla: "))
    return elemTupla

def TuplaFuncao(tupla):
    print(f"O número 9 aparece {tupla.count(9)} vezes")   
    posicaoPrim3 = 0
    for i in range(len(tupla)):
        if int(tupla[i]) == 3:
            posicaoPrim3 = [i]
            print("Posição em que o primeiro valor 3 foi digitado: ", posicaoPrim3)
            break
    if len(posicaoPrim3) == 0:
        print("O número 3 não foi digitado")
    paresLista = []
    for i in range(len(tupla)):
        if int(tupla[i]) % 2 == 0:
            paresLista.append(tupla[i])
    print("Pares: ", paresLista)

#main
tupla = (AdicionaTupla(), AdicionaTupla(), AdicionaTupla(), AdicionaTupla(), AdicionaTupla())
print(tupla)
TuplaFuncao(tupla)

'''
#Exercício 2

def Ordenado(tupla):
    for i in range(len(tupla)):
        if i == 0:
            maior = tupla[i]
            menor = tupla[i]
        if tupla[i] > maior:
            maior = tupla[i]
        if tupla[i] < menor:
            menor = tupla[i]
    print(maior, menor)
    
tupla = (random.randint(1,30),
        random.randint(1,30),
        random.randint(1,30),
        random.randint(1,30),
        random.randint(1,30))
print(tupla)
Ordenado(tupla)

'''
'''
#Exercício 3
nums = int(input("Nº de elementos: "))
lista = []
listaRepetidos = []
repetido = 0
for i in range(nums):
    lista.append(int(input(f"{i+1}º número: ")))
    for j in range(i):
        if lista[j] == lista[i]:
            repetido +=1
            listaRepetidos.append(lista[i])
        else:
            repetido +=0
        
if repetido >= 1:
    print(f"Existe um(ns) número(s) repetido(s): {listaRepetidos}")
else:
    print("Não existe um número repetido")

'''
'''
#Exercício 4

def Sorteio(alunos,s):
    vencedor = False
    for i in range(len(alunos)):
        if alunos[i] == s:
            print(i+1)
            vencedor = True
            break
    if vencedor == False:
        mult = 0
        j = -1
        while vencedor == False:
            mult +=1
            j +=1
            for j in range(len(alunos)):
                if alunos[j] == s+mult or alunos[j] == s-mult:
                    print(j+1)
                    vencedor = True
                    break
            

n = int(input("Nº de camisetas sorteadas: "))
for i in range(n):
    qt,s = input("Quantidade de alunos do grupo e número secreto: ").split()
    qt = int(qt)
    s = int(s)
    alunos = []
    for i in range(qt):
        alunos.append(int(input(f"Número escolhido pelo aluno {i+1}: ")))
    Sorteio(alunos,s)
'''
'''
#Exercício 5

x = []
y = []
count = 0
for i in range(5):
    x.append(int(input("Plugue ou tomada? [0/1]: ")))
    y.append(int(input("Plugue ou tomada? [0/1]: ")))
    if x[i] != y[i]:
        count +=1
if count == 5:
    print("Y")
else:
    print("N")

'''
'''
#Exercício 6

x = []
for i in range(10):
    x.append(int(input("Adicione um número à lista: ")))
    if x[i] <= 0:
        x[i] = 1
    print(f"X[{i}] = {x[i]}")

'''
'''
#Exercício 7

def Verifica(n):
    n.append(int(input("Adicione um valor ao vetor: ")))
    while n[0] > 50:
        n = int(input("Valor acima do suportado. Digite outro valor: "))
    return n


n = []
n.append(Verifica(n))
n.pop(1)
for i in range(9):
    n.append(n[i]*2)
print(n)

'''
'''
#Exercício 8

x = []
y = []
n = int(input("Nº de células do tabuleiro: "))
for i in range(n):
    x.append(int(input("'1' se há uma mina na celula, ou '0' se não há: ")))
for i in range(n):
    if i == 0:
        y.append(x[i] + x[i+1])
    elif i == n-1:
        y.append(x[i] + x[i-1])
    else:
        y.append(x[i-1] + x[i] + x[i+1])
print(y)

'''