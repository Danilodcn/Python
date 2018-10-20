# Dados dois Strings, um contendo uma frase e um contendo uma palavra, determine
# quantas vezes a palavra ocorre na frase.

palavra = input("Palavra : ")
frase = input("Frase  : ")
palavra = palavra.upper()
frase = frase.upper()

numero = 0

for i in range(len(frase) - len(palavra) + 1):
    if palavra == frase[i:i + len(palavra)]:
        numero += 1


print(numero)