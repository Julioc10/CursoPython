minutos = int(input('minutos: '))
if minutos < 200:
    preço = 0.2
else:
    if minutos <= 400:
        preço = 0.18
    else:
        preço = 0.15
print (f'R$ {preço*minutos: .2f}')
