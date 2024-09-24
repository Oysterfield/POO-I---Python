#Exemplo 001
#cadastro de Pessoa
class Pessoa:
    def __init__(self,nome1, idade1):
        self.nome = nome1
        self.idade = idade1
      
    def consulta_nome(self):
        return self.nome
    
    def consulta_idade(self):
        return self.idade
    
    def altera_nome(self,nome):
        self.nome = nome
    
    def altera_idade(self,idade):
        self.idade = idade
        
'''     
#main

#lendo valores do teclado para criar um objeto (instancia) da Classe Pessoa
nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))
#p1 é um objeto, ou seja, uma instância da Classe Pessoa
p1 = Pessoa(nome, idade)

c= p1.consulta_nome()
print(c)

print(p1.consulta_idade())


p2 = Pessoa("joao", 30)
print(p2.nome)

# alternativa (utilizar a invocação ao método)
print("Pessoa: ",p1.consulta_nome())
print("Pessoa: ",p1.consulta_idade())





#alterando a informação de um objeto

#acessando diretamente o atributo
p1.nome = input("Digite novo nome para Pessoa1: ")
print(p1.nome)
'''

#exemplo do uso do método
nome = input("Digite novo nome para Pessoa 1: ")
idade = int(input("Digite nova idade para Pessoa 1: "))
p1 = Pessoa(nome,idade)
print("Nome original: ", p1.consulta_nome())
p1.altera_nome("MariaSouza")
print("Nome atualizado: ", p1.consulta_nome())
p1.altera_idade(idade)
print("Idade atualizada: ", p1.consulta_idade())