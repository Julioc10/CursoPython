'''
Fazendo uma regra de três
1 dia = 1440 minutos = 144 cigarros
'''
cigarros = int(input('cigarros dia: '))
anos = int(input('Anos fumando: '))
total_cigarros = anos * 365 * cigarros
dias = total_cigarros / 144
print (f'voce perdeu {dias:.1f} dias')
