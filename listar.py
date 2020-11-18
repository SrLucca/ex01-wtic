def listarpessoas():
    while(True):
        print('============ LISTAR ============')
        print('As pessoas cadastradas são:')

        with open('cadastrados.txt') as c:
            for linha in c:
                print(linha)
        break
