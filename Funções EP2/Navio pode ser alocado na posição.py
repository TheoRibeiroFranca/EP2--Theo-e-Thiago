def posicao_suporta(mapa, blocos, linha, coluna, orientação):
    if mapa[linha][coluna] == "N":
        return False
    if orientação == "v":
        if (linha + blocos)-1 > len(mapa):
            return False
        else:
            for i in range(linha, linha + blocos):
                if mapa[i][coluna] == "N":
                    return False
            return True
    if orientação == "h":
        for linhas_mapa in mapa:  
            if (coluna + blocos)-1 > len(linhas_mapa):
                return False
            else:
                for j in range(coluna, coluna + blocos):
                    if mapa[linha][j] == "N":
                        return False
                return True
mapa = [
    [' ', ' ', ' ', 'N'],
    [' ', ' ', ' ', 'N'],
    ['N', 'N', ' ', 'N'],
    [' ', ' ', ' ', ' ']
]
blocos = 2
linha = 1
coluna = 0
orientação = "v"
print(posicao_suporta(mapa, blocos, linha, coluna, orientação))
                