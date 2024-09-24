class Cliente:
    def __init__(self,raca,idade,nomeAnimal,nomeDono,mensalidade):
        self.raca = raca
        self.idade = idade
        self.nomeAnimal = nomeAnimal
        self.nomeDono = nomeDono
        self.mensalidade = mensalidade
        
    def imprimir(self):
        print(f"{self.raca}\n{self.idade}\n{self.nomeAnimal}\n{self.nomeDono}\n{self.mensalidade}")
    
    def getIdade(self):
        return self.idade
    

class ClienteVIP(Cliente):
    def __init__(self,restriAliment,raca,idade,nomeAnimal,nomeDono,mensalidade):
        super().__init__(raca,idade,nomeAnimal,nomeDono,mensalidade)
        self.restriAliment = restriAliment
    
    def getRestriAliment(self):
        if self.restriAliment == True:
            return "Sim"
        elif self.restriAliment == False:
            return "Não"

#main
while True:    
    n = int(input("Escolha: "))
    if n == 0:
        break
    
    elif n == 1:
        #a) Cadastrar cliente (cão):
        p1 = Cliente("Pastor Alemão",8,"Juan","Jorge",50)
        p1 = ClienteVIP(0,"Pastor Alemão",8,"Juan","Jorge",50)
        p2 = Cliente("Chow Chow",4,"Logan","Yuri",70)
        idoso = []
        idoso.append(p1.idade)
        idoso.append(p2.idade)

    elif n == 2:
        #b) Imprimir informações do cliente cadastrado:
        print(p1.raca,p1.idade,p1.nomeAnimal,p1.nomeDono,p1.mensalidade)
    
    elif n == 3:    
        #c) Criar um método que verifica (retorna) se determinado cão possui restrição alimentar:
        print(p1.getRestriAliment)

    elif n == 4:    
        #d) Criar um método que verifique a mensalidade do cachorro (calcular a partir do número de banhos por mês (R$ 25,00 por banho)
        print()
    elif n == 5:
        #e) Criar um método que verifique qual o cachorro mais idoso
        idoso.sort()
        print(idoso[len(idoso) - 1])
