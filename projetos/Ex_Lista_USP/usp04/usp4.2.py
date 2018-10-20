# a) escreeva uma funçao encaixa que, recebendo dois numeros inteiros
# a e b como paramentros, verifica se b corresponde aos ultimos digitos de a
# b) usando a funçao do item anterior, faça um programa que le dois numeros a e b
# e verifica de o menor deles e segmento do outro


# função encaixa
def encaixa(a, b):
    a, b = [str(a), str(b)]
    if a[len(a) - len(b):] == b[::]:
        return True
    else:
        return False


# função retorna True ou False
def segmento(a, b):
    a, b = [str(a), str(b)]
    c = []
    c.append(a[:len(a) - len(b) - 1])
    segmento = True
    for i in a[len(a) - len(b) - 1:]:
        if encaixa(c, b):
            segmento = False
            break
        c.append(i)
    if segmento:
        return True
    else: return False



print(segmento(12332146246, 146))
