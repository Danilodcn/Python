#Uma pessoa aplicou x complexos (moeda local) a juros de z% mensais durante 1 ano.
#Determinar o montante de cada mes durante o ano#


x = float(input('x = '))    #Capital
z = float(input('z = '))    #Taxa de juros

m = 0   #Montante

#Percorre todos os meses do ano
for i in range(0, 13):
    j = m * z / 100
    m = x + j
    print('No mes {} o motante será {}'.format(i, m))
