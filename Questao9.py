a = int(input('digite um número: '))
b = int(input('digite um número: '))
c = int(input('digite um número: '))
if a < c: 
  a, c = c, a

if a < b: 
  a, b = b, a 

if b < c: 
  b, c = c, b 

print(f'A ordem decrescente é {a}, {b} e {c}')
