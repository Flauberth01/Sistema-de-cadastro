from exdesafio.lib.interface import *
from exdesafio.lib.arquivo import *
from time import sleep

arquivo = 'banco.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Adicionar usúario', 'Listar usuários cadastrados', 'Sair', ])
    if resposta == 1:
        # aqui cadastra uma nova pessoa.
        cabeçalho('CADASTRO NOVO')
        nome = str(input('Nome: '))
        sobre_nome = str(input('Sobrenome: '))
        cadastrar(arquivo, nome, sobre_nome)

    elif resposta == 2:
        # aqui lista o conteúdo do arquivo.
        lerArquivo(arquivo)

    elif resposta == 3:
        # aqui você sai do sistema.
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        # Quando digitar uma opção inválida no menu.
        print('\033[31mErro! Opção inválida, digite novamente!\033[m')
    sleep(2)
