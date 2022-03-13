preco_Produto1 = float(input("Digite o Preço do primeiro produto: "))
preco_Produto2= float(input("Digite o Preço do segundo produto: "))
preco_Produto3= float(input("Digite o Preço do terceiro produto: "))


if preco_Produto1 < preco_Produto2 and preco_Produto1 < preco_Produto3 :
    print("Compre o Primeiro produto - Menor Preço")
elif preco_Produto2 < preco_Produto1 and preco_Produto2 < preco_Produto3 :
    print("Compre o Segundo produto - Menor Preço")
elif preco_Produto3 < preco_Produto2 and preco_Produto3 < preco_Produto1 :
    print("Compre o Terceiro produto - Menor Preço")
else:
    print("Numeros iguais.")