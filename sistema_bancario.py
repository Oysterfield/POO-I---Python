from banco import Banco
from caixa_eletronico import CaixaEletronico

bc = Banco("Banco do Brejo", 999)
jj = Banco("Banco do Sul Brejo", 777)

cx1 = CaixaEletronico(bc)
cx2 = CaixaEletronico(jj)


while True:
    try:
        operacao, *parametros = input().split()
    except EOFError:
        break
    if operacao == 'abre_conta':
        cpf = parametros[0]
        nct = bc.abre_conta(parametros[-1], cpf)
    elif operacao == 'deposito':      
        cpf = parametros[0]
        nconta = bc.conta_dado_cpf(cpf)
        bc.deposito(nconta, float(parametros[-1]))
    elif operacao == 'saque':      
        cpf = parametros[0]
        nconta = bc.conta_dado_cpf(cpf)
        bc.saque(nconta, float(parametros[-1]))
    elif operacao == 'transferencia':  
        nconta_origem = bc.conta_dado_cpf(parametros[0])
        nconta_destino = bc.conta_dado_cpf(parametros[1])
        bc.transferencia(nconta_origem, nconta_destino, float(parametros[-1]))

for cpf, saldo in bc.relatorio_cpf_saldo():
    print(f"{cpf} {saldo:.2f}")

    