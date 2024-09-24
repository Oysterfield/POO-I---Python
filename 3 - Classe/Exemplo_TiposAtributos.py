#Entendo variável de classe e variável de instância

class Gato:
    '''classe para trabalhar com gatos.'''
    
    tipo_animal = "Felino"  #variável de classe (todas as instâncias recebem o mesmo valor)
    
    def __init__(self,nome):
        '''inicializa o objeto capturando o nome do animal'''
        self.nome = nome    #variável de instância (valores individuais por objeto instanciado)
                            # self indicando que é uma variável de instância
    

#main
g1 = Gato("Thomas")
g2 = Gato("Alfredo")

print(g1.tipo_animal)
print(g2.tipo_animal)

print(g1.nome)
print(g2.nome)

#é possível alterar o valor de uma variável de classe
Gato.tipo_animal = "Pet"
print(g1.tipo_animal)
print(g2.tipo_animal)

print(g1.nome)
print(g2.nome)

# é possível alterar o valor de uma variável de classe apenas para um objeto em particular
# após já ter sido instanciado este objeto
g1.tipo_animal = "Bichano"
print(g1.tipo_animal)
print(g2.tipo_animal)

print(g1.nome)
print(g2.nome)

        