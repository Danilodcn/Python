# Tentando descobrir se um dado era viciado, o dono de um cassino honesto o lançou n vezes.
# Dados um inteiro positivo n e os resultados dos n lançamentos,
# determinar o numero de ocorrencias de cada lançamento

n = 20000

import random

ocorrencias = {}
for i in range(n):
    face = random.randrange(1, 7)
    face = str(face)
    if face not in ocorrencias.keys():
        ocorrencias[face] = 1
    else:
        ocorrencias[face] += 1

for face, ocorrencia in sorted(ocorrencias.items()):
    print(face + "\t" + str(ocorrencia))