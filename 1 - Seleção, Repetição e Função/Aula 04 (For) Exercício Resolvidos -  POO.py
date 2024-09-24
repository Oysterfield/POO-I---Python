'''
#Exercício 1

print("Anos bissextos do século XXI:")
for anos in range(2004,2100,4):
    print(anos)
'''
'''
#Exercício 2

for impares in range(1,50,2):
    print(impares)
'''
'''
#Exercício 3

for i in range(5):
    nome = input("Digite o nome: ")
    mensalidade = float(input("Digite a mensalidade: "))
    nota = int(input("Digite a nota: "))
    
    if (i==0):
        melhorNota = nota
        melhorNome = nome
        melhorMensalidade = mensalidade
    else:
        if (melhorNota < nota):
            melhorNota = nota
            melhorNome = nome
            melhorMensalidade = mensalidade
        
print("Melhor nome: ", melhorNome)
print("Melhor mensalidade: ", melhorMensalidade)
print("Desconto: ", melhorMensalidade*0.7)
'''
'''
#Exercício 4

pares = 0
impares = 0
for i in range(10):
    numero = int(input("Número:"))
    if (numero % 2 == 0):
        pares = (pares + 1)
    else:
        impares = (impares + 1)
print("pares:", pares)
print("impares:", impares)
'''
'''
#Exercício 5

tot = 0
num = int(input("Número: "))

for c in range (1,num+1):
    if num % c == 0:
        tot +=1
        
if tot == 2:
    print("É primo.")
else:
    print("Não é primo.")
'''

#Exercício 6

tot = 0
num = int(input("Número: "))
div = 0
divs = ""
for c in range(1,num+1):
    if num % c == 0:
        tot +=1
        div +=1
        divs +=" "+str(c)
        
if div <= 2:
    print("É primo.")
elif div > 2:
    print(f'não é primo, pois é divisível por{divs}')


'''
#Exercício 7

contador = 0
idades = int(input("Quantas idades deseja cadastrar?: "))
for i in range(idades):
    idade_i = int(input("Sua idade: "))
    contador = contador + idade_i

mediaNova = contador / idades

if 0 < mediaNova <= 25:
    print("A turma é jovem")
elif 26 < mediaNova <= 60:
    print("A turma é adulta")
elif mediaNova > 60:
    print("A turma é idosa")
    
'''
'''
#Exercício 8

acumulador = 0
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
for i in range(num1+1,num2):
    acumulador = acumulador + i
print(acumulador)

'''
'''
#Exercício 9

num = int(input("Tabuada de: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

'''
'''
#Exercício 10

for i in range(5):
    nome = input("Nome do(a) aluno(a): ")
    nota1 = float(input("Nota P1 do(a) aluno(a): "))
    nota2 = float(input("Nota P2 do(a) aluno(a): "))
    media = (nota1 + nota2) / 2
    
    if (i==0):
        melhorMedia = media
        melhorNome = nome
    else:
        if (melhorMedia < media):
            melhorMedia = media
            melhorNome = nome

print(f"A média mais alta foi do(a) aluno(a): {melhorNome}")
if melhorMedia >= 5.75:
    print("E ele(a) está aprovado(a)!")
elif 2.75 <= melhorMedia < 5.75:
    print("E ele(a) está em recuperação")
else:
    print("E ele(a) está Reprovado(a)")

'''
'''
#Exercício 11

acumulador = 0
vezes = int(input("Quantos números deseja ler?: "))
for i in range(vezes):
    num = int(input("Número: "))
    acumulador = acumulador + num
    if i == 0:
        maiorNum = num
        menorNum = num
    else:
        if maiorNum < num:
            maiorNum = num
        elif menorNum > num:
            menorNum = num

media = acumulador / vezes
print(media)
print("Número maior:", maiorNum)
print("Número menor:", menorNum)

'''
'''
#Exercício 12

distancias = 0
praia15_20 = 0
numPraias = int(input("Digite o número de praias que deseja cadastrar: "))
for i in range(numPraias):
    praia = input("Nome da praia: ")
    distancia = int(input("Distância do centro da cidade: "))
    distancias = distancias + distancia
    if 15 < distancia < 20:
        praia15_20 += 1
        longePraia = praia
    if i == 0:
        longePraia = praia
        distanciaPraia = distancia
    else:
        if distanciaPraia < distancia:
            distanciaPraia = distancia
            longePraia = praia
            
media = distancias / numPraias
print(f"A praia mais distante do centro da cidade é: {longePraia}.")
print(f"Há {praia15_20} praias entre 15 e 20km do centro.")
print(str("%.1f"%media),"é a distância média das praias.")
'''