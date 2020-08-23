produto1 = float(input('digite o valor do primeiro produto: '))
produto2 = float(input('digite o valor do segundo produto: '))
produto3 = float(input('digite o valor do terceiro produto: '))

maisbarato = produto1

if produto2 < maisbarato:
    maisbarato = produto2
    if produto3 < maisbarato:
      maisbarato = produto3
        
print(' o produto mais barato é:', maisbarato)
