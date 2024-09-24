'''
#Exercício 1
casa = float(input("Valor da casa = "))
salário = float(input("Seu salário = "))
anos = float(input("Em quantos anos deseja pagar = "))
prestação_mensal = anos*12
if (prestação_mensal > casa*0,3):
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")
'''
'''
#Exercício 2
valor = float(input("Valor do produto = "))
condicao_pag = int(input("(1) à vista, (2) 1x no cartão, (3) 2x no cartão, (4) 3x ou mais no cartão. Escolha sua forma de pagamento = "))
if (condicao_pag == 1):
    print(valor*0.9)
elif (condicao_pag == 2):
    print(valor*0.95)
elif (condicao_pag == 3):
    print(valor)
elif (condicao_pag == 4):
    print(valor*1.20)
else:
    print("Opção inválida")
'''
'''
#Exercício 3
peso = float(input("Digite seu peso = "))
altura = float(input("Digite sua altura = "))
imc = peso/(altura*altura)
if (imc < 18.5):
    print("abaixo do peso")
elif (imc >= 18.5) and (imc < 25):
    print("peso ideal")
elif (imc >= 25) and (imc < 30):
    print("sobrepeso")
elif (imc >= 30) and (imc < 40):
    print("obesidade")
else:
    print("obesidade mórbida")
'''
'''
#Exercício 4
nota1 = ("Nota 1 = ")
nota2 = ("Nota 2 = ")
nota3 = ("Nota 3 = ")
media = (nota1 + nota2 + nota3)/3
if (media < 5):
    print("Reprovado")
elif (media >= 5) and (media < 7):
    print("Em recuperação")
else:
    print("Aprovado")
'''
'''
#Exercício 5) 1051
salario = float(input("Salário = "))
if (salario <= 2000.00):
    print("Você está isento")
elif (salario >= 2000.01) and (salario <= 3000.00):
    print((salario - 2000.00)*0.08)
elif (salario >= 3000.01) and (salario <= 4500.00):
    print((salario - 3000.00)*0.18 + (salario - 3000.00)*0.08)
else:
    print((salario - 2000.00)*0.08 + (salario - 3000.00)*0.18 + (salario - 4500.00)*0.28)
'''
'''
#Exercicio 6) 1061
dia_inicio = int(input("Dia "))
hora, minu, seg = input("  :" "  :" "  ").split()
hora = int(hora)
minu = int(minu)
seg = int(seg)
dia_fim = int(input("Dia "))
horario_fim = input("  :" "  :" "  ").split()
hora_fim = int(hora_fim)
minu_fim = int(minu_fim)
seg_fim = int(seg_fim)
print( "dia(s)" "hora(s)" "minuto(s)" "segundo(s)" )
'''
'''
#Exercício 7) 1050
ddd = int(input("DDD: "))
if (ddd = 61):
    print("Brasilia")
if (ddd = 71):
    print("Salvador")
if (ddd = 11):
    print("Sao Paulo")
if (ddd = 21):
    print("Rio de Janeiro")
if (ddd = 32):
    print("Juiz de Fora")
if (ddd = 19):
    print("Campinas")
if (ddd = 27):
    print("Vitoria")
if (ddd = 31):
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")
'''
'''
#Exercicio 8) 1052
mes = int(input("Mês: "))
if (mes == 1):
    print("January")
if (mes == 2):
    print("February")
if (mes == 3):
    print("March")
if (mes == 4):
    print("April")
if (mes == 5):
    print("May")
if (mes == 6):
    print("June")
if (mes == 7):
    print("July")
if (mes == 8):
    print("August")
if (mes == 9):
    print("September")
if (mes == 10):
    print("October")
if (mes == 11):
    print("November")
if (mes == 12):
    print("December")
     + b)/ 2*a
'''
'''
#Exercicio 9) 1036
import math
a = float(input("Primeira Variável: "))
b = float(input("Segunda Variável: "))
c = float(input("Terceira Variável: "))
raizes = b*b - 4*a*c
raiz_1 = (math.sqrt(raizes) - b)/(2*a)
raiz_2 = (math.sqrt(raizes) + b)/(2*a)
print(raiz_1)
print(raiz_2)
if (/zero):
    print("Impossível calcular")
'''
'''
#Exercicio 10) 2408
a, b, c = input("Os três competidores são: ").split()
a = int(a)
b = int(b)
c = int(c)
if (b < a < c) or (c < a < b):
    print(a)
elif (a < b < c) or (c < b < a):
    print(b)
else:
    print(c)
'''
'''
#Exercicio 11) 2417
cv, ce, cs, fv, fe, fs = input("Vitórias, empates e saldos de gols do Cormengo e Flaminthians, respectivamente").split()
cv = int(cv)*3
ce = int(ce)
cs = int(cs)
fv = int(fv)*3
fe = int(fe)
fs = int(fs)
total_corm = cv + ce
total_flam = fv + fe
if (total_corm > total_flam):
    print("C")
elif (total_flam > total_corm):
    print("F")
elif (total_corm == total_flam):
    (cs > fs):
    print("C")
elif (cs > fs):
    print("F")
else:
    print("=")
'''
#Exercício 12) 2568
'''
'''
#Exercício 13) 2600
'''
#Exercício 14) 1046
hora_inicial = int(input("Hora inicial do jogo: "))
hora_final = int(input("Hora final do jogo: "))
if (hora_inicial < 1) or (hora_inicial > 24) or (hora_final < 1) or (hora_final > 24):
    print("Algum dado incorreto")
duracao = (hora_final - hora_inicial)
if (duracao < 0):
    print(duracao + 24)
else:
    print(duracao)
'''
'''
#Exercício 15) 1047
h_i = int(input("Hora de início: "))
m_i = int(input("Minuto de início: "))
h_f = int(input("Hora final: "))
m_f = int(input("Minuto final: "))
if (h_1 < 1) or (h_i > 24) or (m_i < 1) or (m_i > 60) or (h_f < 1) or (h_f > 24) or (m_f < 1) or (m_f > 60):
    print("Algum dado incorreto")
duracao_m = (m_f - m_i)
if (duracao_m < 0):
    duracao_m_certa = duracao + 60
print(f"O JOGO DUROU {duracao_h} HORA(S) E {duracao_m} MINUTO(S)")
'''
'''
#Exercicio 16) 2375
salario = float(input("Seu salário: "))
if (0 <= salario <= 400):
    print(f"Novo salário: {salario*1.15}")
elif (400.01 <= salario <= 800):
    print(f"Novo salário: {salario*1.12}")
elif (800.01 <= salario <= 1200):
    print(f"Novo salário: {salario*1.10}")
elif (1200.01 <= salario <= 2000):
    print(f"Novo salário: {salario*1.07}")
else:
    print(f"Novo salário: {salario*1.04}")
'''
#Exercicio 17) 1048
    
#Exercicio 18) 2409
'''
#Exercício 19) 1035
a, b, c, d = int(input("Digite os quatro valores: ")).split()
if (b > c) and (d > a) and (c + d > a + b) and (c > 0) and (d > 0) and (a):
    print("Valores aceitos")
else:
    print("Valores não aceitos")
'''
'''
#Exercício 20) 1038
cod = int(input("Digite o código do item: "))
quant = int(input("Digite a quantidade do item: "))
if (cod == 1):
    print("Total: R$ {:.2f}".format(quant*4.00))
elif (cod == 2):
    print("Total: R$ {:.2f}".format(quant*4.50))
elif (cod == 3):
    print("Total: R$ {:.2f}".format(quant*5.00))
elif (cod == 4):
    print("Total: R$ {:.2f}".format(quant*2.00))
elif (cod == 5):
    print("Total: R$ {:.2f}".format(quant*1.50))
'''
'''
#Exercício 21) 2339
c = int(input("Número de competidores: "))
if (c < 1) or (c > 1000):
    print("Número de competidores inválido")
p = int(input("Quantidade de folhas de papel: "))
if (p < 1) or (p > 1000):
    print("Quantidade de folhas de papel inválida")
f = int(input("Quantidade que cada competidor deve receber: "))
if (f < 1) or (f > 1000):
    print("Quantidade que cada competidor deve receber inválido")

print("S")
print("N")
'''
'''
#Exercício 22) 1045
a = float(input("Lado 1 do triângulo: "))
b = float(input("Lado 2 do triângulo: "))
c = float(input("Lado 3 do triângulo: "))
if (a <= 0) or (b <= 0) or (c <= 0):
    print("Algum número inválido")
if (a > b > c):
    a1 = a
if (a >= b + c):
    print("NAO FORMA TRIANGULO")
elif (a**2 == b**2 + c**2):
    print("TRIANGULO RETANGULO")
elif (a**2 > b**2 + c**2):
    print("TRIANGULO OBTUSANGULO")
elif (a**2 < b**2 + c**2):
    print("TRIANGULO ACUTANGULO")
if (a == b == c):
    print("TRIANGULO EQUILATERO")
elif (a == b) or (a == c) or (b == c):
    print("TRIANGULO ISOSCELES")
'''