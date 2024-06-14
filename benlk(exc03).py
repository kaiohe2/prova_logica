# exercicio 3: verificação de ano bissexto

ano = int(input('digite um ano: '))
if ano % 4 == 0:
    print('O ano é BISSEXTO')
else:
    print('O ano NÃO é BISSSEXTO')