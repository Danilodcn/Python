def exer_01():

    with open("planolandia.txt", "r", encoding="utf-8") as arq:
        texto = arq.read()

    dic = {"a": 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
           'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
           'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
           'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
           'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
           'z': 0}

    dic2 = {"a": 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
            'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
            'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
            'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
            'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
            'z': 0}
    chrs = [["a", "á", "ã", "â"], ["b"], ["c", "ç"], ["d"], ["e", "é", "ê", "ẽ"], ["f"],
            ["g"], ["h"], ["i", "í"], ["j"], ["k"], ["l"], ["m"], ["n"], ["o", "ó", "õ"],
            ["p"], ["q"], ["r"], ["s"], ["t"], ["u", "ú"], ["v"], ["w"], ["x"], ["y"], ["z"]]

    for chr in texto:
        for a in chrs:
            if chr.lower() in a:
                dic[a[0]] += 1
                break

        if chr.lower() in dic2.keys():
            dic2[chr.lower()] += 1

    for chr in dic.keys():
        if dic[chr]:
            print(chr, "\t", dic[chr], "\t", dic2[chr])

def exer_03():
    import collections as c

    with open("planolandia.txt", "r") as arq:
        texto = arq.read()

    dic = {}

    for s in texto.split():
        if s not in dic.keys():
            dic[s.lower()] = 1
        else:
            dic[s.lower()] += 1

    l = sorted(dic.items())

    for (x, y) in l:
        print(x, y)








def ordena(lista):

    dic = {'a': 0, 'b': 1, 'c': 2, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
           'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
           'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
           'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    var = lista[0]
    lista2 = []

    def ordenar(str1, str2):
        """ordena duas strings"""
        if len(str1) > len(str2):
            str1, str2 = (str2, str1)

        for i in range(len(str1)):
            if dic[str1[i]] > dic[str2[i]]:
                return str2, str1
        return str1, str2

    for i in range(0, len(lista) - 1):
        for j in range(i + 1, len(lista)):
            lista[i], lista[j] = ordenar(lista[i], lista[j])
            break
    print(lista)

def exer_04():
    with open("planolandia.txt", "r") as arq:
        texto = arq.read()
        palavras = texto.lower().split()

    maior = palavras[0]
    maiores = []
    for palavra in palavras:
        if len(palavra) > len(maior):
            maior = palavra
            maiores.clear()
            maiores.append(maior)
        if len(palavra) == len(maior) and not palavra == maior:
            maiores.append(palavra)


    for i in maiores:
        #if len(i) == len(maior):
        print(i, "\t",len(i))

def exer_05():
    """Escreva um programa que pergunta ao usuário uma frase em portugues
    e imprime a tradução da frase para a língua dos piratas."""

    pirata = {"portugues" : "pirata", "senhor": "matey", "hotel" : "fleabag inn",
              "estudante" : "swabbie", "garoto" : "matey", "senhora" : "proud beauty",
              "professor" : "foul blaggart", "restaurante" : "galley", "seu" : "yer",
              "com lisença" : "arr", "estudantes" : "swabbies", "sao" : "be",
              "advogado" : "foul blaggart", "o" : "th’","a": "th’", "os": "th’",
              "as": "th’","meu": "me", "minha": "me", "oi": "avast",
              "ola": "avast", "estao": "be","homem": "matey", "e" : "be"}

    texto = "ele e o homem"
    #texto = input("Entre com um texto:")
    texto = texto.lower()
    traducao = ""
    for palavra in texto.split():
        if palavra in pirata.keys():
            traducao = traducao + pirata[palavra] + " "
        else:
            traducao = traducao + palavra + " "
    print(traducao)

exer_05()
seq = [1, 2, 3, 4, 5, 6,7]
x= 2
for i in range(len(seq)):
        print(i)