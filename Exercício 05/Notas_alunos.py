Nota01=int(input("Informe sua Primeira nota:"))
Nota02=int(input("Informe sua Segunda nota:"))

Media = (Nota01 + Nota02) /2

if Media > 7 and Media < 10:
    print("Aprovado!")
elif Media < 7 :
    print("Reprovado!")
elif Media == 10:
    print("Aprovado com Distinção")
else:
    print("Erro!!!")

