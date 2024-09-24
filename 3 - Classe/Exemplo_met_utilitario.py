# Exemplo método utilitário

class Cao:
  '''Classe para cães''' 
  def __init__(self, nome):
    '''inicializa o objeto capturando o nome do animal'''
    self.nome = nome
    print('Seu cão se chama', self.nome)

  def peso_cao(self, peso):
    self.peso = peso       #atributo interno do método
    if (self.peso > 10):
      print('Seu cão é de grande porte')
    elif (self.peso > 5):
      print('Seu cão é de médio porte')
    else:
      print('Seu cão é de pequeno porte')

  def _dieta_cao(self):       #método utilitário (invocado por outro método desta classe)
    if (self.peso > 10):
      self.msg = 'Utilize ração para grandes animais'
    elif (self.peso > 5):
      self.msg = 'Utilize ração para animais médios'
    else:
      self.msg = 'Utilize ração para pequenos animais'

    return self.msg

  def dados_cao(self):
    print('\nO cão', self.nome, 'está com', self.peso, 'kg')
    print(self._dieta_cao())


#main
nome_cao = input('Qual o nome do seu cão? ')
c1 = Cao(nome_cao)

peso = float(input('Digite o peso do seu cão'))
c1.peso_cao(peso)
c1.dados_cao()

