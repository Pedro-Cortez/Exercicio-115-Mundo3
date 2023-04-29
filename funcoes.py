from Ex115 import arquivo

lista = ['Cadastrar novo', 'Listar cadastrados', 'Sair do Sistema']
arq = 'pessoas.txt'


def cabeca(frase):
    print('==' * 20)
    print(f'{frase}'.center(40))
    print('==' * 20)
    return


def menu(lista):
    cabeca('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'{cores("amar")}{cont} -{cores("limpa")} {cores("azul")}{item}{cores("limpa")}')
        cont += 1
    print(f'==' * 20)


def cores(cor):
       c = {'verm':'\033[1;31m',
           'verd':'\033[1;32m',
           'amar':'\033[1;33m',
           'lilas':'\033[1;35m',
           'azul':'\033[1;36m',
           'limpa':'\033[m'}
       return c[cor]


def opcao(opc):
    escolha = 0
    while True:
        resp = str(input(opc))
        try:
            escolha = int(resp)
            if escolha == 1:
                cabeca('Novo Cadastro')
                nome = str(input('Nome: '))
                idade = int(input('Idade: '))
                arquivo.novoCad(arq, nome, idade)
                menu(lista)
            elif escolha == 2:
                    cabeca('Listar Cadastrados')
                    arquivo.lerArquivo(arq)
                    menu(lista)
            elif escolha == 3:
                cabeca('Saindo do sistema...Até logo!')
                break
            else:
                print(f'{cores("verm")}ERRO! Digite uma opção válida.{cores("verm")}')
        except ValueError:
            print(f'{cores("verm")}Erro! Informe um número inteiro válido!{cores("verm")}')
