from app import valida

nota_valida = 0
nota = 0
media_das_notas = 0
while nota_valida != 2:
        nota = float(input())
        if valida(nota):
            media_das_notas += nota / 2
            nota_valida = nota_valida + 1
        else:
            print('nota invalida')


print('media = %.2f' % (media_das_notas))