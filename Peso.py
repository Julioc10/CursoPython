a = float(input('Peso:'))
if a > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    multa = excesso = 0
print(f'Multa {multa:.2f}')
print(f'Excesso:{excesso:.2f}')
