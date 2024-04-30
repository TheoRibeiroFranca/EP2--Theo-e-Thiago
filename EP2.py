import random
from math import *

# Navio pode ser alocado na posição
def posicao_suporta(mapa, blocos, linha, coluna, orientação):
    if mapa[linha][coluna] == "N":
        return False
    if orientação == "v":
        if (linha + blocos) > len(mapa):
            return False
        else:
            for i in range(linha, linha + blocos):
                if mapa[i][coluna] == "N":
                    return False
            return True
    if orientação == "h":
        for linhas_mapa in mapa:  
            if (coluna + blocos) > len(linhas_mapa):
                return False
            else:
                for j in range(coluna, coluna + blocos):
                    if mapa[linha][j] == "N":
                        return False
                return True

# Alocando navios para o computador
def aloca_navios(mapa,blocos):
    linhas = len(mapa)
    colunas = len(mapa[0])
    linha = random.randint(0, linhas - 1)
    coluna = random.randint(0, colunas - 1)
    orientacao = random.choice(['h', 'v']) 
    for barcos in blocos:
        a = posicao_suporta(mapa, barcos, linha, coluna, orientacao)
        while a != True:
            linha = random.randint(0, linhas - 1)
            coluna = random.randint(0, colunas - 1)
            orientacao = random.choice(['h', 'v'])
            a = posicao_suporta(mapa, barcos, linha, coluna, orientacao)
        if orientacao == 'v':
            for i in range(linha, linha + barcos):
                mapa[i][coluna] = 'N'
        if orientacao == 'h':
            for j in range(coluna, coluna+barcos):
                mapa[linha][j] = 'N'
    return mapa

# Cria matriz quadrada de espaços
def cria_mapa(n):
    listona = []
    linha_referencia = [' '] * n

    for i in range(0,n):
        listona.append(linha_referencia)
    
    return listona

# Verifica se acabou os 'N's da matriz
def foi_derrotado(matriz):
    for linhas in matriz:
        for elementos in linhas:
            if elementos == "N":
                return False
    return True

# quantidade de blocos por modelo de navio
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

# frotas de cada pais
PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

# alfabeto para montar o nome das colunas
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# cores para o terminal
CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

# lista países
paises = ['Brasil','França','Austrália','Rússia','Japão']

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-- CÓDIGO DO JOGO ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Título
print (' ===================================== \n')
print ('|                                     |\n')
print ('| Bem-vindo ao INSPER - Batalha Naval |\n')
print ('|                                     |\n')
print (' =======   XXXXXXXXXXXXXXXXX   ======= \n')

print ()
























































