# a) escreva uma função que recebe um caractere ch e devolve em tipo 0 se o caractere for inteiro,
# 1 se for letra, 0 caso contrario; e alem disso, no caso de o caractere ser letra,
# converte para maiuscula, se nao develve ch inalterado


def converte(ch):
    if type(ch) is int:
        tipo = 0
    elif type(ch) is str:
        tipo = 1
        ch = ch.upper()
        return ch, tipo
    else: tipo = 2
    return ch, tipo

sequencia = ('a', 'b', 2, 's')

def maiusculas(sequencia):
    seqAlterada = []
    for i in sequencia:
        if converte(i)[1] is 1:
            seqAlterada += converte(i)[0]
    return seqAlterada

print(maiusculas(sequencia))
