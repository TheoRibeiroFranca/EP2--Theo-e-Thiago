def foi_derrotado(matriz):
    for linhas in matriz:
        for elementos in linhas:
            if elementos == "N":
                return False
    return True
print(foi_derrotado([
    ['N', ' ', ' ', 'X'],
    ['N', 'A', 'X', ' '],
    ['X', ' ', 'N', ' '],
    ['A', ' ', 'N', ' ']
]))