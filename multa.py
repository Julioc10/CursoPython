v = int(input('velocidade: '))
if v > 110:
    print ('voce esta multado! ')
    multa = (v - 110) * 5
    print (f'multa R$ {multa:.2f}')
