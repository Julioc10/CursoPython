notas = []
k = 0
soma = 0
while k <= 3:
    notas.append(float(input('Notas:')))
    soma = soma + notas [k]
    k = k + 1
print(f'Média {notas} é {soma/4:.1f}')
