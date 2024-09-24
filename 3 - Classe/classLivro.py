class Livro:
    def __init__(self,nome,qtd,autor,preco):
        self.nome = nome
        self.qtd = qtd
        self.autor = autor
        self.preco = preco
        
    def getNome(self):
        return self.nome
    
    def getPreco(self):
        return self.preco
    
    def setPreco(self,preco):
        self.preco = preco
        
#main
l1 = Livro("POO",120,"João Silva",250)

print(l1.getNome())
print(