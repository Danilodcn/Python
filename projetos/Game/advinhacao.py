import random

def main():
    k = random.randrange(0, 100)
    print(k)
    i = 0
    while i < 1:
        
        print(i, " tentativa: digite um numero entre 0 e 100  ")
        n = int(input())

        if (k == n):
            print("Voce venceu!!!!!!!!")
            break
        elif (k < n):
            print("Desculpe, mas o numero digitado é muito GRANDE")
        elif (k > n):
            print("Desculpe, mas o numero digitado é muito PEQUENO")
        else:
            print("Erro!!!!")
            i -= 1
        i += 1

    a = int(input("Digite 0  para o jogar novamente  "))
    if a == 0:
        main()
    
main()
