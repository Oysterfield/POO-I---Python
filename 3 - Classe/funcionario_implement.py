from funcionario import Funcionario
        
f2 = Funcionario("João",3000)
f3 = Funcionario("Tatiana",3200)
f4 = Funcionario("Rogério",2750)

while True:
    n = int(input("1 - Cadastrar funcionário\n2 - Consultar salário\n3 - Calcular aumento"))
    if n == 0:
        break
    
    elif n == 1:
        f1 = Funcionario(input("Nome: "),int(input("Salário: ")))
        
    elif n == 2:
        print(f1.getSalario())
    
    elif n == 3:
        f1.NovoSalario()