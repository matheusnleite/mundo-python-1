preco=float(input('Digite o preço: '))
desconto = (5/100) * preco
nvalor = preco - desconto

print('Valor com 5% de desconto: R${:.2f}'.format(nvalor))