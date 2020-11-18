def cadastrar():
    print("============ CADASTRO ============")
    while(True):
        try:
            nome = str(input('Insira seu nome: '))
        except ValueError:
            print('Insira apenas letras')
            continue
        try:
            idade = int(input('Insira sua idade: '))
        except ValueError:
            print('Insira apenas numeros')
            continue
        try:
            profissao = str(input('Insira sua profissão: '))
        except ValueError:
            print('Insira apenas letras: ')
            continue
        
        arquivo = open('cadastrados.txt','w')
        arquivo.writelines('\nNome: {}\nIdade: {}\nProfissão: {}\n'.format(nome,idade,profissao))
        arquivo.close()

        print('CADASTRADO COM SUCESSO!!')

        break
