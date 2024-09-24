'''
#INCOMPLETO!!!
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
