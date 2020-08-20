s = float(input('salario: '))
p = float(input('aumento%: '))
aumento = s * p / 100
novo = s + aumento
print(f'aumento: R$ {aumento: .2f}')
print(f'novo salario: R$ {novo: .2f}')
