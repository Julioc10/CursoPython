m = float(input('preço: '))
p = float(input('desconto%: '))
desconto = m * p / 100
novo = m - desconto
print (f'desconto: R$ {desconto: .2f}')
print (f'preço a pagar: {novo: .2f}')
