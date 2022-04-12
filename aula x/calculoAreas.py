from cmath import pi


print('[a] Quadrado')
print('[b] Circulo')
print('[c] Triangulo')

ask = input('Qual voce quer calcular?  ').lower()

if ask == 'a':
    print('[A] Area')
    print('[B] Perimetro')
    askAgain = input('O que voce quer calcular do Quadrado?  ').upper()

    if askAgain == 'A':
        lado = float(input('Qual o tamanho do lado do Quadrado?   '))
        area = lado ** 2
        print(f'Area: {round(area, 2)}')

    elif askAgain == 'B':
        lado = float(input('Qual o tamanho do lado do Quadrado?   '))
        perimetro = lado * 4
        print(f'Perimetro: {round(perimetro, 2)}')


elif ask == 'b':
    print('[A] Area')
    print('[B] Perimetro')
    askAgain = input('O que voce quer calcular do Circulo?   ').upper()

    if askAgain == 'A':
        raio = float(input('Qual o raio do Circulo?   '))
        area = (raio ** 2) * pi
        print(f'Area: {round(area, 2)}')

    elif askAgain == 'B':
        raio = float(input('Qual o raio do Circulo?   '))
        perimetro = 2 * (pi * raio)
        print(f'Perimetro: {round(perimetro, 2)}')


elif ask == 'c':
    print('[A] Area')
    print('[B] Perimetro')
    askAgain = input('O que voce quer calcular do Triangulo?   ').upper()

    if askAgain == 'A':
        base = float(input('Qual a base do Triangulo?   '))
        altura = float(input('Qual a altura do Triangulo?   '))
        area = (base * altura) / 2
        print(f'Area: {area}')
    elif askAgain == 'B':
        lado1 = float(input('Qual o valor do lado 1?   '))
        lado2 = float(input('Qual o valor do lado 2?   '))
        lado3 = float(input('Qual o valor do lado 3?   '))
        perimetro = lado1 + lado2 + lado3
        print(f'Perimetro: {perimetro}')