#Importações
import random

#Modo de Exibição
def printa(  algo  ):
    print('')
    print('~' * 75)
    print('|')
    print(f'|  {algo}')
    print('|')
    print('~' * 75)
    print('')


#Calculo
def calculaPi(  numeros  ):
    Points__Circle = Points__Square = 0

    for _ in range (numeros):
        valor__x, valor__y = random.uniform(0, 1), random.uniform(0, 1)
        calculo = valor__x**2 + valor__y**2

        if (calculo <= 1):
            Points__Circle += 1
        Points__Square += 1

    pi = 4 * (Points__Circle / Points__Square)
    return printa(pi)


calculaPi(10000000)