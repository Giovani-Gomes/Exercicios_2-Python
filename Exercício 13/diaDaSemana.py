dia = int(input("Entre com um dia da semana (1-7):"))

if(dia == 1):
    print("Domingo")
elif(dia == 2):
    print("Segunda")
elif(dia == 3):
    print("Terça")
elif(dia == 4):
    print("Quarta")
elif(dia == 5):
    print("Quinta")
elif(dia == 6):
    print("Sexta")
elif(dia == 7):
    print("Sábado")
elif(dia < 1 or dia > 7 ):
    print("Número inválido")