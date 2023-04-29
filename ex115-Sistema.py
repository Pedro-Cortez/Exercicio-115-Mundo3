from funcoes import menu, cores, opcao
from Ex115.arquivo import *

arq = 'pessoas.txt'

if not arqexiste(arq):
    criarArquivo(arq)

menu(['Cadastrar novo', 'Listar cadastrados', 'Sair do Sistema'])
resp = opcao(f'{cores("amar")}Sua opção:{cores("limpa")} ')
