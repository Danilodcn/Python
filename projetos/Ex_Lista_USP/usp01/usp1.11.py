"""Função que verifica se um número n dado é primo """

#Essa função retorna se um dado número n é primo.
def primo(n):
    primo = False
    if n <= 0:
        print('Erro o número {} é negativo!'.format(n))
    else:
        for i in range(2, int(n ** (1 / 2)) + 2):
            if n == 2:
                primo = True
                break
            elif n % i == 0:
                primo = False
                break
            else: primo = True
        if primo:
            print('O número {} é primo'.format(n))
        else:
            print('O número {} não é primo'.format(n))
    return 0


n = int(input('Digite um número positivo: '))
primo(n)

