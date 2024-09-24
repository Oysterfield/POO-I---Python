#Exercício 1
class Cubo:
    def __init__(self,valor):
        self.x = valor
    
    def calcula_cubo(self):
        cubo = self.x * self.x * self.x
        return "Cubo calculado: "+ str(cubo)

#main
cubo1 = Cubo(int(input("Nº que deseja saber o cubo: ")))
print(cubo1.calcula_cubo())