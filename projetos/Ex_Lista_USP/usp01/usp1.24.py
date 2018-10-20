"""
São dados dois numeros positivos p e q,
sendo que o numero de digitos de p <= numero de digitos de q.
Verificar se p é solúvel em q
"""

p, q = [input('p = '), input('q = ')]
p, q = [str(p), str(q)]

if len(p) >= len(q): print('Numeros inválidos!')

else:
    soluvel = False
    for i in range(0, len(q) - 1):
        if p[::] == q[i:len(p) + i]:
            soluvel = True

    if soluvel: print('Solúvel')
    else: print('Insolúvel')