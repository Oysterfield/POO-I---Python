'''
#Exercício 2

class Aluno:
    def __init__(self,nome,curso,tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir
        
    def estudar(self,estudo):
        self.tempoSemDormir += estudo
        
    def dormir(self,sono):
        self.tempoSemDormir -= sono
        
        
aluno = Aluno("Tiago","POO",16)
aluno.estudar(6)
aluno.dormir(8)
print(aluno.tempoSemDormir)

'''
class Carro:
    def __init__(self,consumo):
        self.consumo = consumo
        self.tanque = 0
        
    def andar(self,distancia):
        self.tanque -= distancia/self.consumo
        
    def obterGasolina(self):
        print(self.tanque)
    
    def adicionarGasolina(self,gasolina):
        self.tanque += gasolina
        
meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
meuFusca.obterGasolina()