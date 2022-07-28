from exdesafio.lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<15}{dado[1]:>3}')
    finally:
        a.close()


def cadastrar(arquivo, nome='campo não informado', sobre_nome='segundo campo não informado'):
    try:
        a = open(arquivo, 'at')
    except:
        print('ERRO ao abrir o arquivo!')
    else:
        try:


            a.write(f'NOME: {nome};Sobrenome: {sobre_nome}\n')
        except:
            print('Teve um erro ao escrever os dados!')
        else:
            print(f'Novo registro de "{nome} {sobre_nome}", adicionado')
            a.close()
