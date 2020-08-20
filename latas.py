a = int(input('metros:'))
if a % 54 == 0:
    latas = a / 54
else:
    latas = int(a / 54) + 1
valor = latas * 80
print(f'{latas}latas')
print(f'Total:R${valor:.2f}')
