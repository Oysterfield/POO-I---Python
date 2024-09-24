class Veiculo:
    def __init__(self, cor, marca, modelo, tanque):
        self.tanque = tanque
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        
    def abastecer(self, litros):
        print('Abastecendo...' + str(litros) + " litros")
        self.tanque += litros
        
    def __str__(self):
        print('O Veiculo: ' + self.marca + " " + self.modelo + " está com " +
              str(self.tanque) + " litros no tanque.")
  
  
class Carro(Veiculo):
    def __init__(self, cor, marca, modelo, tanque, ano):
        super().__init__(cor, marca, modelo, tanque)
        self.ano = ano
        self.limit = 50
        
    def abastecer(self, litros):
        print('Tentando abastecer: ' + str(litros) + " litros")
        if self.tanque + litros > self.limit:
            print('Capacidade máxima alcançada, foi possível abastecer: ' +
                  str(self.limit - self.tanque) + ' litros.')
            self.tanque = self.limit
        else:
            self.tanque += litros

#main
v1 = Veiculo('azul', 'Scania', 'R450', 10)
c1 = Carro('Grafite', 'Fiat', 'Argo', 25, 2020)

# instancia da classe Veiculo abastecendo
v1.__str__()
v1.abastecer(50)
v1.__str__()
v1.abastecer(30)
v1.__str__()
v1.abastecer(40)

print()

# instância da classe Carro abastecendo
# a instancia c1 irá executar o método abastecer que está
#definido na Classe Carro (polimorfismo)
#irá executar o método __str__() na super classe Veiculo(herança)
c1.__str__()
c1.abastecer(10)
c1.__str__()
c1.abastecer(20)
c1.__str__()
c1.abastecer(40)

print()