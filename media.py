n = 1
soma = 0
while n <= 10:
    x = int(input(f'{n} numero:'))
    soma = soma + x
    n = n + 1
print(f'Media: {soma/10:.1f}')
