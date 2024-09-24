class Funcionario:
    def __init__(self,funcionario, salario):
        self.funcionario = funcionario
        self.salario = salario

    def getFuncionario(self):
        return self.funcionario
        
    def getSalario(self):
        return self.salario
    
    def NovoSalario(self):
        if self.salario <= 2000:
            salarioNovo = self.salario + (self.salario*15)/100
        elif 2000 < self.salario <= 3000:
            salarioNovo = self.salario + (self.salario*10)/100
        elif self.salario > 3000:
            salarioNovo = self.salario + (self.salario*5)/100

        print(self.funcionario,f"Salário antigo: {self.salario},Salário atual: {salarioNovo}")
