nota1 = float(input("Digite nota 1 : "))
nota2 = float(input("Digite nota 2 : "))
nota3 = float(input("Digite nota 3 : "))

media =(nota1+nota2+nota3) / 3

if media >= 7:
    if media >=10:
        print("Aprovado com Distinção")
    else:
        print("Aprovado")
if media < 7:
    print("Reprovado")