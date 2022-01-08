Num1 = int(input("Informe o Primeiro número: "))
Num2 = int(input("Informe o Segundo número: "))
Num3 = int(input("Informe o Terceiro número: "))

if Num1 > Num2 and Num1 > Num3:
    print("{0} é o maior".format(Num1))
elif Num2 > Num1 and Num2 > Num3:
    print("{0} é o maior".format(Num2))
elif Num3 > Num2 and Num3 > Num1:
    print("{0} é o maior".format(Num3) )
else:
    print("Os números são iguais")