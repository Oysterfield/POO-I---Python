'''
#Exemplo 1

def hello(meuNome,idade):
    print(f"Olá {meuNome}\nSua idade é: {idade}")
    
hello("Fábio",28)


#Exemplo 2

def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario=horas*taxa
    else:
        h_excd = horas - 40
        salario = 40*taxa+(h_excd*(1.5*taxa))
    return salario

str_horas = input("Digite as horas: ")
str_taxa = input("Digite a taxa: ")
total_salario = calcular_pagamento(str_horas,str_taxa)
print("O valor de seus rendimentos é R$",total_salario)

'''
'''
#Exercício 1

def calcSalario(salario):
    if salario <= 400:
        percentReaj = 15
    elif 400 < salario <= 800:
        percentReaj = 12
    elif 800 < salario <= 1200:
        percentReaj = 10
    elif 1200 < salario <= 2000:
        percentReaj = 7
    else:
        percentReaj = 4
    reajuste = (salario/100)*percentReaj
    novoSalario = salario + reajuste
    print("Novo salário: {:.2f}".format(novoSalario))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: {}%".format(percentReaj))
    
calcSalario(float(input("Digite o salário: ")))   

'''
'''
#Exercício 2

def horaChegada(saida,viagem,fuso):
    total = saida + viagem + fuso
    if total > 23:
        total -=24
    if total < 0:
        total +=24
    print(total)
    
saida,viagem,fuso = input("Hora de saída, tempo de viagem e fuso horário: ").split()
saida = int(saida)
viagem = int(viagem)
fuso = int(fuso)
horaChegada(saida,viagem,fuso)

'''
'''
#Exercício 3

def UltrapassandoZ(x):
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
    
UltrapassandoZ(int(input("X: ")))

'''
'''
#Exercício 4

def Quadrante(x,y):
        if x > 0 and y > 0:
            print("primeiro")
        if x < 0 and y > 0:
            print("segundo")
        if x < 0 and y < 0:
            print("terceiro")
        if x > 0 and y < 0:
            print("quarto")
while True:
    x = int(input("X: "))
    y = int(input("Y: "))
    if x == 0 or y == 0:
        break
    Quadrante(x,y)

'''
'''
#Exercício 5
def Elevador(n,c):
    tot = 0
    count = 0
    for i in range(n):
        s,e = input("Saídas e entradas: ").split()
        s = int(s)
        e = int(e)
        count = count - s + e
        if count > c:
           tot +=1 
    if tot >= 1:
        print("S")
    else:
        print("N")

n,c = input("Nº de leituras do sensor e capacidade máxima do elevador: ").split()
n = int(n)
c = int(c)
Elevador(n,c)

'''
'''
#Exercício 6

def CalcPorta(a):
    a,b,c = input("Dimensões do colchão: ").split()
    a = int(a)
    b = int(b)
    c = int(c)
    h,l = input("Altura e largura das portas: ").split()
    h = int(h)
    l = int(l)
    if b > h:
        return "N"
    else:
        return "S"
    
#main
a = 0
resposta = CalcPorta(a)
if resposta == "N":
    print("N")
else:
    print("S")

'''
#Exercício 7

def CalcMédia(soma):

    for i in range(5):
        nota = int(input("nota Aluno {}: ".format(i+1)))
        soma +=nota
        if i == 0:
            melhorNota = nota
        if nota > melhorNota:
            melhorNota = nota
    media = soma/5
    print("Média da turma: ", media)
    return melhorNota

#main
soma = 0
melhorNota = CalcMédia(soma)
if melhorNota >= 5.75:
    print("Aprovado")
elif 5.75 > melhorNota >= 2.75:
    print("Em recuperação")
else:
    print("Reprovado")
