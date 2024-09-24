#Trabalho POO

class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        
    def getUserNome(self):
        return self.nome
    
    def getUserEmail(self):
        return self.email
    
    def getUserSenha(self):
        return self.senha
    
    def setUserNome(self,nome):
        self.nome = nome
        
    def setUserEmail(self,email):
        self.email = email
        
    def serUserSenha(self,senha):
        self.senha = senha
        
#class Herança:        
class UsuarioPro(Usuario):
    def __init__(self,userPro,nome,email,senha):
        super().__init__(nome,email,senha)
        self.userPro = userPro

#class Polimorfismo:


class Filme:
    def __init__(self,nome,estrelas,ano,generos):
        self.nome = nome
        self.estrelas = estrelas
        self.ano = ano
        self.generos = generos
        
    def getFilme(self):
        print(f"\nNome: {self.nome}\nEstrelas: {self.estrelas}\nAno: {self.ano}\nGênero(s): {self.generos}")
        
class ListaDesejos:
    def __init__(self,nome,ano,generos):
        self.nome = nome
        self.ano = ano
        self.generos = generos
        
        

#main
cadastro = False
reviews = 0
lisDes = 0
reviewsLista = []
lisDesLista = []
while True:
    n = input("1 - Cadastro\n2 - Login\n3 - Fechar app\nOpção: ")
    while n != '1' and n != '2' and n != '3':
        n = input("Valor inválido. Digite novamente: ")
    n = int(n)
    
    if n == 3:
        break
    
    if n == 1:
        nome = input("Nome de usuário: ")
        email = input("E-mail: ")
        senha = input("Senha: ")
        senhaConfirm = input("Confirmar senha: ")
        while senha != senhaConfirm:
            senha = input("Senhas diferentes! Digite novamente\nSenha: ")
            senhaConfirm = input("Confirmar senha: ")
        u1 = Usuario(nome,email,senha)
        cadastro = True
        
    elif n == 2:
        if cadastro == False:
            print("Para logar, deve haver no mínimo 1 cadastro!")
            break
        else:
            print("="*15)
            print("  Modo Login")
            print("="*15)
            loginEmail = input("E-mail: ")
            loginSenha = input("Senha: ")
            if loginEmail != u1.email:
                print("Usuário inexistente\n")
            elif loginEmail == u1.email and loginSenha != u1.senha:
                print("Senha incorreta\n")
            else:                    
                while True:
                    m = input("1 - Adicionar review\n2 - Adicionar à lista de desejos\n3 - Buscar filme\n4 - Ver estatísticas\n5 - Gerenciar conta\n6 - Logout\nOpção: ")
                    while m != '1' and m != '2' and m != '3' and m != '4' and m != '5' and m != '6':
                        m = input("Valor inválido. Digite novamente: ")
                    m = int(m)
                    
                    if m == 6:
                        break
                    
                    if m == 1:
                        nome = input("Nome: ")
                        estrelas = input("Estrelas (1 a 10): ")
                        while estrelas != '1' and estrelas != '2' and estrelas != '3' and estrelas != '4' and estrelas != '5' and estrelas != '6' and estrelas != '7' and estrelas != '8' and estrelas != '9' and estrelas != '10':
                            estrelas = input("Valor imcompatível. Digite novamente: ")
                        estrelas = int(estrelas)
                        ano = input("Ano: ")
                        generos = input("Gênero(s): ")
                        f1 = Filme(nome,estrelas,ano,generos)
                        reviews += 1
                        reviewsLista.append(f1.nome)
                    
                    elif m == 2:
                        nome = input("Nome: ")
                        ano = int(input("Ano: "))
                        generos= input("Gênero(s): ")
                        l1 = ListaDesejos(nome,ano,generos)
                        lisDes += 1
                        lisDesLista.append(l1.nome)
                    
                    elif m == 3:
                        try:
                            f1
                        except NameError:
                            print("Não há filmes!")
                        else:
                            f1.getFilme()
                        
                    elif m == 4:
                        print("-"*15)
                        print(f"ESTATÍSTICAS\nNº de reviews: {reviews}\n:{reviewsLista}\nNº na Lista de Desejos: {lisDes}\n:{lisDesLista}")
                        print("-"*15)
                        
                    elif m == 5:
                        while True:
                            p = input("\n1 - Consultar informações\n2 - Alterar nome\n3 - Alterar e-mail\n4 - Alterar senha\n5 - Mudar para PRO\n6 - Excluir conta\n7 - Voltar\nOpção:")
                            while p != 1 and p != 2 and m != 3 and m != 4 and m != 5 and m != 6:
                                p = input("Valor inválido. Digite novamente: ")
                            p = int(p)
                            
                            if p == 1:
                                print(f"Nome: {u1.getUserNome()}\nE-mail: {u1.getUserEmail()}\nSenha: getUserSenha(u1)")
                            
                            elif p == 2:
                                u1.setUserNome(input("Novo nome: "))
                                
                            elif p == 3:
                                u1.setUserEmail(input("Novo e-mail: "))
                                
                            elif p == 4:
                                u1.setUserSenha(input("Nova senha: "))
                            
                            elif p == 5:
                                globals()[str] = UsuarioPro(str.nome,str.email,str.senha)
                            
                            elif p == 6:
                                del u1
                            
                            elif p == 7:
                                break