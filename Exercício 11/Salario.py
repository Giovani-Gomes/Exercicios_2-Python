salario = float(input("Infome seu Salário: "))

if salario <= 280.00:
    aumento = 0.2
    salarioReajustado = salario * aumento
    valorAumento = salario -  salarioReajustado
    print("Salário sem reajuste {} ".format(salario))
    print("O percentual de aumento aplicado: {} ".format(aumento))
    print("Valor de Aumento {} ".format(valorAumento))
    print("Salário Reajustado {} ".format(salarioReajustado))

elif salario > 280.00 and 700.00:
    aumento = 0.15
    salarioReajustado = salario * aumento
    valorAumento = salario - salarioReajustado
    print("Salário sem reajuste {} ".format(salario))
    print("O percentual de aumento aplicado: {} ".format(aumento))
    print("Valor de Aumento {} ".format(valorAumento))
    print("Salário Reajustado {} ".format(salarioReajustado))
elif salario > 700.00 and 1500.00:
    aumento = 0.1
    salarioReajustado = salario * aumento
    valorAumento = salario - salarioReajustado
    print("Salário sem reajuste {} ".format(salario))
    print("O percentual de aumento aplicado: {} ".format(aumento))
    print("Valor de Aumento {} ".format(valorAumento))
    print("Salário Reajustado {} ".format(salarioReajustado))
elif salario > 1500.00:
    aumento = 0.05
    salarioReajustado = salario * aumento
    valorAumento = salario - salarioReajustado
    print("Salário sem reajuste {} ".format(salario))
    print("O percentual de aumento aplicado: {} ".format(aumento))
    print("Valor de Aumento {} ".format(valorAumento))
    print("Salário Reajustado {} ".format(salarioReajustado))
else:
    print("Error")