class CaixaEletronico:
    
    def __init__(self, banco):
        self.__banco = banco
        
    
    def saldo(self, numero_conta):
        return self.__banco.saldo(numero_conta)
    
    def saque(self, numero_conta, valor):
        if self.__banco.saldo(numero_conta) >= valor and self.__tem_notas(valor):
            self.__banco.saque(numero_conta, valor)
            
    def deposito(self,numero_conta,valor):
        
        if self.__banco.saldo(numero_conta) >= valor and self.__tem_notas(valor):
            self.__banco.deposito(numero_conta, valor)
    
    def __tem_notas(self, valor):
        valores_notas = []
        qtd_notas = []

        for _ in range(n):
            valores_notas.append(float(input()))
            qtd_notas.append(int(input()))
        saque = float(input(valor))

        notas_necessarias = []
        for i in range(len(valores_notas)-1, -1, -1):
            valor = valores_notas[i]
            qtd = min(int(saque / valor), qtd_notas[i])
            saque -= qtd * valor
            notas_necessarias.append(qtd)

        print(*notas_necessarias[::-1])

        return True