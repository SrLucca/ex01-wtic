from cadastro import cadastrar
from listar import listarpessoas

print('============ EX01 WTIc ============')
print('01 - PARA CADSTRAR')
print('02 - PARA LISTAR PESSOAS CADASTRADAS')
print('03 - PARA SAIR')

try:
    opcao = int(input('OPCAO: '))
except ValueError:
    print('Insira apenas numeros')

if opcao == 1:
    cadastrar()
if opcao == 2:
    listarpessoas()
if opcao == 3:
    exit(0)
