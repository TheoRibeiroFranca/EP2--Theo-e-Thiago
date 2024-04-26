def foi_derrotado(matriz):
    for linhas in matriz:
        for i in range(len(linhas)):
            if matriz[linhas][i] == "N":
                return False
    return True