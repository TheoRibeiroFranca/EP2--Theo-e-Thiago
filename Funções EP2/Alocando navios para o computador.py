import random
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
