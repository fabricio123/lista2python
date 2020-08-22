n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))

media = (n1+n2)/2

if media > 6.9 and media < 10:
    print('aprovado com a media: ', media)

if media < 7:
     print('reprovado com a media: ',media)

if media == 10:
     print('aprovado com distinção, media:', media) 
