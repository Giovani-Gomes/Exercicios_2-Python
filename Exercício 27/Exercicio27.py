
Quantidade_morangos = int(input("Digite a quantidade de morangos [kg]: "))
Quantidade_macas = int(input("Digite a quantidade de maças [kg]: "))
preco_morango = Quantidade_morangos * 2.50
preco_morango2 = Quantidade_morangos * 2.20

preco_maca = Quantidade_macas * 1.80
preco_maca2 = Quantidade_macas * 1.50

print("Quantidade de maçãs: ", Quantidade_macas, "\nQuantidade de morangos: ", Quantidade_morangos)

if Quantidade_morangos > 5:
    preco_certo_morango = preco_morango
else:
    preco_certo_morango = preco_morango2

if Quantidade_macas > 5:
    preco_certo_maca = preco_maca
else:
    preco_certo_maca = preco_maca2

preco_total = preco_certo_maca + preco_certo_morango

if preco_total > 25 or (Quantidade_macas + Quantidade_morangos) > 8:
    print("Preço final: ", (preco_total - (preco_total * 0.1)))
else:
    print("Preço final: ", preco_total)