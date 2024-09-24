class FichaBancaria:

    def __init__(self,num_conta,nome,cpf) -> None:
        self.num_conta = num_conta
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def set_num_conta(self,num_conta):
        self.num_conta = num_conta

    def set_nome(self,nome):
        self.nome = nome

    def set_cpf(self,cpf):
        self.cpf = cpf

    def credite(self,valor):
        self.saldo += valor

    def debite(self,valor):
        self.saldo -= valor

    def get_num_conta(self):
        return self.num_conta
    
    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def get_saldo(self):
        return self.saldo