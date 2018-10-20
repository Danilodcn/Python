#Converter celcius para Farenheint
# -*- coding: cp1252 -*-

print("programa para Converção")

while(True):
    print("\nDigite a opção Desejada")
    print("0.....Sair do Programa")
    print("1.....Celsius pra Farenheint")
    print("2.....Farenheint para Celsius")
    escolha=int(input("Opção: "))

    if(escolha==0):
        break
    elif(escolha==1):
        tempC=float(input("Digite a temperatura em graus Celsius: "))
        tempF=tempC*(9.0/5.0)+32.0
        print("%.2f °C  equivale a %.2f °F" %(tempC, tempF))

    elif(escolha==2):
        F=float(input("Digite a temperatura em graus Farenheint: "))
        C=5*(F-32)/9
        print("%.2f °F equivale a %.2f °C" %(F, C))

    else:
        print("Opção inválida")

    
print("Fim do programa")
