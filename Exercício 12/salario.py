valorHora= float(input("Entre com o valor/hora: "))
qtdHoras= float(input("Entre com as horas trabalhadas no mês: "))

salarioBruto= valorHora * qtdHoras

percentualIR = 0
if salarioBruto <= 900:
    percentualIR = 0
elif salarioBruto > 900 and salarioBruto <= 1500:
    percentualIR = 5
elif salarioBruto > 1500 and salarioBruto <= 2500:
    percentualIR = 10
elif salarioBruto > 2500:
    percentualIR = 20

ir = (salarioBruto / 100) * percentualIR
inss = (salarioBruto / 100) * 10
fgts = (salarioBruto / 100) * 11
totalDescontos =ir + inss
salarioLiquido =  salarioBruto - totalDescontos


print("Salário Bruto: ({} * {}) : {} )" .format(valorHora, qtdHoras , salarioBruto))
print("(-) IR ({}%) : {}".format(percentualIR, ir))
print("(-) INSS (10%): {}".format(fgts))
print("FTGS (11%): {}" .format(fgts))
print("Total de descontos: {}".format(totalDescontos))
print("Salário Líquido: {}".format(salarioLiquido))