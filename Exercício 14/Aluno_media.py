nota1=float(input("Entre com Primeira nota: "))
nota2=float(input("Entre com Segunda nota: "))

media = (nota1 + nota2) / 2
aproveitamento  = ""


if media >= 9 and media <= 10:
    aproveitamento  = "A"
elif media >= 7.5 and media <= 9:
    aproveitamento  = "B"
elif media >= 6 and media < 7.5:
    aproveitamento  = "C"
elif media >= 4 and media < 6:
    aproveitamento  = "D"
elif media >= 0 and media < 4:
    aproveitamento  = "E"

print("Nota 1 : {}".format(nota1))
print("Nota 2 : {}".format(nota2))
print("Média : {}".format(media))
print("Conceito : {}".format(aproveitamento))

if aproveitamento == "A" or aproveitamento == "B" or aproveitamento == "C":
    print("Aprovado")
else:
    print("Reprovado")




    
    
