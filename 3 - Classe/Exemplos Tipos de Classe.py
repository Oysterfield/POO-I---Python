#Herança:
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def setNome(self,nome):
        self.nome = nome
        
    def setIdade(self,idade):
        self.idade = idade
        
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
class PessoaFisica(Pessoa):
    def __init__(self,cpf,nome,idade):
        super().__init__(nome,idade)
        self.CPF = cpf
        
    def setCPF(self,cpf):
        self.CPF = cpf
        
    def getCPF(self):
        return self.cpf
    
class PessoaJuridica(Pessoa):
    def __init__(self,cnpj,nome,idade):
        super().__init__(nome,idade)
        self.CNPJ = cnpj
        
    def setCPF(self,cnpj):
        self.CNPJ = cnpj
        
    def getCPF(self):
        return self.cnpj
    
    
    
#Polimorfismo:
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



#Agregação:
class



#Histórico:
import datetime
class Historico():
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
        
    def imprime(self):
        print("data abertura: {}".format(self.data_abertura))
        print("transações: ")
        for t in self.transacoes:
            print("-",t)
            
class Conta():
    def __init__(self,numero,cliente,saldo,limite):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()