def posicao_suporta(mapa, blocos, linha, coluna, orientação):
    if mapa[linha][coluna] == "N":
        return False
    if orientação == "v":
        if (coluna + blocos)-1 > len(mapa):
            return False
        else:
            for i in range(coluna, coluna + blocos):
                if mapa[i][coluna] == "N":
                    return False
                else:
                    return True
    if orientação == "h":
        for linhas_mapa in mapa:  
            if (linha + blocos)-1 > len(linhas_mapa):
                return False
            else:
                for j in range(linha, linha + blocos):
                    if mapa[linha][j] == "N":
                        return False
                    else:
                        return True
                