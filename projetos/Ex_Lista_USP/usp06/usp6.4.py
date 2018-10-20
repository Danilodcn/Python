# Dados um inteiro positivo n e dois vetores x e y, calcular o produto escalar desses vetores

class Vetor:
    def __init__(self, cordenadas):
        self.cordenadas = cordenadas
    def getCordenadas(self):
        return self.cordenadas
    def produtoEscalar(self, other):
        if len(self.cordenadas) is len(other.cordenadas):
            produto = 0
            for i in range(len(self.cordenadas)):
                parcela = self.cordenadas[i] * other.cordenadas[i]
                produto += parcela
            return produto
        return ValueError

def cordenadas(n):
    import random
    cordenadas = []
    limites = 1
    for i in range(n):
        cordenadas.append(random.randrange(-limites, limites + 1))
    return cordenadas

def main():
    dimensao = 2
    x = Vetor(cordenadas(dimensao))
    y = Vetor(cordenadas(dimensao))
    print(x.cordenadas)
    print(y.cordenadas)
    print(x.produtoEscalar(y))

if __name__ == '__main__':
    main()