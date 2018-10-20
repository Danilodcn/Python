# Dadas as populaçoes de Uauá(BA) e Nova York(PI) e sabendo que a população de Uauá
# tem um crescimento anual x e a populaçao de Nova York tem um crescimento y determine:
# 1. Se a população da cidade menor ultrapassa a maior
# 2. Quantos anos passaram antes que isso ocorra

P_UA = int(input('Quantos habitantes existem em Uauá(BA)? '))
x = int(input('Qual o crescimento de Uauá(BA)? '))
P_NY = int(input('Quantos habitantes existem em Nova York(PI)? '))
y = int(input('Qual o crescimento de Nova York(PI)? '))




# funçao principal
def main(x, y, P_UA, P_NY):
    tempo = 0
    lista = []

    while True:
        parar = False
        parou = False

        if (P_UA > P_NY) and x >= y:
            print('Nova York nunca será mais populosa que Uauá')
            parar = True
            parou = True

        elif (P_NY > P_UA) and y >= x:
            print('Uauá nunca será mais populosa que Nova York')
            parar = True
            parou = True

        elif (P_UA + x * tempo) > (P_NY + y * tempo):
            lista.append(1)

        elif (P_NY + y * tempo) > (P_UA + x * tempo):
            lista.append(2)
        if len(lista) >= 3:
            del lista[0]
        for i in range(len(lista) - 1):
            if lista[i] != lista[i + 1]: parar = True

        if parar: break

        tempo += 1
    if not parou:
        len(lista)
        if lista[1] == 2:
            print('Nova York terá população maior em', tempo, 'anos')

        elif lista[1] == 1:
            print('Uauá terá população maior em', tempo, 'anos')
    print(lista)


main(x, y, P_UA, P_NY)
