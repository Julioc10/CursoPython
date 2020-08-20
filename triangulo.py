a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))
if a > b + c or b > c + a or c > a + b:
 print('Não pode ser um triangulo')
 print('Um dos lados é maior que a soma dos outros')
elif a == b == c:
 print('Equilatero')
elif a == b or b == c or a == c:
 print('Isósceles')
else:
 print('Escaleno')
