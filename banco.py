import ficha_bancaria

class Banco:
    
    def __init__(self, nome_banco, codigo_banco):
        self.__nome = nome_banco
        self.__numero = codigo_banco
        self.__ultima_conta_criada = 0
        self.__fichario = {}
        
    def abre_conta(self, nome_cliente, cpf_cliente):
        ''' Abre uma nova conta no banco '''
        
        self.__ultima_conta_criada += 1
        
        ficha = FichaBancaria()
        ficha.set_numero(self.__ultima_conta_criada)
        ficha.set_nome(nome_cliente)
        ficha.set_cpf(cpf_cliente)
        self.__fichario[self.__ultima_conta_criada] = ficha
        return self.__ultima_conta_criada
  
    def conta_dado_cpf(self, cpf):
        for ficha in self.__fichario.values():
            if ficha.get_cpf() == cpf:
                return ficha.get_numero()
        return -1
    
    def relatorio_cpf_saldo(self):
        pares = list()
        for ficha in self.__fichario.values():
            pares.append( (ficha.get_cpf(), ficha.get_saldo()) )
        pares.sort()
        return pares
  
    def deposito(self, numero_conta, valor):
        ''' Realiza um depósito numa conta '''
        
        if numero_conta in self.__fichario:
            self.__fichario[numero_conta].credite(valor)
            return True
        else:
            return False
            
    def saque(self, numero_conta, valor):
        ''' Realiza um saque numa conta '''
        

        return None
    
    def transferencia(self, nct_origem, nct_destino, valor):
        ''' Realiza transferência entre duas contas '''
        
        if nct_origem in self.__fichario and nct_destino in self.__fichario:
            ficha_origem = self.__fichario[nct_origem]
            ficha_destino = self.__fichario[nct_destino]
            if ficha_origem.get_saldo() >= valor:
                ficha_origem.debite(valor)
                ficha_destino.credite(valor)
                return True
        return False

    def saldo(self, numero_conta):       
        ''' Obtém o saldo de uma conta '''
        
        return None
 
    def encerra_conta(self, numero_conta):
        ''' Encerra uma conta '''
        
        if numero_conta in self.__fichario and self.saldo(numero_conta) == 0:
            del self.__fichario[numero_conta]
            return True
        else:
            return False
        
    def conta_maior_saldo(self):
        '''Obtém o nº da conta do cliente com maior saldo'''
        
        maior_saldo = -math.inf
        nct = 0
        for ficha in self.__fichario.values():
            if ficha.get_saldo() > maior_saldo:
                maior_saldo = ficha.get_saldo()
                nct = ficha.get_numero()
        return nct

    def saldo_medio(self):
        '''Cálcula o saldo médio dos correntistas'''
        
        saldo = 0
        num_fichas = 0
        for ficha in self.__fichario.values():
            saldo += ficha.get_saldo()
            num_fichas += 1
        media = saldo / num_fichas
        return media
    
    def cpfs_duplicados(self):
        ''' Obtém os cpfs duplicados (em mais de uma conta) '''
        cpfs = set()
        cpfs_duplicados = set()
        for ficha in self.__fichario.values():
            cpf = ficha.get_cpf()
            if cpf in cpfs:
                cpfs_duplicados.add(cpf)
            else:
                cpfs.add(cpf)
                
        return cpfs_duplicados