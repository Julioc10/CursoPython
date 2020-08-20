pagina = open('Calculadora do tio.html', 'w')
pagina.write('<html lang=\'pt-BR\'>\n')
pagina.write('<head>\n')
pagina.write('<title>Pagina em HTML com Python</title>\n')
pagina.write('</head>\n')
pagina.write('<bory>\n')
pagina.write('Calculadora\n')
x = int(input('Digite um numero:'))
y = int(input('Digite outro numero:'))
s = x + y
m = x * y
d = x / y
print(f'A soma é {s} \nA multiplicação é {m} \nE a divisão é {d}')
pagina.write(f'<p></p>\n % {x} {y}')
pagina.write('</bory>\n')
pagina.write('</html\n>')
pagina.close()
