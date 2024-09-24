'''
#Exercício 1

def Direcao(posicao):
    if posicao % 360 == 0:
        print('L')
    if posicao % 360 == 90:
        print('N')
    if posicao % 360 == 180:
        print('O')
    if posicao % 360 == 270:
        print('S')

while True:
    n = int(input("Nº de comandos do sargento: "))
    if n == 0:
        break
    comandos = input("comandos: ").upper()
    posicao = 90
    for i in range(n):
        if comandos[i] == "E":
            posicao +=90 
        elif comandos[i] == "D":
            posicao -=90
    Direcao(posicao)
'''
'''
#Exercício 2

def Jogo(c):
    
    if int(c[0]) == int(c[2]):
        resultado = int(c[0])*int(c[2])
    elif c[1].isupper():
        resultado = int(c[2]) - int(c[0])
    else:
        resultado = int(c[0]) + int(c[2])
    return resultado

#main
n = int(input("Nº de casos de teste: "))
for i in range(n):
    c = input("Digite um número, uma letra e outro número: ")
    print(Jogo(c))

'''
'''
#Exercício 3

def Leds(n):
    leds = 0
    for i in range(len(n)):
        if n[i] == '1':
            leds += 2
        elif n[i] == '2' or n[i] == '3' or n[i] == '5':
            leds += 5
        elif n[i] == '4':
            leds += 4
        elif n[i] == '6' or n[i] == '9' or n[i] == '0':
            leds += 6
        elif n[i] == '7':
            leds += 3
        elif n[i] == '8':
            leds += 7
    print(f"{leds} leds")

#main
casos = int(input("Nº de casos de teste: "))
for i in range(casos):
    n = input("Nº que deseja representar: ")
    Leds(n)
    
'''
'''
#Exercício 4

def Porcent(coelhos,ratos,sapos):
    total = coelhos + ratos + sapos
    porcentC = (coelhos / total)*100
    porcentR = (ratos / total)*100
    porcentS = (sapos / total)*100
    print(f"Percentual de coelhos: {porcentC:.2f} % \nPercentual de ratos: {porcentR:.2f} % \nPercentual de sapos: {porcentS:.2f} %")

#main
coelhos = 0
ratos = 0
sapos = 0
tot = 0
casos = int(input("Nº de casos de teste: "))
for i in range(casos):
    quantia,tipo = input("Nº e tipo de cobaia: ").split()
    quantia = int(quantia)
    tot += quantia
    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia
print(f"Total: {tot} cobaias \nTotal de coelhos: {coelhos} \nTotal de ratos: {ratos} \nTotal de sapos: {sapos}")
Porcent(coelhos,ratos,sapos)    

'''
'''
#Exercício 5

while True:
    
    def DivPor3(n,m):
        soma = 0
        for i in range(n):
            soma += int(m[i])
        print(soma)
        if soma % 3 == 0:
            print("sim")
        else:
            print("não")
    
    #main
    n = int(input("Nº de algarismos: "))
    m = input("Nº em si: ")
    DivPor3(n,m)
    
    resposta = input("Deseja continuar? [S/N]: ")
    if resposta.upper() == 'N':
        break
'''