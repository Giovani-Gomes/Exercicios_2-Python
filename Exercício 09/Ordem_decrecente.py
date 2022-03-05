num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
num3 = int(input("Informe último número: "))

if num1 < num2 and num1 < num3 and num2 < num3 :
    print("{0} {1} {2} ".format(num3 , num2, num1)) 
elif num1 > num2 and num1 < num3 and num2 < num3 :
    print("{0} {1} {2} ".format(num3, num1, num2))
elif num1 < num2 and num1 < num3 and num2 > num3 :
    print("{0} {1} {2} ".format(num2 , num3, num1))
elif num1 < num2 and num1 > num3 and num2 > num3 :
    print("{0} {1} {2} ".format(num2 , num1, num3))
elif num1 > num2 and num1 > num3 and num2 < num3 :
    print("{0} {1} {2} ".format(num1 , num2, num3))
elif num1 > num2 and num1 < num3 and num2 > num3 :
    print("{0} {1} {2} ".format(num1 , num3, num2))
else:
    print("Números iguais")











