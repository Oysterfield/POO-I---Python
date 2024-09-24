'''
#Exercício 1

for i in range(int(input("Número de idas à feira: "))):
    lista = []
    for i in range(int(input("Produtos disponíveis na feiras: "))):
        produtos = {}
        produtos['produto'] = (input("Nome do produto: "))
        produtos['preço'] = float(input("Preço do produto: "))
        lista.append(produtos)
    listaDona = []
    for i in range(int(input("Quantidade de produtos que deseja comprar: "))):
        produtosDona = {}
        produtosDona['produto'] = input("Nome do produto: ")
        produtosDona['quant'] = int(input("Quantidade do produto: "))
        listaDona.append(produtosDona)
    print(listaDona)
    soma = 0
    for i in lista:
        for j in listaDona:
            if i['produto'] == j['produto']:
                soma += i['preço']*j['quant']
                break
    print("R$ {:.2f}".format(soma))
    
'''
'''
#Exercício 2

lista = []
for i in range(int(input("Número de traduções: "))):
    idioma = {}
    idioma['lingua'] = input("Língua: ")
    idioma['traducao'] = input("Tradução: ")
    lista.append(idioma)
lista2 = []
for i in range(int(input("Quantidade de crianças: "))):
    crianca = {}
    crianca['nome'] = input("Nome: ")
    crianca['lingua'] = input("Língua: ")
    lista2.append(crianca)
for i in lista2:
    for j in lista:
        if j['lingua'] == i['lingua']:
            print(f"{i['nome']} \n{j['traducao']}\n")
'''
'''
#Exercício 3

while True:
    n = int(input("Quantidade de alunos na turma: "))
    if n == 0:
        break
    lista = []
    for i in range(n):
        aluno = {}
        aluno['nome'] = input("Nome: ").capitalize()
        aluno['assinatura'] = input("Assinatura: ")
        lista.append(aluno)
    lista2 = []
    falsasAssin = 0
    for i in range(int(input("Quantidade de alunos que compareceram: "))):
        aluno2 = {}
        aluno2['nome'] = input("Nome: ").capitalize()
        aluno2['assinatura'] = input("Assinatura: ")
        lista2.append(aluno2)
        for j in lista:
            falsas = 0
            if j['nome'] == lista2[i]['nome']:
                for k in range(len(j['assinatura'])):
                    if j['assinatura'][k] != lista2[i]['assinatura'][k]:
                        falsas +=1
                    if falsas > 1:
                        falsasAssin +=1
                        break
                break
    print(falsasAssin)

'''
'''
#Exercício 4

lista = [{'pais': 'brasil', 'traducao': 'Feliz Natal!'},
         {'pais': 'alemanha', 'traducao': 'Frohliche Weihnachten!'},
         {'pais': 'austria', 'traducao': 'Frohe Weihnacht!'},
         {'pais': 'coreia', 'traducao': 'Chuk Sung Tan!'},
         {'pais': 'espanha', 'traducao': 'Feliz Navidad!'},
         {'pais': 'grecia', 'traducao': 'Kala Christougena!'},
         {'pais': 'estados-unidos', 'traducao': 'Merry Christmas!'},
         {'pais': 'inglaterra', 'traducao': 'Merry Christmas!'},
         {'pais': 'australia', 'traducao': 'Merry Christmas!'},
         {'pais': 'portugal', 'traducao': 'Feliz Natal!'},
         {'pais': 'suecia', 'traducao': 'God Jul!'},
         {'pais': 'turquia', 'traducao': 'Mutlu Noeller!'},
         {'pais': 'argentina', 'traducao': 'Feliz Navidad!'},
         {'pais': 'chile', 'traducao': 'Feliz Navidad!'},
         {'pais': 'mexico', 'traducao': 'Feliz Navidad!'},
         {'pais': 'antardida', 'traducao': 'Merry Christmas!'},
         {'pais': 'canada', 'traducao': 'Merry Christmas!'},
         {'pais': 'irlanda', 'traducao': 'Nollaig Shona Dhuit!'},
         {'pais': 'belgica', 'traducao': 'Zalig Kerstfesst!'},
         {'pais': 'italia', 'traducao': 'Buon Natale!'},
         {'pais': 'libia', 'traducao': 'Buon Natale!'},
         {'pais': 'siria', 'traducao': 'Milad Mubarak!'},
         {'pais': 'marrocos', 'traducao': 'Milad Mubarak!'},
         {'pais': 'japao', 'traducao': 'Merii Kurisumasu!'},]

while True:
    m = input("Digite o país: ")
    if m == '0':
        break
    flag = False
    for i in lista:
        if m == i['pais']:
            print(i['traducao'])
            flag = True
            break
    if flag == False:
        print("--- NOT FOUND ---")

'''
'''
#Exercício 5

def Solitario(lista):
    for j in range(len(lista)):
        flag = False
        for k in range(len(lista)):
            if j != k and lista[j] == lista[k]:
                lista.pop(j)
                lista.pop(k-1)
                flag = True
                break
        if flag == False:
            print(lista[j])
            lista = [lista[j]]
            return
            break
        else:
            return lista
            break
                
while True:
    n = int(input("Quantidade de nºs:"))
    if n == 0:
        break
    dicio = {}
    lista = []
    for i in range(n):
        lista.append(int(input("Add um nº: ")))
    
    while len(lista) != 1:
        lista = Solitario(lista)
        if len(lista) == 1:
            print(lista[0])

'''
'''
#Exercício 6

while True:
    epr = 0
    ehd = 0
    intrusos = 0
    n = int(input("Número de alunos: "))
    if n == 0:
        break
    for i in range(n):
        aluno = {}
        aluno['matrícula'] = input("Matrícula: ")
        aluno['sigla'] = input("Sigla do curso: ")
        if aluno['sigla'] == 'EPR':
            epr +=1
        elif aluno['sigla'] == 'EHD':
            ehd +=1
        else:
            intrusos +=1
    print(f"EPR: {epr} \nEHD: {ehd} \nINTRUSOS: {intrusos}")

'''
'''
#Exercício 7

def Funcao(lista2,lista):
    salario = 0
    for i in lista:
        if i['palavra'] in lista2:
            salario += i['valor']*lista2.count(i['palavra'])
    print(salario)
    
m = int(input("Quantidade de palavras no dicionário: "))
n = int(input("Quantidade de descrições: "))
lista = []
for i in range(m):
    dicio = {}
    dicio['palavra'] = input("Palavra: ")
    dicio['valor'] = int(input("Valor: "))
    lista.append(dicio)
lista2 = []
for i in range(n):
    lista2.append(input("Descrição:"))
    Funcao(lista2[i],lista)
    
'''
'''
#Exercício 8

while True:
    x = int(input("Quantidade de participantes: "))
    if x == 0:
        break
    lista = []
    for i in range(x):
        dicio = {}
        dicio['nome'] = input("Nome: ")
        for j in range(1,4):
                  
        lista.append(dicio)
    
    while True:
        consulta = {'nome':f'{input("Nome: ")}','presente':f'{input("Presente: ")}'}
        for i in lista:
            if consulta['nome'] == i['nome']:
                if consulta['presente'] in i:
                    print("Uhul! Seu amigo secreto vai adorar o/")
                else:
                    print("Tente Novamente!")
                    
        if input("Deseja continuar?[S/N]: ").upper() == 'N':
            break
    
'''
'''
#Exercício 9
dicio = {'w': 1,
'h': 0.5,
'q': 0.25,
'e': 0.125,
's': 0.0625,
't': 0.03125,
'x': 0.015625}
while True:
    n = input("Composição: ")
    if n == '*':
        break
    
    compassos = -1
    errados = 0
    count = 0
    for i in range(len(n)):
        if n[i] != '/':
            count += dicio[f'{n[i]}']
        if i < len(n)-1 and n[i+1] == '/':
            if count != 1:
                errados +=1
        if n[i] == '/':
            count = 0
            compassos +=1
    print(compassos - errados)

'''
'''
#Exercício 10

lista = []
dicio = {}
while True:
    print("----------- MENU -----------\n1) Cadastrar usuário \n2) Imprimir dados (pesquisar pelo nome) \n3) Imprimir dados (todos os usuários) \n4) Encerrar programa")
    n = int(input(": "))
        
    if n == 1:
        dicio['nome'] = input("Nome: ").capitalize()
        nascimento = int(input("Ano de nascimento: "))
        dicio['idade'] = 2023 - nascimento
        dicio['clt'] = int(input("CLT: "))
        if dicio['clt'] != 0:
            dicio['contrat'] = int(input("Ano de contratação: "))
            dicio['salário'] = int(input("Salário: "))
            dicio['aposentar'] = dicio['contrat'] - nascimento + 35
        lista.append(dicio.copy())
    if n == 2:
        flag = False
        consulta = input("Pesquisar nome: ").capitalize()
        for i in lista:
            if consulta == i['nome']:
                print(i)
                flag = True
        if flag == False:
            print("Cadastro não encontrado")
        
    if n == 3:
        print(lista)
        
    if n == 4:
        break
'''