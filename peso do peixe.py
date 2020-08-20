a = float(input('Peso: '))
if a < 50:
    print('Não tem multa')
else:
    multa = (a - 50) * 4
    print('Multado')
    print(f'Multa {multa:.2f}')
    
