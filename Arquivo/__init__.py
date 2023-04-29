from Ex115.funcoes import *


def arqexiste(nome):
    try:
        teste = open(nome, 'rt')
        teste.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        cria = open(nome, 'wt+')
        cria.close()
    except:
         print(f'Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        ler = open(nome, 'rt')
    except:
        print('Erro na leitura do arquivo!')
    else:
        cabeca('Pessoas Cadastradas')
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(ler.read())
    finally:
        ler.close()


def novoCad(arq, nome='<Desconhecido>', idade=0):
    try:
        ncad = open(arq, 'at')
    except:
        print(f'ERRO! Problemas ao abrir o arquivo.')
    else:
        try:
            ncad.write(f'{nome};{idade}\n')
        except:
            print('ERRO! Problemas na redação do novo cadastro.')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            ncad.close()
            
