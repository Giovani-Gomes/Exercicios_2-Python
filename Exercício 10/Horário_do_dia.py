Horario = str(input("Informe seu Turno \n [M]-Matutino \n [V]-Vespertino \n [N]- Noturno \n").upper())

if Horario == 'M':
    print("Você Digitou Matutino")
elif Horario == 'V':
    print("Você Digitou Vespertino")
elif Horario == 'N':
    print("Você Digitou Noturno")
else:
    print("Valor inválido")