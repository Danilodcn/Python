"""
Nesse arquivo estam definidos alguns metodos especificos de matrizes como adicao, subtracao e multiplicacao.
Nele tambem sera possivel identificar o tipo de matriz
"""

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def str_matriz(matriz):
    """matriz -> str
    converte uma matriz em uma string pronta para aplicar a função print
    """
    str_matriz = ""
    str_matriz += str(matriz[0])
    try:
        for i in range(len(matriz) - 1):
            str_matriz += "\n" + str(matriz[i + 1])
    except: None
            
    return str_matriz

def imprime_matriz(matriz):
    """Imprime a matriz de uma maneira mais amigavel:
    [a1, a2, a3, ...]
    [b1, b2, b3, ...]
    [. , . , . , ...]
    [. , . , . , ...]
    [. , . , . , ...]
    """
    print(str_matriz(matriz))


def get_elemento(matriz, i, j, valor):
    """(matriz, int, int, real)
    altera o elemento [i][j] da matriz"""
    matriz[i][j] = valor

def _matriz(n_linhas, n_colunas, valor=0):
    """(int, int, int) -> matriz
    Esse metodo serve para criar uma matriz"""

    #repete n_linas vezes
    matriz = []
    for i in range(n_linhas):
        linha = []
        #repete n_colunas vezes
        for j in range(n_colunas):
            linha.append(valor)
        
        matriz.append(linha)
    return matriz

def cria_matriz():
    """Esse metodo possibilita ao usuario digitar cada elemento da martriz"""

    n_linhas = int(input("Digite o numero de linhas: "))
    n_colunas = int(input("Digite o numero de colunas: "))
    matriz = _matriz(n_linhas, n_colunas)    #cria uma matriz nula n_linhas x n_colunas
    for i in range(len(matriz)):    #itera sobre as linhas da matriz
        for j in range(len(matriz[i])):     #itera sobre os elementos das colunas
            valor = input("Digite o valor do elemento [{}][{}]: ".format(i, j))
             
            #identifica o tipo de numero digitado
            if "." in valor:    
                get_elemento(matriz, i, j, float(valor))
                
            else: get_elemento(matriz, i, j, int(valor))
    return matriz