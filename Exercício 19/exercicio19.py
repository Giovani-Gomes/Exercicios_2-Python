numero = int(input('Digite um numero inteiro positivo: '))

unidade = numero % 10

numero = (numero - unidade) / 10

dezena = numero % 10

numero = (numero - dezena) / 10
centena = numero

dezena = int(dezena)
centena = int(centena)
print('{}, centena(s), {}, dezena(s) e, {}, unidade(s)'.format(centena,dezena,unidade))