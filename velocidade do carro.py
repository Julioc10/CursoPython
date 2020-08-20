Velocidade = int(input('Velocidade do carro: '))
if Velocidade > 110:
    print('Esta acima do limite')
    multa = (Velocidade - 110) * 5
    print (f'Multa R$ {multa:.2f}')
