Num1 = int(input("Informe o Primeiro Número: "))
Num2 = int(input("Informe o Segundo Número: "))

if Num1 > Num2:
    print("{} é Maior que {}".format(Num1,Num2))
elif Num2 > Num1:
    print("{} é Maior que {}".format(Num2,Num1))
elif Num2 == Num1:
    print("Números iguais")
