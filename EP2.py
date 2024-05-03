import random
from math import *

# Navio pode ser alocado na posição
def posicao_suporta(mapa, blocos, linha, coluna, orientação):
    if mapa[linha][coluna] == " N":
        return False
    if orientação == "v":
        if (linha + blocos) > len(mapa):
            return False
        else:
            for i in range(linha, linha + blocos):
                if mapa[i][coluna] == " N":
                    return False
            return True
    if orientação == "h":
        for linhas_mapa in mapa:  
            if (coluna + blocos) > len(linhas_mapa):
                return False
            else:
                for j in range(coluna, coluna + blocos):
                    if mapa[linha][j] == " N":
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
                mapa[i][coluna] = ' N'
        if orientacao == 'h':
            for j in range(coluna, coluna+barcos):
                mapa[linha][j] = ' N'
    return mapa

# Cria matriz quadrada de espaços
def cria_mapa(n):
    listona = []
    linha_referencia = ['  '] * n

    for i in range(0,n):
        listona.append(linha_referencia)
    
    return listona

# Verifica se acabou os 'N's da matriz
def foi_derrotado(matriz):
    for linhas in matriz:
        for elementos in linhas:
            if elementos == " N":
                return False
    return True

#função para criar um mapa para o print
def mapa_print(pc, jog, pais_pc, pais_jogador):
    return(f'''
 COMPUTADOR - {pais_pc}                    JOGADOR - {pais_jogador}
    A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J          
 1 {pc[0][0]} {pc[0][1]} {pc[0][2]} {pc[0][3]} {pc[0][4]} {pc[0][5]} {pc[0][6]} {pc[0][7]} {pc[0][8]} {pc[0][9]}  1    1 {jog[0][0]} {jog[0][1]} {jog[0][2]} {jog[0][3]} {jog[0][4]} {jog[0][5]} {jog[0][6]} {jog[0][7]} {jog[0][8]} {jog[0][9]}  1
 2 {pc[1][0]} {pc[1][1]} {pc[1][2]} {pc[1][3]} {pc[1][4]} {pc[1][5]} {pc[1][6]} {pc[1][7]} {pc[1][8]} {pc[1][9]}  2    2 {jog[1][0]} {jog[1][1]} {jog[1][2]} {jog[1][3]} {jog[1][4]} {jog[1][5]} {jog[1][6]} {jog[1][7]} {jog[1][8]} {jog[1][9]}  2
 3 {pc[2][0]} {pc[2][1]} {pc[2][2]} {pc[2][3]} {pc[2][4]} {pc[2][5]} {pc[2][6]} {pc[2][7]} {pc[2][8]} {pc[2][9]}  3    3 {jog[2][0]} {jog[2][1]} {jog[2][2]} {jog[2][3]} {jog[2][4]} {jog[2][5]} {jog[2][6]} {jog[2][7]} {jog[2][8]} {jog[2][9]}  3
 4 {pc[3][0]} {pc[3][1]} {pc[3][3]} {pc[3][3]} {pc[3][4]} {pc[3][5]} {pc[3][6]} {pc[3][7]} {pc[3][8]} {pc[3][9]}  4    4 {jog[3][0]} {jog[3][1]} {jog[3][3]} {jog[3][3]} {jog[3][4]} {jog[3][5]} {jog[3][6]} {jog[3][7]} {jog[3][8]} {jog[3][9]}  4
 5 {pc[4][0]} {pc[4][1]} {pc[4][4]} {pc[4][3]} {pc[4][4]} {pc[4][5]} {pc[4][6]} {pc[4][7]} {pc[4][8]} {pc[4][9]}  5    5 {jog[4][0]} {jog[4][1]} {jog[4][4]} {jog[4][3]} {jog[4][4]} {jog[4][5]} {jog[4][6]} {jog[4][7]} {jog[4][8]} {jog[4][9]}  5 
 6 {pc[5][0]} {pc[5][1]} {pc[5][5]} {pc[5][3]} {pc[5][4]} {pc[5][5]} {pc[5][6]} {pc[5][7]} {pc[5][8]} {pc[5][9]}  6    6 {jog[5][0]} {jog[5][1]} {jog[5][5]} {jog[5][3]} {jog[5][4]} {jog[5][5]} {jog[5][6]} {jog[5][7]} {jog[5][8]} {jog[5][9]}  6
 7 {pc[6][0]} {pc[6][1]} {pc[6][2]} {pc[6][3]} {pc[6][4]} {pc[6][5]} {pc[6][6]} {pc[6][7]} {pc[6][8]} {pc[6][9]}  7    7 {jog[6][0]} {jog[6][1]} {jog[6][2]} {jog[6][3]} {jog[6][4]} {jog[6][5]} {jog[6][6]} {jog[6][7]} {jog[6][8]} {jog[6][9]}  7
 8 {pc[7][0]} {pc[7][1]} {pc[7][2]} {pc[7][3]} {pc[7][4]} {pc[7][5]} {pc[7][6]} {pc[7][7]} {pc[7][8]} {pc[7][9]}  8    8 {jog[7][0]} {jog[7][1]} {jog[7][2]} {jog[7][3]} {jog[7][4]} {jog[7][5]} {jog[7][6]} {jog[7][7]} {jog[7][8]} {jog[7][9]}  8
 9 {pc[8][0]} {pc[8][1]} {pc[8][2]} {pc[8][3]} {pc[8][4]} {pc[8][5]} {pc[8][6]} {pc[8][7]} {pc[8][8]} {pc[8][9]}  9    9 {jog[8][0]} {jog[8][1]} {jog[8][2]} {jog[8][3]} {jog[8][4]} {jog[8][5]} {jog[8][6]} {jog[8][7]} {jog[8][8]} {jog[8][9]}  9
10 {pc[9][0]} {pc[9][1]} {pc[9][2]} {pc[9][3]} {pc[9][4]} {pc[9][5]} {pc[9][6]} {pc[9][7]} {pc[9][8]} {pc[9][9]}  10  10 {jog[9][0]} {jog[9][1]} {jog[9][2]} {jog[9][3]} {jog[9][4]} {jog[9][5]} {jog[9][6]} {jog[9][7]} {jog[9][8]} {jog[9][9]}  10
    A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J    
''')
#função para alocar os navios do jogador
def navio_jogador(mapa, barco, linha, coluna, orientação):
    a = posicao_suporta(mapa, barco, linha, coluna, orientação)
    while a != True:
        print("Espaço inválido")
        print("tente de novo")
        linha = input("qual linha") 
        coluna = input("qual coluna")
        orientação = input("qual orientação")
        a = posicao_suporta(mapa, barco, linha, coluna, orientação)
    if orientação == 'v':
        for i in range(linha, linha + barco):
            mapa[i][coluna] = ' N'
    if orientação == 'h':
        for j in range(coluna, coluna+barco):
            mapa[linha][j] = ' N'
    return mapa
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

# lista de 1 a 5
lista_de_um_a_cinco = [1,2,3,4,5]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-- CÓDIGO DO JOGO ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Título
print (' ===================================== \n')
print ('|                                     |\n')
print ('| Bem-vindo ao INSPER - Batalha Naval |\n')
print ('|                                     |\n')
print (' =======   XXXXXXXXXXXXXXXXX   ======= \n')

# texto pré infos
pais_pc = random.choice(paises)

print ('Iniciando o Jogo! \n')

print ('Computador está alocando os navios de guerra do país {0}...'.format(pais_pc))
print ('Computador já está em posição de batalha! \n')

# Infos Brasil
print('1: Brasil \n')

print('\t 1 cruzador \n')
print('\t 2 torpedeiro \n')
print('\t 1 destroyer \n')
print('\t 1 couracado \n')
print('\t 1 porta-avioes \n')     

# Infos França
print('2: França \n')

print('\t 3 cruzador \n')
print('\t 1 porta-avioes \n')
print('\t 1 destroyer \n')
print('\t 1 submarino \n')
print('\t 1 couracado \n')  

# Infos Austrália 
print('3: Austrália \n')

print('\t 1 couracado \n')
print('\t 3 cruzador \n')
print('\t 1 submarino \n')
print('\t 1 porta-avioes \n')
print('\t 1 torpedeiro \n')

# Infos Rússia
print('4: Rússia \n')

print('\t 1 cruzador \n')
print('\t 1 porta-avioes \n')
print('\t 2 couracado \n')
print('\t 1 destroyes \n')
print('\t 1 submarino \n')

# Infos Japão
print('5: Japão \n')

print('\t 2 torpedeiros \n')
print('\t 1 cruzador \n')
print('\t 2 destroyer \n')
print('\t 1 couracado \n')
print('\t 1 submarino \n')

# listas para checagem de inputs corretos
lista_linhas_checagem = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
lista_colunas_checagem = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
lista_orientacao_checagem = ["h","v"]
# Pergunta ao jogador com que país ele deseja jogar
n_pais_jogador = int(input('Qual o número da nação da sua frota?  \n'))


while True:
    if n_pais_jogador not in lista_de_um_a_cinco:
        print('Opção inválida \n')
        n_pais_jogador = int(input('Qual o número da nação da sua frota?  \n'))
    else:
        break

dic_pais = {1: "Brasil" ,2: "França" ,3: "Austrália" ,4: "Rússia" ,5: "Japão"}
pais_jogador = dic_pais[n_pais_jogador]

#Mensagem sobre o país do jogador e início para printar o mapa e continuar o jogo
print("Você escolheu {0} \nAgora é sua vez de alocar seus navios de guerra! \n".format(pais_jogador))

# INÍNIO - Criar o mapa do computador e do jogador
#############
mapa_jogador = cria_mapa(10)
mapa_computador = cria_mapa(10)

#Cria os mapas printáveis

mapa_printado = mapa_print(mapa_computador,mapa_jogador,pais_pc,pais_jogador)
print(mapa_printado)

# FIM - Criar o mapa do computador e do jogador

#posicionamento dos barcos para o computador
barcos_computador = PAISES[pais_pc]
lista_barcos_computador = []
if 'cruzador' in barcos_computador:
    for n in range(barcos_computador["cruzador"]):
        lista_barcos_computador.append(2)
if 'torpedeiros' in barcos_computador:
    for n in range(barcos_computador["torpedeiros"]):
        lista_barcos_computador.append(3)
if 'destroyer' in barcos_computador:
    for n in range(barcos_computador["destroyer"]):
        lista_barcos_computador.append(3)
if 'couracado' in barcos_computador:
    for n in range(barcos_computador["couracado"]):
        lista_barcos_computador.append(4)
if 'porta-avioes' in barcos_computador:
    for n in range(barcos_computador["porta-avioes"]):
        lista_barcos_computador.append(5)
if 'submarino' in barcos_computador:
    for n in range(barcos_computador["submarino"]):
        lista_barcos_computador.append(2)
print(lista_barcos_computador)
mapa_computador = aloca_navios(mapa_computador,lista_barcos_computador)
print(mapa_computador)

#alocando os barcos para o jogador
barcos_jogador = PAISES[pais_jogador]
lista_barcos_jogador = []
lista_nomes_barcos_jogador = []
if 'cruzador' in barcos_jogador:
    for n in range(barcos_jogador["cruzador"]):
        lista_barcos_jogador.append(2)
        lista_nomes_barcos_jogador.append("cruzador")
if 'torpedeiros' in barcos_jogador:
    for n in range(barcos_jogador["torpedeiros"]):
        lista_barcos_jogador.append(3)
        lista_nomes_barcos_jogador.append("torpedeiros")
if 'destroyer' in barcos_jogador:
    for n in range(barcos_jogador["destroyer"]):
        lista_barcos_jogador.append(3)
        lista_nomes_barcos_jogador.append("destroyer")
if 'couracado' in barcos_jogador:
    for n in range(barcos_jogador["couracado"]):
        lista_barcos_jogador.append(4)
        lista_nomes_barcos_jogador.append("couracado")
if 'porta-avioes' in barcos_jogador:
    for n in range(barcos_jogador["porta-avioes"]):
        lista_barcos_jogador.append(5)
        lista_nomes_barcos_jogador.append("porta-avioes")
if 'submarino' in barcos_jogador:
    for n in range(barcos_jogador["submarino"]):
        lista_barcos_jogador.append(2)
        lista_nomes_barcos_jogador.append("submarino")

for i in range(len(lista_nomes_barcos_jogador)):
    mapa_printado = mapa_print(mapa_computador,mapa_jogador,pais_pc,pais_jogador)
    print(mapa_printado)
    alocar = (f"alocar: {lista_nomes_barcos_jogador[i]} ({lista_barcos_jogador[i]} casas)")
    proximos = ",".join(lista_nomes_barcos_jogador[i + 1:])
    print(alocar)
    print(f"Próximos:{proximos}")
    linha = input("qual linha")
    coluna = input("qual Letra")
    coluna = coluna.upper()
    while linha not in lista_linhas_checagem:
        print("Linha inválida")
        linha = input("qual linha")
    linha = lista_linhas_checagem.index(linha)
    while coluna not in lista_colunas_checagem:
        print('Letra inválida')
        coluna = input("qual Letra")
        coluna = coluna.upper()
    coluna = lista_colunas_checagem.index(coluna)
    orientação = input("qual orientação[h/v]")
    orientação = orientação.lower()
    while orientação not in lista_orientacao_checagem:
        print("Orientação inválida")
        orientação = input("qual orientação[h/v]")
        orientação = orientação.lower()
    navio_jogador(mapa_jogador, lista_barcos_jogador[i],linha,coluna,orientação)

    
    







































































