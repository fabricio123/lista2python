n1 = int(input('digite um numero: '))
n2 = int(input('digite um número: '))
n3 = int(input('digite um numero: '))

maior = n1

if n2 > maior:
    maior = n2
    if n3 > maior:
      maior = n3

    menor = n1

if n2 < menor:
    maior = n2
    if n3 < menor:
      menor = n3
        
print('o maior é:' , maior)
print(' o menor é:', menor)
